-- Add Stripe payment tracking + invoice columns to bookings table
ALTER TABLE bookings
  ADD COLUMN IF NOT EXISTS stripe_session_id   TEXT,
  ADD COLUMN IF NOT EXISTS stripe_customer_id  TEXT,
  ADD COLUMN IF NOT EXISTS deposit_paid_at     TIMESTAMPTZ,
  ADD COLUMN IF NOT EXISTS invoice_sent        BOOLEAN DEFAULT FALSE,
  ADD COLUMN IF NOT EXISTS invoice_sent_at     TIMESTAMPTZ;
