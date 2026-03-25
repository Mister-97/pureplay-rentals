#!/usr/bin/env python3
"""Generate city-specific SEO landing pages for Pure Play Rentals."""

import os

cities = [
    {
        "slug": "naperville",
        "name": "Naperville",
        "county": "DuPage County",
        "lat": "41.7508",
        "lon": "-88.1535",
        "zip": "60540",
        "desc": "Naperville's top-rated bounce house rental. Pure Play Rentals delivers, sets up, and takes down at your Naperville backyard, park, or event venue.",
        "hero_sub": "From Naperville's best backyards to Centennial Beach events, Pure Play brings the bounce to you. Delivered, set up, and sanitized.",
        "faq": [
            ("How much does bounce house rental cost in Naperville?",
             "Pure Play Rentals offers bounce house rentals in Naperville for $300 per day. This flat rate includes delivery, setup, and takedown within 20 miles of Chicago."),
            ("Does Pure Play Rentals deliver bounce houses to Naperville parks?",
             "Yes! We deliver to Naperville backyard parties, Centennial Park, DuPage River Trail events, and most public parks. We just need a power source within 100 feet."),
            ("How far in advance should I book a bounce house in Naperville?",
             "We recommend booking 1-2 weeks in advance for weekends, especially during summer. Last-minute bookings are sometimes available — call or book online to check availability."),
            ("Is your bounce house rental service licensed and insured in Naperville?",
             "Yes. Pure Play Rentals is fully insured and complies with all Illinois and DuPage County requirements for inflatable party equipment rentals."),
        ]
    },
    {
        "slug": "schaumburg",
        "name": "Schaumburg",
        "county": "Cook County",
        "lat": "42.0334",
        "lon": "-88.0834",
        "zip": "60173",
        "desc": "Bounce house rental in Schaumburg IL. Pure Play Rentals delivers premium inflatables to Schaumburg parties, events, and backyards. Book online today.",
        "hero_sub": "Serving Schaumburg families, schools, and corporate events. Pure Play delivers premium inflatables straight to your door — we set up, you celebrate.",
        "faq": [
            ("How much does it cost to rent a bounce house in Schaumburg?",
             "Pure Play Rentals offers bounce house rentals in Schaumburg for $300 per day. Delivery, professional setup, and takedown are all included."),
            ("Do you deliver bounce houses to Schaumburg parks and forest preserves?",
             "Yes! We deliver to backyards, Spring Valley Nature Center events, Busse Woods picnic areas, and most Schaumburg park locations. We require a power outlet within 100 feet."),
            ("What neighborhoods in Schaumburg do you serve?",
             "We serve all of Schaumburg including Weathersfield, Springbrook, Remington, Plum Grove, Schaumburg Township, and surrounding communities like Hoffman Estates and Elk Grove Village."),
            ("Can I get a bounce house delivered same-day in Schaumburg?",
             "Same-day delivery in Schaumburg is sometimes available based on schedule. We recommend booking online at least 1 week in advance for weekend dates."),
        ]
    },
    {
        "slug": "aurora",
        "name": "Aurora",
        "county": "Kane / DuPage County",
        "lat": "41.7606",
        "lon": "-88.3201",
        "zip": "60505",
        "desc": "Bounce house rental Aurora IL. Pure Play Rentals delivers inflatable party rentals to Aurora backyards and events. $300/day, free delivery and setup.",
        "hero_sub": "Aurora's City of Lights deserves a party that shines. Pure Play delivers premium bounce houses to Aurora neighborhoods, parks, and venues — setup included.",
        "faq": [
            ("How much does bounce house rental cost in Aurora IL?",
             "Pure Play Rentals rents bounce houses in Aurora for $300 per day. That price includes delivery from Chicago, professional setup, and takedown at your location."),
            ("Do you serve all of Aurora including North Aurora and Montgomery?",
             "Yes! We serve all of Aurora — the Fox Valley, downtown Aurora, North Aurora, and nearby communities like Montgomery, Oswego, and Batavia."),
            ("What is the biggest bounce house you have for an Aurora party?",
             "Our rainbow combo castle with slide is our most popular unit — great for backyard birthday parties in Aurora. It fits 6-8 kids safely at once."),
            ("Do I need a permit to rent a bounce house at an Aurora park?",
             "Some Aurora parks require permits for inflatable equipment. We recommend checking with Aurora Parks & Recreation. We're happy to help with the paperwork process."),
        ]
    },
    {
        "slug": "joliet",
        "name": "Joliet",
        "county": "Will County",
        "lat": "41.5250",
        "lon": "-88.0817",
        "zip": "60432",
        "desc": "Bounce house rental Joliet IL. Pure Play Rentals delivers inflatable rentals to Joliet and Will County. Safe, sanitized, and set up at your door. $300/day.",
        "hero_sub": "Joliet families love Pure Play. We deliver, inflate, and set up at your backyard or venue — all you have to do is show up and have fun.",
        "faq": [
            ("How much does a bounce house rental cost in Joliet?",
             "Pure Play Rentals rents bounce houses in Joliet for $300 per day, including delivery, setup, and takedown anywhere in the Joliet area."),
            ("Do you deliver to Joliet parks and event venues?",
             "Yes! We deliver to Joliet backyards, Bicentennial Park, Pilcher Park, Joliet Memorial Stadium events, and most Will County outdoor venues."),
            ("How long is the rental period for a Joliet bounce house booking?",
             "All rentals are full-day (up to 8 hours). We arrive 60 minutes early to set up so your party time is never cut short."),
            ("Do you serve New Lenox, Plainfield, and other Joliet suburbs?",
             "Absolutely. We serve all of Will County including New Lenox, Plainfield, Crest Hill, Lockport, Romeoville, and Shorewood."),
        ]
    },
    {
        "slug": "orland-park",
        "name": "Orland Park",
        "county": "Cook County",
        "lat": "41.6031",
        "lon": "-87.8537",
        "zip": "60462",
        "desc": "Bounce house rental Orland Park IL. Pure Play Rentals delivers premium inflatables to Orland Park parties and events. Free setup. Book online.",
        "hero_sub": "Orland Park's favorite bounce house company. We deliver premium inflatables to your backyard, the park, or any venue in the southwest suburbs.",
        "faq": [
            ("What does it cost to rent a bounce house in Orland Park?",
             "Pure Play Rentals offers bounce house rentals in Orland Park for $300 per day. This includes delivery, setup, and pickup — no hidden fees."),
            ("Do you serve Tinley Park, Mokena, and other Orland Park area towns?",
             "Yes! We serve all southwest Cook County suburbs including Tinley Park, Mokena, Frankfort, Matteson, and Homewood."),
            ("How early do you arrive to set up the bounce house?",
             "We arrive 60 minutes before your party start time to set up, inflate, and do a safety inspection — so everything's ready when your guests arrive."),
            ("Can you deliver a bounce house to Orland Park's Wolf Road Prairie or parks?",
             "We deliver to most parks and open spaces in Orland Park. Some locations may require permits — check with the Orland Park Park District. We're happy to help."),
        ]
    },
    {
        "slug": "arlington-heights",
        "name": "Arlington Heights",
        "county": "Cook County",
        "lat": "42.0886",
        "lon": "-87.9806",
        "zip": "60004",
        "desc": "Bounce house rental Arlington Heights IL. Pure Play Rentals delivers premium inflatable party rentals to Arlington Heights. $300/day, delivery and setup included.",
        "hero_sub": "Serving Arlington Heights and the northwest suburbs with premium inflatable rentals. We deliver, set up, and take down so you can focus on the party.",
        "faq": [
            ("How much is bounce house rental in Arlington Heights?",
             "Pure Play Rentals rents bounce houses in Arlington Heights for $300 per day, which includes delivery, professional setup, and takedown."),
            ("Do you serve Mount Prospect, Palatine, and Rolling Meadows?",
             "Yes — we serve all northwest suburbs including Mount Prospect, Palatine, Rolling Meadows, Buffalo Grove, and Wheeling from our Chicago base."),
            ("Can I rent a bounce house for a birthday party in Arlington Heights?",
             "Absolutely! Birthday parties are our specialty. Our rainbow combo castle is perfect for ages 3-14 and fits perfectly in most Arlington Heights backyards."),
            ("How do I book a bounce house rental for Arlington Heights?",
             "Book online in minutes at pureplayrentals.com/book — select your date, add a banner, enter your address, and pay. We'll confirm within 2 hours."),
        ]
    },
    {
        "slug": "bolingbrook",
        "name": "Bolingbrook",
        "county": "Will / DuPage County",
        "lat": "41.6983",
        "lon": "-88.0684",
        "zip": "60440",
        "desc": "Bounce house rental Bolingbrook IL. Pure Play Rentals delivers inflatable party rentals to Bolingbrook. Trusted by 500+ Chicagoland families. Book online.",
        "hero_sub": "From Bolingbrook's great backyards to Independence Grove events — Pure Play delivers, inflates, and sets up so you can enjoy every minute.",
        "faq": [
            ("What is the cost for bounce house rental in Bolingbrook?",
             "Pure Play Rentals charges $300 per day for bounce house rentals in Bolingbrook. Delivery, setup, and pickup are all included in this flat rate."),
            ("Do you serve Romeoville, Woodridge, and Lisle near Bolingbrook?",
             "Yes! We cover all of the I-55 corridor including Romeoville, Woodridge, Lisle, Downers Grove, and Lemont."),
            ("Is the bounce house safe for young kids in Bolingbrook?",
             "Our bounce houses are ASTM safety certified and cleaned with hospital-grade, child-safe sanitizers after every rental. We do a full safety inspection before every party."),
            ("How large is your biggest bounce house rental for Bolingbrook parties?",
             "Our rainbow combo castle is approximately 15x20 feet when inflated. Most standard Bolingbrook backyards can fit it comfortably — about 20x25 feet of open space needed."),
        ]
    },
    {
        "slug": "tinley-park",
        "name": "Tinley Park",
        "county": "Cook / Will County",
        "lat": "41.5731",
        "lon": "-87.7873",
        "zip": "60477",
        "desc": "Bounce house rental Tinley Park IL. Pure Play Rentals delivers premium inflatables to Tinley Park parties and events. $300/day, delivery included.",
        "hero_sub": "Tinley Park's trusted bounce house rental company. We bring the fun to your backyard, park, or event venue — fully set up and ready to bounce.",
        "faq": [
            ("How much does bounce house rental cost in Tinley Park?",
             "Pure Play Rentals rents bounce houses in Tinley Park for $300 per day. This flat rate covers delivery, setup, and takedown — nothing extra."),
            ("Do you serve Orland Park, Mokena, and Frankfort near Tinley Park?",
             "Yes! We serve the entire south and southwest suburbs including Orland Park, Mokena, Frankfort, Matteson, Oak Forest, and Midlothian."),
            ("Can you set up a bounce house at the Tinley Park Convention Center or pavilions?",
             "We can deliver to most outdoor event spaces in Tinley Park. Indoor venues require special arrangements. Contact us and we'll work with your venue."),
            ("Do you require a deposit to book a Tinley Park bounce house?",
             "We accept full payment at booking through our secure online system. We offer free weather reschedule if severe weather affects your party day."),
        ]
    },
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Bounce House Rental {name} IL | Pure Play Rentals | $300/Day Delivered</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="bounce house rental {name}, bounce house rental {name} IL, inflatable rental {name} Illinois, party rental {name}, jumpy house {name}, bounce house {name} Illinois, kids party rental {name}">
  <link rel="canonical" href="https://www.pureplayrentals.com/{slug}">
  <meta property="og:title" content="Bounce House Rental {name} IL | Pure Play Rentals">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="https://www.pureplayrentals.com/bounce-house-rental-chicago-illinois.png">
  <meta property="og:url" content="https://www.pureplayrentals.com/{slug}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Bounce House Rental {name} IL | Pure Play Rentals">
  <meta name="twitter:description" content="{desc}">
  <meta name="geo.region" content="US-IL">
  <meta name="geo.placename" content="{name}, Illinois">
  <meta name="geo.position" content="{lat};{lon}">
  <meta name="ICBM" content="{lat}, {lon}">
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;800;900&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />

  <!-- JSON-LD: LocalBusiness -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": ["LocalBusiness", "EntertainmentBusiness"],
    "@id": "https://www.pureplayrentals.com/#business",
    "name": "Pure Play Rentals",
    "description": "Premium bounce house and inflatable party rentals serving {name} IL and all of Chicagoland. We deliver, set up, and take down at your location.",
    "url": "https://www.pureplayrentals.com",
    "telephone": "+15551234567",
    "email": "hello@pureplayrentals.com",
    "image": "https://www.pureplayrentals.com/bounce-house-rental-chicago-illinois.png",
    "logo": "https://www.pureplayrentals.com/pureplay.png",
    "priceRange": "$$",
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "{name}",
      "addressRegion": "IL",
      "postalCode": "{zip}",
      "addressCountry": "US"
    }},
    "geo": {{
      "@type": "GeoCoordinates",
      "latitude": "{lat}",
      "longitude": "{lon}"
    }},
    "areaServed": [
      {{"@type": "City", "name": "{name}"}},
      {{"@type": "City", "name": "Chicago"}},
      {{"@type": "City", "name": "Naperville"}},
      {{"@type": "City", "name": "Aurora"}},
      {{"@type": "City", "name": "Joliet"}},
      {{"@type": "City", "name": "Schaumburg"}},
      {{"@type": "City", "name": "Bolingbrook"}},
      {{"@type": "City", "name": "Orland Park"}},
      {{"@type": "City", "name": "Arlington Heights"}},
      {{"@type": "City", "name": "Tinley Park"}}
    ],
    "openingHoursSpecification": [
      {{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
        "opens": "07:00",
        "closes": "20:00"
      }}
    ],
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "reviewCount": "127",
      "bestRating": "5"
    }},
    "offers": {{
      "@type": "Offer",
      "price": "300",
      "priceCurrency": "USD",
      "priceSpecification": {{"@type": "UnitPriceSpecification", "price": "300", "priceCurrency": "USD", "unitText": "DAY"}}
    }}
  }}
  </script>

  <!-- JSON-LD: FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{faq_json}]
  }}
  </script>

  <!-- JSON-LD: BreadcrumbList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.pureplayrentals.com/"}},
      {{"@type": "ListItem", "position": 2, "name": "Bounce House Rental {name}", "item": "https://www.pureplayrentals.com/{slug}"}}
    ]
  }}
  </script>

  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --navy: #0d1f3c;
      --navy-light: #162d54;
      --orange: #f7941d;
      --orange-dark: #d97a0f;
      --white: #ffffff;
      --light: #f9fafb;
      --gray: #f3f4f6;
      --text: #1a1a2e;
      --muted: #6b7280;
      --radius: 20px;
      --radius-lg: 28px;
      --shadow: 0 4px 24px rgba(13,31,60,0.10);
      --shadow-lg: 0 12px 48px rgba(13,31,60,0.18);
    }}
    html {{ scroll-behavior: smooth; }}
    body {{ font-family: 'Inter', sans-serif; color: var(--text); background: var(--white); overflow-x: hidden; }}
    h1, h2, h3, h4 {{ font-family: 'Nunito', sans-serif; font-weight: 900; line-height: 1.1; }}
    img {{ display: block; max-width: 100%; }}
    a {{ text-decoration: none; color: inherit; }}

    /* NAVBAR */
    .navbar {{
      position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
      padding: 0 5%; height: 72px;
      display: flex; align-items: center; justify-content: space-between;
      transition: background 0.3s, box-shadow 0.3s;
    }}
    .navbar.scrolled {{ background: var(--white); box-shadow: 0 2px 20px rgba(0,0,0,0.10); }}
    .navbar.scrolled .nav-link {{ color: var(--navy); text-shadow: none; }}
    .navbar.scrolled .hamburger span {{ background: var(--navy); }}
    .navbar.scrolled .nav-logo img {{ filter: none; }}
    .nav-logo img {{ height: 52px; width: auto; object-fit: contain; filter: drop-shadow(0 2px 8px rgba(0,0,0,0.35)); }}
    .nav-links {{ display: flex; align-items: center; gap: 36px; list-style: none; }}
    .nav-link {{ font-family: 'Nunito', sans-serif; font-weight: 800; font-size: 0.95rem; color: var(--white); letter-spacing: 0.3px; transition: color 0.2s; text-shadow: 0 1px 6px rgba(0,0,0,0.4); }}
    .nav-link:hover {{ color: var(--orange); }}
    .btn {{ display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 12px 28px; border-radius: 50px; font-family: 'Nunito', sans-serif; font-weight: 800; font-size: 0.95rem; cursor: pointer; transition: all 0.22s; border: none; letter-spacing: 0.2px; }}
    .btn-orange {{ background: var(--orange); color: var(--white); }}
    .btn-orange:hover {{ background: var(--orange-dark); transform: translateY(-2px); box-shadow: 0 6px 20px rgba(247,148,29,0.45); }}
    .btn-white-ghost {{ background: transparent; color: var(--white); border: 2.5px solid rgba(255,255,255,0.75); }}
    .btn-white-ghost:hover {{ background: rgba(255,255,255,0.12); border-color: var(--white); }}
    .btn-navy {{ background: var(--navy); color: var(--white); }}
    .btn-navy:hover {{ background: var(--navy-light); transform: translateY(-2px); box-shadow: 0 6px 20px rgba(13,31,60,0.35); }}
    .hamburger {{ display: none; flex-direction: column; gap: 5px; cursor: pointer; padding: 4px; background: none; border: none; }}
    .hamburger span {{ display: block; width: 26px; height: 2.5px; background: var(--white); border-radius: 2px; transition: all 0.3s; }}
    .mobile-menu {{ display: none; position: fixed; top: 72px; left: 0; right: 0; background: var(--white); padding: 24px 5% 32px; box-shadow: 0 8px 32px rgba(0,0,0,0.12); z-index: 999; flex-direction: column; gap: 4px; }}
    .mobile-menu.open {{ display: flex; }}
    .mobile-menu a {{ font-family: 'Nunito', sans-serif; font-weight: 800; font-size: 1.1rem; color: var(--navy); padding: 12px 0; border-bottom: 1px solid var(--gray); }}
    .mobile-menu .btn {{ margin-top: 16px; width: 100%; }}

    /* HERO */
    .hero {{ position: relative; width: 100%; height: 80vh; min-height: 560px; display: flex; align-items: center; justify-content: center; overflow: hidden; }}
    .hero-bg {{ position: absolute; inset: 0; background: var(--navy); }}
    .hero-bg img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center; }}
    .hero-overlay {{ position: absolute; inset: 0; background: linear-gradient(135deg, rgba(13,31,60,0.85) 0%, rgba(13,31,60,0.60) 60%, rgba(13,31,60,0.40) 100%); }}
    .hero-content {{ position: relative; z-index: 2; text-align: center; padding: 0 24px; max-width: 860px; }}
    .hero-eyebrow {{ display: inline-flex; align-items: center; gap: 8px; background: rgba(247,148,29,0.15); border: 1.5px solid rgba(247,148,29,0.55); color: var(--orange); font-family: 'Nunito', sans-serif; font-weight: 800; font-size: 0.8rem; letter-spacing: 1.5px; text-transform: uppercase; padding: 6px 16px; border-radius: 50px; margin-bottom: 24px; }}
    .hero-title {{ font-size: clamp(1.9rem, 3.8vw, 3rem); color: var(--white); margin-bottom: 24px; text-shadow: 0 2px 24px rgba(0,0,0,0.3); }}
    .hero-title .highlight {{ color: var(--orange); }}
    .hero-sub {{ font-size: clamp(1rem, 2.2vw, 1.2rem); color: rgba(255,255,255,0.88); font-weight: 400; line-height: 1.7; max-width: 560px; margin: 0 auto 40px; }}
    .hero-btns {{ display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }}
    .hero-btns .btn {{ font-size: 1.05rem; padding: 15px 36px; }}
    .hero-curve {{ position: absolute; bottom: -2px; left: 0; width: 100%; line-height: 0; z-index: 3; }}
    .hero-curve svg {{ display: block; width: 100%; height: auto; }}

    /* BREADCRUMB */
    .breadcrumb {{ background: var(--light); padding: 14px 5%; border-bottom: 1px solid var(--gray); }}
    .breadcrumb-inner {{ max-width: 1100px; margin: 0 auto; display: flex; align-items: center; gap: 8px; font-size: 0.83rem; color: var(--muted); }}
    .breadcrumb-inner a {{ color: var(--orange); font-weight: 600; }}
    .breadcrumb-inner a:hover {{ text-decoration: underline; }}

    /* SOCIAL PROOF */
    .social-proof {{ background: var(--white); padding: 32px 5%; }}
    .sp-inner {{ max-width: 1100px; margin: 0 auto; display: flex; align-items: center; justify-content: space-around; flex-wrap: wrap; gap: 24px; }}
    .sp-item {{ display: flex; align-items: center; gap: 14px; }}
    .sp-icon {{ width: 52px; height: 52px; border-radius: 50%; background: rgba(247,148,29,0.1); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
    .sp-text strong {{ display: block; font-family: 'Nunito', sans-serif; font-weight: 900; font-size: 1.2rem; color: var(--navy); line-height: 1.1; }}
    .sp-text span {{ font-size: 0.82rem; color: var(--muted); font-weight: 500; }}
    .sp-divider {{ width: 1px; height: 44px; background: var(--gray); }}

    /* SHARED */
    .section-label {{ font-family: 'Nunito', sans-serif; font-weight: 800; font-size: 0.78rem; letter-spacing: 2px; text-transform: uppercase; color: var(--orange); margin-bottom: 12px; }}
    .section-title {{ font-size: clamp(2rem, 4vw, 2.8rem); color: var(--navy); margin-bottom: 16px; }}
    .section-sub {{ font-size: 1.05rem; color: var(--muted); line-height: 1.7; max-width: 540px; }}

    /* PRODUCT */
    .product-section {{ background: var(--light); padding: 88px 5%; }}
    .product-inner {{ max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; }}
    .product-img {{ border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); }}
    .product-img img {{ width: 100%; height: 100%; object-fit: cover; }}
    .product-info .section-sub {{ max-width: 100%; margin-bottom: 28px; }}
    .feature-list {{ list-style: none; display: flex; flex-direction: column; gap: 12px; margin-bottom: 32px; }}
    .feature-list li {{ display: flex; align-items: center; gap: 10px; font-size: 0.95rem; color: var(--text); }}
    .feature-list li .check {{ width: 22px; height: 22px; border-radius: 50%; background: rgba(247,148,29,0.12); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
    .price-tag {{ display: inline-flex; align-items: baseline; gap: 4px; background: var(--navy); color: var(--white); padding: 12px 24px; border-radius: var(--radius); margin-bottom: 24px; }}
    .price-tag .amount {{ font-family: 'Nunito', sans-serif; font-weight: 900; font-size: 2.2rem; }}
    .price-tag .period {{ font-size: 0.9rem; opacity: 0.75; }}

    /* WHY SECTION */
    .why-section {{ background: var(--white); padding: 88px 5%; }}
    .why-inner {{ max-width: 1100px; margin: 0 auto; }}
    .why-header {{ text-align: center; margin-bottom: 56px; }}
    .why-header .section-sub {{ margin: 0 auto; }}
    .why-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 28px; }}
    .why-card {{ background: var(--light); border-radius: var(--radius); padding: 32px 28px; }}
    .why-icon {{ width: 52px; height: 52px; border-radius: 14px; background: rgba(247,148,29,0.12); display: flex; align-items: center; justify-content: center; margin-bottom: 18px; }}
    .why-card h3 {{ font-size: 1.1rem; color: var(--navy); margin-bottom: 10px; }}
    .why-card p {{ font-size: 0.9rem; color: var(--muted); line-height: 1.65; }}

    /* HOW IT WORKS */
    .how-section {{ background: var(--navy); padding: 88px 5%; }}
    .how-inner {{ max-width: 1100px; margin: 0 auto; text-align: center; }}
    .how-inner .section-label {{ color: var(--orange); }}
    .how-inner .section-title {{ color: var(--white); margin-bottom: 56px; }}
    .steps-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 32px; }}
    .step {{ position: relative; }}
    .step-num {{ width: 56px; height: 56px; border-radius: 50%; background: var(--orange); color: var(--white); font-family: 'Nunito', sans-serif; font-weight: 900; font-size: 1.4rem; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; }}
    .step h3 {{ font-size: 1rem; color: var(--white); margin-bottom: 10px; }}
    .step p {{ font-size: 0.88rem; color: rgba(255,255,255,0.65); line-height: 1.65; }}

    /* FAQ */
    .faq-section {{ background: var(--light); padding: 88px 5%; }}
    .faq-inner {{ max-width: 820px; margin: 0 auto; }}
    .faq-header {{ text-align: center; margin-bottom: 48px; }}
    .faq-header .section-sub {{ margin: 0 auto; }}
    .faq-list {{ display: flex; flex-direction: column; gap: 12px; }}
    .faq-item {{ background: var(--white); border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow); }}
    .faq-question {{ width: 100%; padding: 20px 24px; display: flex; align-items: center; justify-content: space-between; gap: 16px; cursor: pointer; text-align: left; font-family: 'Nunito', sans-serif; font-weight: 800; font-size: 1rem; color: var(--navy); transition: background 0.2s; background: none; border: none; }}
    .faq-question:hover {{ background: var(--light); }}
    .faq-item.open .faq-question {{ background: var(--light); color: var(--orange); }}
    .faq-chevron {{ flex-shrink: 0; transition: transform 0.3s; color: var(--muted); }}
    .faq-item.open .faq-chevron {{ transform: rotate(180deg); color: var(--orange); }}
    .faq-answer {{ max-height: 0; overflow: hidden; transition: max-height 0.35s ease, padding 0.2s; padding: 0 24px; font-size: 0.95rem; color: var(--muted); line-height: 1.75; }}
    .faq-item.open .faq-answer {{ max-height: 300px; padding: 0 24px 22px; }}

    /* CTA BAND */
    .cta-band {{ background: linear-gradient(135deg, var(--orange) 0%, #f97316 100%); padding: 72px 5%; text-align: center; }}
    .cta-band h2 {{ font-size: clamp(1.8rem, 3.5vw, 2.6rem); color: var(--white); margin-bottom: 16px; }}
    .cta-band p {{ font-size: 1.05rem; color: rgba(255,255,255,0.9); margin-bottom: 32px; }}
    .cta-band .btn-white {{ background: var(--white); color: var(--orange); font-weight: 800; padding: 16px 40px; font-size: 1.1rem; border-radius: 50px; }}
    .cta-band .btn-white:hover {{ transform: translateY(-2px); box-shadow: 0 8px 28px rgba(0,0,0,0.2); }}

    /* FOOTER */
    .footer {{ background: var(--navy); color: rgba(255,255,255,0.75); padding: 64px 5% 32px; }}
    .footer-grid {{ max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 2fr 1fr 1fr 1.4fr; gap: 48px; margin-bottom: 48px; }}
    .footer-logo img {{ height: 56px; width: auto; margin-bottom: 16px; }}
    .footer-tagline {{ font-size: 0.9rem; line-height: 1.7; margin-bottom: 24px; }}
    .footer-social {{ display: flex; gap: 10px; }}
    .social-btn {{ width: 38px; height: 38px; border-radius: 50%; background: rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: center; font-size: 0.85rem; font-family: 'Nunito', sans-serif; font-weight: 800; color: var(--white); transition: background 0.2s; cursor: pointer; border: none; }}
    .social-btn:hover {{ background: var(--orange); }}
    .footer-col h4 {{ font-family: 'Nunito', sans-serif; font-weight: 800; font-size: 0.95rem; color: var(--white); margin-bottom: 20px; }}
    .footer-links {{ list-style: none; display: flex; flex-direction: column; gap: 10px; }}
    .footer-links a {{ font-size: 0.88rem; color: rgba(255,255,255,0.65); transition: color 0.2s; }}
    .footer-links a:hover {{ color: var(--orange); }}
    .footer-contact-item {{ display: flex; align-items: flex-start; gap: 10px; margin-bottom: 14px; font-size: 0.88rem; }}
    .footer-contact-item .ico {{ flex-shrink: 0; margin-top: 1px; color: var(--orange); }}
    .footer-bottom {{ max-width: 1100px; margin: 0 auto; padding-top: 28px; border-top: 1px solid rgba(255,255,255,0.08); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; font-size: 0.82rem; }}

    /* RESPONSIVE */
    @media (max-width: 900px) {{
      .product-inner {{ grid-template-columns: 1fr; }}
      .footer-grid {{ grid-template-columns: 1fr 1fr; }}
      .nav-links {{ display: none; }}
      .hamburger {{ display: flex; }}
    }}
    @media (max-width: 600px) {{
      .footer-grid {{ grid-template-columns: 1fr; gap: 32px; }}
      .footer-bottom {{ flex-direction: column; text-align: center; }}
      .sp-divider {{ display: none; }}
    }}
  </style>
</head>
<body>

  <nav class="navbar" id="navbar">
    <a href="../" class="nav-logo">
      <img src="../pureplay.png" alt="Pure Play Rentals - Chicago Bounce House Rental" />
    </a>
    <ul class="nav-links">
      <li><a href="../" class="nav-link">Home</a></li>
      <li><a href="../shop" class="nav-link">Shop</a></li>
      <li><a href="../book" class="nav-link">Book</a></li>
      <li><a href="#contact" class="nav-link">Contact</a></li>
      <li><a href="../book" class="btn btn-orange" style="padding:10px 22px;font-size:0.9rem;">Book Now</a></li>
    </ul>
    <button class="hamburger" id="hamburger" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
  </nav>

  <div class="mobile-menu" id="mobileMenu">
    <a href="../">Home</a>
    <a href="../shop">Shop</a>
    <a href="../book">Book</a>
    <a href="#contact">Contact</a>
    <a href="../book" class="btn btn-orange">Book Now</a>
  </div>

  <!-- HERO -->
  <section class="hero">
    <div class="hero-bg">
      <img src="../bounce-house-rental-backyard-chicagoland.png" alt="Bounce house rental {name} Illinois" loading="eager" />
    </div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <div class="hero-eyebrow">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
        {name}'s Favorite Bounce House Rental
      </div>
      <h1 class="hero-title">Bounce House Rental<br><span class="highlight">{name}, IL</span></h1>
      <p class="hero-sub">{hero_sub}</p>
      <div class="hero-btns">
        <a href="../book" class="btn btn-orange">Book Now — $300/Day</a>
        <a href="../shop" class="btn btn-white-ghost">See the Bounce House</a>
      </div>
    </div>
    <div class="hero-curve">
      <svg viewBox="0 0 1440 72" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M0,72 L0,40 Q360,0 720,36 Q1080,72 1440,20 L1440,72 Z" fill="#ffffff"/>
      </svg>
    </div>
  </section>

  <!-- BREADCRUMB -->
  <div class="breadcrumb">
    <div class="breadcrumb-inner">
      <a href="../">Pure Play Rentals</a>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><polyline points="9 18 15 12 9 6"/></svg>
      <span>Bounce House Rental {name}</span>
    </div>
  </div>

  <!-- SOCIAL PROOF -->
  <section class="social-proof">
    <div class="sp-inner">
      <div class="sp-item">
        <div class="sp-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--orange)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
        </div>
        <div class="sp-text">
          <strong>Serving {name}</strong>
          <span>and all of Chicagoland</span>
        </div>
      </div>
      <div class="sp-divider"></div>
      <div class="sp-item">
        <div class="sp-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--orange)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
        </div>
        <div class="sp-text">
          <strong>500+ Parties Served</strong>
          <span>Across Chicagoland</span>
        </div>
      </div>
      <div class="sp-divider"></div>
      <div class="sp-item">
        <div class="sp-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="var(--orange)" stroke="var(--orange)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
        </div>
        <div class="sp-text">
          <strong>4.9 Star Rating</strong>
          <span>127 reviews</span>
        </div>
      </div>
      <div class="sp-divider"></div>
      <div class="sp-item">
        <div class="sp-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--orange)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <div class="sp-text">
          <strong>Fully Insured</strong>
          <span>ASTM safety certified</span>
        </div>
      </div>
    </div>
  </section>

  <!-- PRODUCT SECTION -->
  <section class="product-section">
    <div class="product-inner">
      <div class="product-img">
        <img src="../bounce-house-rental-chicago-illinois.png" alt="Rainbow combo bounce house rental {name} Illinois" loading="lazy" />
      </div>
      <div class="product-info">
        <p class="section-label">Featured Rental</p>
        <h2 class="section-title">Rainbow Combo Castle with Slide</h2>
        <div class="price-tag">
          <span class="amount">$300</span>
          <span class="period">/ day</span>
        </div>
        <p class="section-sub" style="margin-bottom:28px;">Our most popular rental — a massive rainbow bounce castle with a built-in slide. Perfect for backyard birthday parties, school events, and church festivals in {name}.</p>
        <ul class="feature-list">
          <li>
            <span class="check">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="var(--orange)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
            </span>
            Delivered to {name} — free setup and takedown
          </li>
          <li>
            <span class="check">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="var(--orange)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
            </span>
            Sanitized with hospital-grade, child-safe cleaners
          </li>
          <li>
            <span class="check">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="var(--orange)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
            </span>
            Full-day rental — up to 8 hours of bounce time
          </li>
          <li>
            <span class="check">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="var(--orange)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
            </span>
            Custom banner add-on available for birthday names
          </li>
          <li>
            <span class="check">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="var(--orange)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>
            </span>
            Free weather reschedule — no stress, no fees
          </li>
        </ul>
        <a href="../book" class="btn btn-orange" style="font-size:1.05rem;padding:15px 36px;">Book for {name}</a>
      </div>
    </div>
  </section>

  <!-- WHY SECTION -->
  <section class="why-section">
    <div class="why-inner">
      <div class="why-header">
        <p class="section-label">Why Choose Us</p>
        <h2 class="section-title">The Best Bounce House Rental in {name}</h2>
        <p class="section-sub">We're not just another rental company. Pure Play is built for {name} families who want reliable, clean, and hassle-free party rentals.</p>
      </div>
      <div class="why-grid">
        <div class="why-card">
          <div class="why-icon">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="var(--orange)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
          </div>
          <h3>We Deliver to {name}</h3>
          <p>We know {name} streets, parks, and neighborhoods. Reliable, on-time delivery every single booking.</p>
        </div>
        <div class="why-card">
          <div class="why-icon">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="var(--orange)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <h3>Safety First</h3>
          <p>ASTM certified equipment, hospital-grade sanitation, and a full safety inspection before every rental.</p>
        </div>
        <div class="why-card">
          <div class="why-icon">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="var(--orange)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          </div>
          <h3>We Arrive Early</h3>
          <p>Our team shows up 60 minutes before party time so everything is inflated, tested, and ready when guests arrive.</p>
        </div>
        <div class="why-card">
          <div class="why-icon">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="var(--orange)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <h3>Simple Flat Pricing</h3>
          <p>$300 per day, period. Delivery, setup, and takedown included. No hidden fees, no fuel surcharges.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- HOW IT WORKS -->
  <section class="how-section">
    <div class="how-inner">
      <p class="section-label">How It Works</p>
      <h2 class="section-title">Book Your {name} Bounce House in Minutes</h2>
      <div class="steps-grid">
        <div class="step">
          <div class="step-num">1</div>
          <h3>Pick Your Date</h3>
          <p>Choose your party date on our live calendar. See real-time availability for {name}.</p>
        </div>
        <div class="step">
          <div class="step-num">2</div>
          <h3>Add a Banner</h3>
          <p>Personalize the bounce house with a custom birthday or event banner.</p>
        </div>
        <div class="step">
          <div class="step-num">3</div>
          <h3>Confirm and Pay</h3>
          <p>Secure online booking. Pay in full today, and we'll confirm your {name} delivery within 2 hours.</p>
        </div>
        <div class="step">
          <div class="step-num">4</div>
          <h3>We Handle Everything</h3>
          <p>We arrive early, inflate, and set up. After the party, we take it all down. You just enjoy.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="faq-section" id="faq">
    <div class="faq-inner">
      <div class="faq-header">
        <p class="section-label">FAQ</p>
        <h2 class="section-title">Common Questions About {name} Bounce House Rentals</h2>
        <p class="section-sub">Everything {name} families ask before booking their first bounce house.</p>
      </div>
      <div class="faq-list">
{faq_html}
      </div>
    </div>
  </section>

  <!-- CTA BAND -->
  <section class="cta-band">
    <h2>Ready to Book Your {name} Bounce House?</h2>
    <p>Join 500+ Chicagoland families who chose Pure Play. Delivered, set up, and sanitized — $300 flat.</p>
    <a href="../book" class="btn-white btn">Book Now — Check {name} Availability</a>
  </section>

  <!-- FOOTER -->
  <footer class="footer" id="contact">
    <div class="footer-grid">
      <div>
        <div class="footer-logo">
          <img src="../pureplay.png" alt="Pure Play Rentals Chicago" />
        </div>
        <p class="footer-tagline">Bringing the bounce to backyards, parks, and events across Chicago and all Chicagoland suburbs. Safe, clean, and certified inflatables for every occasion.</p>
        <div class="footer-social">
          <a href="https://www.facebook.com/pureplayrentals" class="social-btn" aria-label="Facebook">f</a>
          <a href="https://www.instagram.com/pureplayrentals" class="social-btn" aria-label="Instagram">ig</a>
          <button class="social-btn" aria-label="TikTok">tk</button>
        </div>
      </div>
      <div class="footer-col">
        <h4>Navigate</h4>
        <ul class="footer-links">
          <li><a href="../">Home</a></li>
          <li><a href="../shop">Shop</a></li>
          <li><a href="../book">Book Now</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Service Areas</h4>
        <ul class="footer-links">
          <li><a href="../naperville">Naperville</a></li>
          <li><a href="../schaumburg">Schaumburg</a></li>
          <li><a href="../aurora">Aurora</a></li>
          <li><a href="../joliet">Joliet</a></li>
          <li><a href="../orland-park">Orland Park</a></li>
          <li><a href="../arlington-heights">Arlington Heights</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Contact Us</h4>
        <div class="footer-contact-item">
          <span class="ico">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.61 3.18 2 2 0 0 1 3.6 1h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.64a16 16 0 0 0 5.55 5.55l.95-.95a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 21 16.92z"/></svg>
          </span>
          <span><a href="tel:+15551234567" style="color:inherit;">(555) 123-4567</a></span>
        </div>
        <div class="footer-contact-item">
          <span class="ico">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          </span>
          <span><a href="mailto:hello@pureplayrentals.com" style="color:inherit;">hello@pureplayrentals.com</a></span>
        </div>
        <div class="footer-contact-item">
          <span class="ico">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          </span>
          <span>Mon to Sun: 7am to 8pm</span>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&#169; 2025 Pure Play Rentals. All rights reserved.</span>
      <span>Privacy Policy · Terms of Service</span>
    </div>
  </footer>

  <script>
    // Navbar scroll
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {{
      navbar.classList.toggle('scrolled', window.scrollY > 60);
    }});
    // Hamburger
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobileMenu');
    hamburger.addEventListener('click', () => mobileMenu.classList.toggle('open'));
    mobileMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => mobileMenu.classList.remove('open')));
    // FAQ accordion
    document.querySelectorAll('.faq-question').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const item = btn.closest('.faq-item');
        const wasOpen = item.classList.contains('open');
        document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
        if (!wasOpen) item.classList.add('open');
      }});
    }});
  </script>
</body>
</html>"""

def build_faq_json(faqs):
    items = []
    for q, a in faqs:
        items.append(
            f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        )
    return ",\n      ".join(items)

def build_faq_html(faqs):
    html = []
    for q, a in faqs:
        chevron = '<svg class="faq-chevron" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>'
        html.append(f"""        <div class="faq-item">
          <button class="faq-question">{q}{chevron}</button>
          <div class="faq-answer">{a}</div>
        </div>""")
    return "\n".join(html)

for city in cities:
    faq_json = build_faq_json(city["faq"])
    faq_html = build_faq_html(city["faq"])

    content = TEMPLATE.format(
        slug=city["slug"],
        name=city["name"],
        county=city["county"],
        lat=city["lat"],
        lon=city["lon"],
        zip=city["zip"],
        desc=city["desc"],
        hero_sub=city["hero_sub"],
        faq_json=faq_json,
        faq_html=faq_html,
    )

    path = f"/Users/a/Downloads/pureplay-rentals/{city['slug']}/index.html"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"Created: {path}")

print("Done — all city pages generated.")
