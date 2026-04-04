const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY)
const { Resend } = require('resend')

// Required to read raw body for Stripe signature verification
export const config = { api: { bodyParser: false } }

const resend = new Resend(process.env.RESEND_API_KEY)

async function getRawBody(req) {
  return new Promise((resolve, reject) => {
    let data = ''
    req.on('data', chunk => { data += chunk })
    req.on('end', () => resolve(Buffer.from(data)))
    req.on('error', reject)
  })
}

async function sendConfirmationEmail(meta, depositPaid) {
  const remainingBalance = (parseFloat(meta.totalAmount) - depositPaid).toFixed(2)

  // 1. Customer confirmation
  await resend.emails.send({
    from: 'Pure Play Rentals <bookings@pureplayrentals.com>',
    to: meta.email,
    subject: '🎉 Your Booking is Confirmed — Pure Play Rentals',
    html: `
      <div style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto;color:#222;">
        <div style="background:#7c3aed;padding:32px;text-align:center;border-radius:12px 12px 0 0;">
          <h1 style="color:#fff;margin:0;font-size:26px;">Booking Confirmed!</h1>
          <p style="color:#e9d5ff;margin:8px 0 0;">Pure Play Rentals</p>
        </div>
        <div style="background:#f9fafb;padding:32px;border-radius:0 0 12px 12px;border:1px solid #e5e7eb;">
          <p style="font-size:16px;">Hi <strong>${meta.firstName}</strong>, your deposit is in and your rental is locked in! 🎊</p>

          <table style="width:100%;border-collapse:collapse;margin:24px 0;">
            <tr style="background:#ede9fe;">
              <td style="padding:10px 14px;font-weight:bold;border-radius:6px 0 0 6px;">Rental Item</td>
              <td style="padding:10px 14px;border-radius:0 6px 6px 0;">${meta.rentalItem}</td>
            </tr>
            <tr>
              <td style="padding:10px 14px;font-weight:bold;">Event Date</td>
              <td style="padding:10px 14px;">${meta.eventDate}</td>
            </tr>
            <tr style="background:#f3f4f6;">
              <td style="padding:10px 14px;font-weight:bold;">Event Address</td>
              <td style="padding:10px 14px;">${meta.address}</td>
            </tr>
            <tr>
              <td style="padding:10px 14px;font-weight:bold;">Deposit Paid</td>
              <td style="padding:10px 14px;color:#16a34a;font-weight:bold;">$${depositPaid.toFixed(2)}</td>
            </tr>
            <tr style="background:#f3f4f6;">
              <td style="padding:10px 14px;font-weight:bold;">Remaining Balance</td>
              <td style="padding:10px 14px;color:#dc2626;font-weight:bold;">$${remainingBalance}</td>
            </tr>
            <tr>
              <td style="padding:10px 14px;font-weight:bold;">Total</td>
              <td style="padding:10px 14px;">$${parseFloat(meta.totalAmount).toFixed(2)}</td>
            </tr>
            ${meta.notes ? `
            <tr style="background:#f3f4f6;">
              <td style="padding:10px 14px;font-weight:bold;">Notes</td>
              <td style="padding:10px 14px;">${meta.notes}</td>
            </tr>` : ''}
          </table>

          <div style="background:#fffbeb;border:1px solid #fcd34d;border-radius:8px;padding:16px;margin-bottom:24px;">
            <p style="margin:0;font-size:14px;color:#92400e;">
              <strong>⚠️ Remaining balance of $${remainingBalance}</strong> is due on the day of your event in cash or via payment link we'll send closer to the date.
            </p>
          </div>

          <p style="font-size:14px;color:#6b7280;">Questions? Reply to this email or text us at <strong>(708) 669-5486</strong>.</p>
          <p style="font-size:14px;color:#6b7280;">We can't wait to make your event amazing! 🏰</p>

          <p style="margin-top:32px;font-size:13px;color:#9ca3af;">— The Pure Play Rentals Team<br>pureplayrentals.com</p>
        </div>
      </div>
    `
  })

  // 2. Owner + manager notification
  const ownerEmailHtml = `
    <div style="font-family:Arial,sans-serif;max-width:580px;margin:0 auto;color:#222;">
      <div style="background:#f7941d;padding:20px 24px;border-radius:12px 12px 0 0;">
        <p style="margin:0;font-size:13px;color:rgba(255,255,255,0.85);font-weight:bold;letter-spacing:1px;text-transform:uppercase;">Pure Play Rentals</p>
        <h2 style="margin:6px 0 0;color:#fff;font-size:22px;">🏰 New Bounce House Booking!</h2>
      </div>
      <div style="background:#fff;border:1px solid #e5e7eb;border-top:none;border-radius:0 0 12px 12px;padding:24px;">
        <div style="background:#f0fdf4;border:1.5px solid #86efac;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
          <p style="margin:0;font-size:15px;color:#15803d;font-weight:bold;">✅ Deposit of $${depositPaid.toFixed(2)} received — booking is confirmed</p>
        </div>
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <tr style="background:#fef3c7;">
            <td style="padding:11px 14px;font-weight:bold;width:140px;border-radius:6px 0 0 6px;">📞 Phone</td>
            <td style="padding:11px 14px;border-radius:0 6px 6px 0;"><a href="tel:${meta.phone}" style="color:#d97706;font-weight:bold;font-size:16px;text-decoration:none;">${meta.phone}</a></td>
          </tr>
          <tr>
            <td style="padding:11px 14px;font-weight:bold;">👤 Customer</td>
            <td style="padding:11px 14px;">${meta.firstName} ${meta.lastName}</td>
          </tr>
          <tr style="background:#f9fafb;">
            <td style="padding:11px 14px;font-weight:bold;">✉️ Email</td>
            <td style="padding:11px 14px;"><a href="mailto:${meta.email}" style="color:#4f46e5;">${meta.email}</a></td>
          </tr>
          <tr>
            <td style="padding:11px 14px;font-weight:bold;">🏰 Rental</td>
            <td style="padding:11px 14px;">${meta.rentalItem}</td>
          </tr>
          <tr style="background:#f9fafb;">
            <td style="padding:11px 14px;font-weight:bold;">📅 Event Date</td>
            <td style="padding:11px 14px;font-weight:bold;color:#1a1a2e;">${meta.eventDate}</td>
          </tr>
          <tr>
            <td style="padding:11px 14px;font-weight:bold;">📍 Address</td>
            <td style="padding:11px 14px;">${meta.address}</td>
          </tr>
          <tr style="background:#f9fafb;">
            <td style="padding:11px 14px;font-weight:bold;">💵 Deposit Paid</td>
            <td style="padding:11px 14px;color:#16a34a;font-weight:bold;">$${depositPaid.toFixed(2)}</td>
          </tr>
          <tr>
            <td style="padding:11px 14px;font-weight:bold;">💳 Remaining Due</td>
            <td style="padding:11px 14px;color:#dc2626;font-weight:bold;">$${remainingBalance}</td>
          </tr>
          <tr style="background:#f9fafb;">
            <td style="padding:11px 14px;font-weight:bold;">💰 Total</td>
            <td style="padding:11px 14px;">$${parseFloat(meta.totalAmount).toFixed(2)}</td>
          </tr>
          ${meta.notes ? `<tr><td style="padding:11px 14px;font-weight:bold;">📝 Notes</td><td style="padding:11px 14px;">${meta.notes}</td></tr>` : ''}
        </table>
        <p style="margin:20px 0 0;font-size:13px;color:#6b7280;">Call or text the customer to confirm delivery details at least 24 hours before the event.</p>
      </div>
    </div>
  `

  await Promise.all([
    resend.emails.send({
      from: 'Pure Play Rentals <bookings@pureplayrentals.com>',
      to: 'pureplayrentals@gmail.com',
      subject: `🏰 NEW BOOKING — ${meta.firstName} ${meta.lastName} | ${meta.eventDate} | $${depositPaid.toFixed(2)} paid`,
      html: ownerEmailHtml,
    }),
    resend.emails.send({
      from: 'Pure Play Rentals <bookings@pureplayrentals.com>',
      to: 'c4mgmtgroup@gmail.com',
      subject: `🏰 NEW BOOKING — ${meta.firstName} ${meta.lastName} | ${meta.eventDate} | $${depositPaid.toFixed(2)} paid`,
      html: ownerEmailHtml,
    }),
  ])
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).end()

  const sig = req.headers['stripe-signature']
  const rawBody = await getRawBody(req)

  let event
  try {
    event = stripe.webhooks.constructEvent(rawBody, sig, process.env.STRIPE_WEBHOOK_SECRET)
  } catch (err) {
    console.error('Webhook signature failed:', err.message)
    return res.status(400).send(`Webhook Error: ${err.message}`)
  }

  if (event.type === 'checkout.session.completed') {
    const session = event.data.object
    const meta = session.metadata
    const depositPaid = session.amount_total / 100

    console.log('✅ Payment confirmed:', {
      customer: `${meta.firstName} ${meta.lastName}`,
      email: meta.email,
      item: meta.rentalItem,
      date: meta.eventDate,
      address: meta.address,
      deposit: depositPaid,
      total: meta.totalAmount,
    })

    try {
      await sendConfirmationEmail(meta, depositPaid)
      console.log('📧 Confirmation emails sent to', meta.email)
    } catch (emailErr) {
      console.error('Email send failed:', emailErr.message)
    }
  }

  if (event.type === 'payment_intent.payment_failed') {
    const pi = event.data.object
    console.log('❌ Payment failed:', pi.id, pi.last_payment_error?.message)
  }

  res.status(200).json({ received: true })
}
