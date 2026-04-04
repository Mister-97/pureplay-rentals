// Pure Play Rentals — Event Reminder Email Sender
// Sends friendly reminder emails via Resend the day before and day of the event.
//
// Two cron jobs (already configured in Supabase):
//   Day-before  0 14 * * *  → body: '{"offset":1}'   (9 AM Chicago)
//   Day-of      0 13 * * *  → body: '{"offset":0}'   (8 AM Chicago)
//
// Secrets required (Project Settings → Edge Functions → Secrets):
//   RESEND_API_KEY

import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

const RESEND_API_KEY = Deno.env.get('RESEND_API_KEY')!
const FROM = 'Pure Play Rentals <bookings@pureplayrentals.com>'

const supabase = createClient(
  Deno.env.get('SUPABASE_URL')!,
  Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
)

function getChicagoDateString(offsetDays = 0): string {
  const d = new Date()
  d.setDate(d.getDate() + offsetDays)
  const fmt = new Intl.DateTimeFormat('en-US', {
    timeZone: 'America/Chicago',
    year: 'numeric', month: '2-digit', day: '2-digit',
  })
  const parts = fmt.formatToParts(d)
  const y = parts.find(p => p.type === 'year')!.value
  const m = parts.find(p => p.type === 'month')!.value
  const day = parts.find(p => p.type === 'day')!.value
  return `${y}-${m}-${day}`
}

function formatDate(dateStr: string): string {
  const [y, m, d] = dateStr.split('-')
  const months = ['January','February','March','April','May','June','July','August','September','October','November','December']
  return `${months[parseInt(m) - 1]} ${parseInt(d)}, ${y}`
}

async function sendEmail(to: string, subject: string, html: string) {
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${RESEND_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ from: FROM, to, subject, html }),
  })
  if (!res.ok) {
    const err = await res.text()
    throw new Error(`Resend error: ${err}`)
  }
  return res.json()
}

function buildDayBeforeEmail(booking: any): string {
  const dateFormatted = formatDate(booking.booking_date)
  const remaining = (parseFloat(booking.total_amount || '300') - parseFloat(booking.deposit_amount || '100')).toFixed(2)
  return `
    <div style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto;color:#222;">
      <div style="background:#0d1f3c;padding:28px 32px;border-radius:12px 12px 0 0;text-align:center;">
        <h1 style="color:#fff;margin:0;font-size:24px;">See You Tomorrow! 🏰</h1>
        <p style="color:rgba(255,255,255,0.75);margin:8px 0 0;font-size:14px;">Pure Play Rentals</p>
      </div>
      <div style="background:#fff;border:1px solid #e5e7eb;border-top:none;border-radius:0 0 12px 12px;padding:32px;">
        <p style="font-size:16px;">Hi <strong>${booking.first_name}</strong>! 👋</p>
        <p style="font-size:15px;color:#444;line-height:1.7;">Just a friendly reminder that your <strong>${booking.inflatable_name}</strong> is scheduled for <strong>${dateFormatted}</strong>. We're excited to make your event amazing!</p>

        <div style="background:#f0fdf4;border:1.5px solid #86efac;border-radius:10px;padding:18px 22px;margin:24px 0;">
          <p style="margin:0;font-size:15px;color:#15803d;font-weight:bold;">✅ Your deposit is confirmed — you're all set!</p>
        </div>

        <div style="background:#fef3c7;border:1.5px solid #fcd34d;border-radius:10px;padding:18px 22px;margin:24px 0;">
          <p style="margin:0 0 6px;font-size:14px;font-weight:bold;color:#92400e;">💵 Remaining Balance: $${remaining}</p>
          <p style="margin:0;font-size:14px;color:#92400e;">We'll collect the remaining balance <strong>in person on the day of your event</strong>. Cash is preferred — no need to do anything now!</p>
        </div>

        <p style="font-size:14px;color:#6b7280;line-height:1.7;">Our team will be in touch to confirm your delivery window. If you have any questions, give us a call or text at <strong>(708) 669-5486</strong>.</p>
        <p style="font-size:14px;color:#6b7280;">We'll see you tomorrow! 🎉</p>
        <p style="margin-top:32px;font-size:13px;color:#9ca3af;">— The Pure Play Rentals Team<br>pureplayrentals.com</p>
      </div>
    </div>
  `
}

