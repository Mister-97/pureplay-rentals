// Pure Play Rentals — Day-Of Invoice Sender
// Runs every morning at 8:00 AM Chicago time.
// Finds all paid bookings for today and sends a $200 remaining balance invoice via Stripe.
//
// HOW TO SCHEDULE (one-time setup):
//   Supabase Dashboard → Database → Extensions → enable "pg_cron"
//   Then: Database → Cron Jobs → + New Cron Job
//     Name:     send-day-of-invoice
//     Schedule: 0 13 * * *   (13:00 UTC = 8:00 AM Chicago time, adjust for DST if needed)
//     Command:
//       select net.http_post(
//         url := 'https://rrvneinvifudtujaupma.supabase.co/functions/v1/send-day-of-invoice',
//         headers := '{"Authorization": "Bearer YOUR_ANON_KEY", "Content-Type": "application/json"}'::jsonb,
//         body := '{}'::jsonb
//       );
//
// Secrets required (Supabase Dashboard → Project Settings → Edge Functions → Secrets):
//   STRIPE_SECRET_KEY      — from Stripe Dashboard → Developers → API Keys

import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'
import Stripe from 'https://esm.sh/stripe@14?target=deno'

const stripe = new Stripe(Deno.env.get('STRIPE_SECRET_KEY')!, {
  apiVersion: '2023-10-16',
  httpClient: Stripe.createFetchHttpClient(),
})

const supabase = createClient(
  Deno.env.get('SUPABASE_URL')!,
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
)

// Get today's date string in Chicago time (YYYY-MM-DD)
function getTodayChicago(): string {
  const fmt = new Intl.DateTimeFormat('en-US', {
    timeZone: 'America/Chicago',
    year:  'numeric',
    month: '2-digit',
    day:   '2-digit',
  })
  const parts = fmt.formatToParts(new Date())
  const y = parts.find(p => p.type === 'year')!.value
  const m = parts.find(p => p.type === 'month')!.value
  const d = parts.find(p => p.type === 'day')!.value
  return `${y}-${m}-${d}`
}

serve(async (_req) => {
  const todayStr = getTodayChicago()
  console.log(`Sending day-of invoices for ${todayStr}`)

  // Fetch all paid bookings for today that haven't been invoiced yet
  const { data: bookings, error: fetchErr } = await supabase
    .from('bookings')
    .select('*')
    .eq('booking_date', todayStr)
    .eq('status', 'paid')
    .eq('invoice_sent', false)

  if (fetchErr) {
    console.error('Error fetching bookings:', fetchErr)
    return new Response('Database error', { status: 500 })
  }

  if (!bookings || bookings.length === 0) {
    console.log('No bookings to invoice today.')
    return new Response(JSON.stringify({ date: todayStr, invoiced: 0 }), {
      headers: { 'Content-Type': 'application/json' },
    })
  }

  console.log(`Found ${bookings.length} booking(s) to invoice`)
  const results = []

  for (const booking of bookings) {
    try {
      // Find or create the Stripe customer
      let customerId: string = booking.stripe_customer_id

      if (!customerId) {
        const existing = await stripe.customers.list({ email: booking.email, limit: 1 })
        if (existing.data.length > 0) {
          customerId = existing.data[0].id
        } else {
          const customer = await stripe.customers.create({
            email: booking.email,
            name:  `${booking.first_name} ${booking.last_name}`,
            phone: booking.phone,
          })
          customerId = customer.id
        }
      }

      // Add the $200 remaining balance line item
      await stripe.invoiceItems.create({
        customer:    customerId,
        amount:      20000, // $200 in cents
        currency:    'usd',
        description: `Pure Play Rentals — ${booking.inflatable_name} rental on ${booking.booking_date} — Remaining Balance`,
      })

      // Create, finalize, and send the invoice
      const invoice = await stripe.invoices.create({
        customer:           customerId,
        collection_method:  'send_invoice',
        days_until_due:     1,
        metadata: {
          booking_id:   String(booking.id),
          booking_date: booking.booking_date,
        },
      })

      await stripe.invoices.finalizeInvoice(invoice.id)
      await stripe.invoices.sendInvoice(invoice.id)

      // Mark invoice sent in Supabase
      await supabase
        .from('bookings')
        .update({
          invoice_sent:    true,
          invoice_sent_at: new Date().toISOString(),
        })
        .eq('id', booking.id)

      console.log(`Invoice sent → ${booking.email} (booking ${booking.id})`)
      results.push({ id: booking.id, email: booking.email, status: 'sent' })

    } catch (err) {
      console.error(`Failed to invoice booking ${booking.id}:`, err.message)
      results.push({ id: booking.id, email: booking.email, status: 'error', error: err.message })
    }
  }

  return new Response(JSON.stringify({ date: todayStr, results }), {
    headers: { 'Content-Type': 'application/json' },
  })
})
