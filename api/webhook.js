const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY)

// Required to read raw body for Stripe signature verification
export const config = { api: { bodyParser: false } }

async function getRawBody(req) {
  return new Promise((resolve, reject) => {
    let data = ''
    req.on('data', chunk => { data += chunk })
    req.on('end', () => resolve(Buffer.from(data)))
    req.on('error', reject)
  })
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

    console.log('✅ Payment confirmed:', {
      customer: `${meta.firstName} ${meta.lastName}`,
      email: meta.email,
      item: meta.rentalItem,
      date: meta.eventDate,
      address: meta.address,
      deposit: session.amount_total / 100,
      total: meta.totalAmount,
    })

    // TODO: send confirmation email here
    // e.g. await sendConfirmationEmail(meta)
  }

  if (event.type === 'payment_intent.payment_failed') {
    const pi = event.data.object
    console.log('❌ Payment failed:', pi.id, pi.last_payment_error?.message)
  }

  res.status(200).json({ received: true })
}
