// Pure Play Rentals — Stripe Webhook Handler
// Fires when a customer completes the $100 deposit payment.
// Marks the booking as "paid" in Supabase.
//
// Secrets required (set in Supabase Dashboard → Project Settings → Edge Functions → Secrets):
//   STRIPE_SECRET_KEY      — from Stripe Dashboard → Developers → API Keys
//   STRIPE_WEBHOOK_SECRET  — from Stripe Dashboard → Developers → Webhooks (after adding endpoint)
//   SUPABASE_SERVICE_ROLE_KEY — already available automatically in edge functions

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

serve(async (req) => {
  const body = await req.text()
  const sig  = req.headers.get('stripe-signature')

  if (!sig) {
    return new Response('Missing stripe-signature header', { status: 400 })
  }

  let event: Stripe.Event
  try {
    event = await stripe.webhooks.constructEventAsync(
      body,
      sig,
      Deno.env.get('STRIPE_WEBHOOK_SECRET')!
    )
  } catch (err) {
    console.error('Webhook signature verification failed:', err.message)
    return new Response(`Webhook Error: ${err.message}`, { status: 400 })
  }

  if (event.type === 'checkout.session.completed') {
    const session = event.data.object as Stripe.Checkout.Session

    // client_reference_id is the booking row ID we pass from the booking page
    const bookingId = session.client_reference_id

    if (!bookingId) {
      console.warn('checkout.session.completed received with no client_reference_id', session.id)
      return new Response('ok', { status: 200 })
    }

    const { error } = await supabase
      .from('bookings')
      .update({
        status:             'paid',
        stripe_session_id:  session.id,
        stripe_customer_id: (session.customer as string) || null,
        deposit_paid_at:    new Date().toISOString(),
      })
      .eq('id', bookingId)

    if (error) {
      console.error('Supabase update failed for booking', bookingId, error)
      return new Response('Database error', { status: 500 })
    }

    console.log(`Booking ${bookingId} marked as paid — session ${session.id}`)
  }

  return new Response('ok', { status: 200 })
})