function buildDayOfEmail(booking: any): string {
  const dateFormatted = formatDate(booking.booking_date)
  const remaining = (parseFloat(booking.total_amount || '300') - parseFloat(booking.deposit_amount || '100')).toFixed(2)
  return `
    <div style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto;color:#222;">
      <div style="background:#f7941d;padding:28px 32px;border-radius:12px 12px 0 0;text-align:center;">
        <h1 style="color:#fff;margin:0;font-size:24px;">Today's the Day! 🎉</h1>
        <p style="color:rgba(255,255,255,0.85);margin:8px 0 0;font-size:14px;">Pure Play Rentals</p>
      </div>
      <div style="background:#fff;border:1px solid #e5e7eb;border-top:none;border-radius:0 0 12px 12px;padding:32px;">
        <p style="font-size:16px;">Hi <strong>${booking.first_name}</strong>! 🎊</p>
        <p style="font-size:15px;color:#444;line-height:1.7;">Your <strong>${booking.inflatable_name}</strong> is on its way today — <strong>${dateFormatted}</strong>. Get ready for an awesome event!</p>

        <div style="background:#f0fdf4;border:1.5px solid #86efac;border-radius:10px;padding:18px 22px;margin:24px 0;">
          <p style="margin:0;font-size:15px;color:#15803d;font-weight:bold;">✅ Deposit paid — thank you for booking with Pure Play Rentals!</p>
        </div>

        <div style="background:#fef3c7;border:1.5px solid #fcd34d;border-radius:10px;padding:18px 22px;margin:24px 0;">
          <p style="margin:0 0 6px;font-size:14px;font-weight:bold;color:#92400e;">💵 Remaining Balance Due Today: $${remaining}</p>
          <p style="margin:0;font-size:14px;color:#92400e;">Our team will collect the remaining balance <strong>in person at delivery</strong>. Cash is preferred — please have it ready!</p>
        </div>

        <p style="font-size:14px;color:#6b7280;line-height:1.7;">Questions about your delivery time? Call or text us at <strong>(708) 669-5486</strong> and we'll get you sorted right away.</p>
        <p style="font-size:14px;color:#6b7280;">Thank you for choosing Pure Play Rentals — enjoy every moment! 🏰</p>
        <p style="margin-top:32px;font-size:13px;color:#9ca3af;">— The Pure Play Rentals Team<br>pureplayrentals.com</p>
      </div>
    </div>
  `
}

serve(async (req) => {
  let offset = 0
  try {
    const body = await req.json()
    offset = typeof body.offset === 'number' ? body.offset : 0
  } catch (_) { /* default day-of */ }

  const targetDate = getChicagoDateString(offset)
  const type = offset === 0 ? 'day-of' : 'day-before'
  console.log(`Sending ${type} reminders for ${targetDate}`)

  const { data: bookings, error } = await supabase
    .from('bookings')
    .select('*')
    .eq('booking_date', targetDate)
    .eq('status', 'paid')

  if (error) {
    console.error('DB error:', error)
    return new Response('Database error', { status: 500 })
  }

  if (!bookings || bookings.length === 0) {
    console.log(`No bookings for ${targetDate}`)
    return new Response(JSON.stringify({ date: targetDate, sent: 0 }), {
      headers: { 'Content-Type': 'application/json' },
    })
  }

  const results = []
  for (const booking of bookings) {
    try {
      const subject = offset === 0
        ? `🎉 Today's the Day — Your Bounce House is Coming! | Pure Play Rentals`
        : `🏰 See You Tomorrow! Your Bounce House Reminder | Pure Play Rentals`

      const html = offset === 0
        ? buildDayOfEmail(booking)
        : buildDayBeforeEmail(booking)

      await sendEmail(booking.email, subject, html)
      console.log(`Reminder sent → ${booking.email}`)
      results.push({ id: booking.id, email: booking.email, status: 'sent' })
    } catch (err: any) {
      console.error(`Failed booking ${booking.id}:`, err.message)
      results.push({ id: booking.id, email: booking.email, status: 'error', error: err.message })
    }
  }

  return new Response(JSON.stringify({ date: targetDate, type, results }), {
    headers: { 'Content-Type': 'application/json' },
  })
})
