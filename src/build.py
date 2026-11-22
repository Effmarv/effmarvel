"""Builds the case study pages into public/<slug>/index.html. Run: python3 src/build.py"""
import pathlib, html
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "public"

HEAD = """<!doctype html>
<html lang="en-GB"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Marvelous Effiong</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title} case study · Marvelous Effiong">
<meta property="og:description" content="{desc}">
<meta name="theme-color" content="#faf8f4">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,600;0,9..144,700;1,9..144,600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
</head><body>
<nav class="nav"><div class="wrap">
  <a class="logo" href="/">effmarvel<span>.</span></a>
  <ul><li><a href="/#work">Work</a></li><li><a href="/#how">How I build</a></li><li><a class="btn" href="/#contact" style="padding:9px 16px;color:#fff">Say hello</a></li></ul>
</div></nav>
"""
FOOT = """<footer><div class="wrap"><span>© 2026 Marvelous Effiong</span>
<span><a href="https://rezzo.co.uk">Rezzo</a> · <a href="https://lastprice.ng">LastPrice.ng</a> · <a href="https://lionsvogue.com">Lions Vogue</a></span></div></footer>
<script src="/site.js" defer></script></body></html>
"""

def page(p):
    facts = "".join(f"<div><small>{k}</small><b>{v}</b></div>" for k, v in p["facts"])
    gallery = "".join(f'<figure><div class="phone full">{img}</div><figcaption>{cap}</figcaption></figure>' for img, cap in p["gallery"])
    toc = "".join(f'<a href="#{s[0]}">{s[1]}</a>' for s in p["sections"])
    body = "".join(f'<div class="block reveal" id="{s[0]}"><h2>{s[1]}</h2>{s[2]}</div>' for s in p["sections"])
    return HEAD.format(title=p["title"], desc=html.escape(p["desc"])) + f"""
<header class="cs-hero"><div class="wrap">
  <a class="back" href="/#work">← All work</a>
  <div class="eyebrow">{p["eyebrow"]}</div>
  <h1>{p["h1"]}</h1>
  <p class="lead">{p["lead"]}</p>
  <div style="margin-top:24px"><a class="btn" href="{p["url"]}">Visit {p["title"]} ↗</a></div>
  <div class="facts">{facts}</div>
</div></header>
<div class="wrap"><div class="gallery">{gallery}</div></div>
<div class="wrap cs-body"><aside>{toc}</aside><div>{body}</div></div>
<div class="wrap next"><a href="/#work">← All work</a><a href="{p["next"][0]}">Next: {p["next"][1]} →</a></div>
""" + FOOT

def img(name, alt):
    return f'<img src="/img/{name}.webp" alt="{alt}" loading="lazy">'

def d(title, why):
    return f'<div class="decision"><b>{title}</b><span>{why}</span></div>'

PAGES = {}

PAGES["rezzo"] = dict(
  title="Rezzo", url="https://rezzo.co.uk",
  desc="Case study: Rezzo, a mobile-first booking page and shop link for UK salons and barbers, £9 a month with no commission.",
  eyebrow="Case study · UK · 2026",
  h1="Rezzo: bookings for your business, in your pocket",
  lead="A booking page, deposits, reminders, a shop and a diary for UK salons, barbers, nail techs and lash artists. One link in their Instagram bio, a flat £9 a month, and no commission on any booking.",
  facts=[("Role","Founder, product &amp; build"),("Market","UK small service businesses"),("Platforms","Web, Android, iOS"),("Price","£9 / month, no commission")],
  gallery=[(img("rezzo-booking","Booking page"),"The booking page clients see"),
           (img("rezzo-services","Service menu with categories"),"Services grouped by category"),
           (img("rezzo-checkout","Checkout with discount code"),"Pick a time, apply a code"),
           (img("rezzo-info","Opening hours and info"),"Work photos, hours, policies"),
           (img("rezzo-welcome","Vendor app welcome screen"),"The business owner's app"),
           (img("rezzo-lock","App lock screen"),"Fingerprint and face lock")],
  sections=[
    ("problem","The problem","""<p>Most small UK beauty businesses run their bookings through Instagram DMs and WhatsApp. That means hours of back-and-forth about prices and times, double bookings, and no-shows that wipe out a day's earnings.</p>
<p>The existing tools were built for bigger salons. They charge per staff member, take a cut of each booking, or push clients into downloading an app and making an account. For a braider working alone, that's too much cost and too much friction for her clients.</p>"""),
    ("decisions","Key decisions","""
"""+d("A flat price with no commission","£9 a month for a solo operator, £15 for a team regardless of size. Businesses keep every pound of every booking, which is easy to explain and hard for marketplace-style competitors to match.")+
d("No accounts for clients","Clients book from one link with just a name and mobile number. Every extra step loses bookings, so there's no app and no sign-up on the client side.")+
d("Instant booking on by default","Busy owners can't approve requests in the middle of an appointment, so new businesses accept bookings instantly. They can still switch to approval if they want.")+
d("Deposits paid straight to the business","Payments go through Stripe Connect into the owner's own bank account, so deposits cut no-shows without Rezzo ever holding their money.")+
d("Mobile first, everywhere","The owners run their business from their phone, and so do their clients. Every screen is designed at phone width first.")),
    ("built","What I built","""<ul>
<li><b>A booking page per business</b> with services, categories, styles, team, work photos, opening hours, policies, Google reviews and a month calendar.</li>
<li><b>Payments:</b> deposits or full price, discount codes, and yearly plans with Bacs Direct Debit, all on Stripe.</li>
<li><b>Owner app</b> for Android and iOS: diary, clients, staff rota, breaks, push notifications and a fingerprint or face lock.</li>
<li><b>Keeping clients:</b> email and WhatsApp confirmations, reminders, a loyalty card, review requests and a "book again" home screen shortcut.</li>
<li><b>A shop</b> so businesses can sell products alongside services.</li>
<li><b>AI where it saves time:</b> it writes the business bio, drafts support replies and writes news updates.</li>
<li><b>Support and admin:</b> an in-app help chat, a team inbox, and account deletion that meets app store rules.</li>
</ul>"""),
    ("results","Results so far","""<p>Rezzo is live at <a href="https://rezzo.co.uk">rezzo.co.uk</a>, with Android and iOS apps in progress for the stores. From the first line of code to a working product with payments, apps and emails took about four days and 95 shipped changes.</p>
<div class="note">Launch is underway now. I'll add real numbers here (businesses, bookings, no-shows saved) as they come in.</div>"""),
    ("learned","What I learned","""<p>The decisions mattered more than the features. Choosing a flat price, no client accounts and instant booking shaped everything else, and they all came from picturing one person: a braider with her hands full.</p>"""),
  ],
  next=("/lastprice/","LastPrice.ng"))

PAGES["lastprice"] = dict(
  title="LastPrice.ng", url="https://lastprice.ng",
  desc="Case study: LastPrice.ng, a free shop link for Nigerian small sellers where orders land in WhatsApp.",
  eyebrow="Case study · Nigeria",
  h1="LastPrice.ng: your shop and bookings in one link",
  lead="A free shop link for Nigerian small sellers. Customers see prices, pick what they want, and the order lands in the seller's WhatsApp. No website and no app to download.",
  facts=[("Role","Founder, product &amp; build"),("Market","Nigerian small sellers"),("Built for","Everyday Android, slow data"),("Price","Free, Pro ₦2,500 / month")],
  gallery=[],
  sections=[
    ("problem","The problem","""<p>In Nigeria, a huge amount of small business happens on WhatsApp and Instagram. Sellers of fashion, cakes, skincare, phones and hair services answer the same question all day: <i>"How much? What's your last price?"</i></p>
<p>Building a website is expensive and slow, and most customers won't download another app or wait for a heavy page to load on mobile data.</p>"""),
    ("decisions","Key decisions","""
"""+d("Free forever, not a free trial","Up to 10 items free with no end date, so any seller can start today. Pro (₦2,500 a month) unlocks unlimited items, more photos, a customer list and full stats.")+
d("WhatsApp is the checkout","Orders arrive in the seller's WhatsApp, where they already talk to customers. Payment is agreed in the chat by transfer or cash, so there's nothing new to learn.")+
d("Light enough for slow data","Built for everyday Android phones on patchy connections, because that's what most customers actually use.")+
d("A founding offer to start momentum","The first 100 shops keep 20 free items forever, which rewards early sellers for taking a chance on it.")),
    ("built","What I built","""<ul>
<li><b>A shop link and QR poster</b> for each seller, ready to share on WhatsApp status, Instagram or a market stall.</li>
<li><b>Items and services in one place</b>, so a salon or barber can take booking requests as easily as a boutique takes orders.</li>
<li><b>Orders straight to WhatsApp</b>, with an order number and a total, so nothing gets lost in the chat.</li>
<li><b>Seller tools on Pro:</b> customer list, order history, best sellers, promo prices and their own colours.</li>
<li><b>Weekly stats</b> so sellers can see what's working.</li>
</ul>"""),
    ("results","Results so far","""<p>LastPrice.ng is live at <a href="https://lastprice.ng">lastprice.ng</a>, open to sellers across Nigeria.</p>
<div class="note">Numbers to add: shops created, orders sent and founding spots taken.</div>"""),
    ("learned","What I learned","""<p>LastPrice taught me to build around the tools people already trust. Sellers didn't need a new place to talk to customers; they needed their prices in front of them before the chat even started.</p>"""),
  ],
  next=("/lionsvogue/","Lions Vogue"))

PAGES["lionsvogue"] = dict(
  title="Lions Vogue", url="https://lionsvogue.com",
  desc="Case study: Lions Vogue, an event ticketing platform for Nigerian nightlife with instant QR tickets and door check-in.",
  eyebrow="Case study · Nigeria",
  h1="Lions Vogue: discover the party, skip the queue",
  lead="An event ticketing platform and party marketplace for Nigerian nightlife. Party-goers find trending events and get QR tickets instantly. Organisers launch events fast, sell securely, scan at the door and get paid.",
  facts=[("Role","Founder, product &amp; build"),("Market","Nigerian nightlife"),("Cities","Lagos, Abuja, Port Harcourt, Uyo"),("Model","Marketplace for organisers")],
  gallery=[],
  sections=[
    ("problem","The problem","""<p>Nigeria's party scene moves fast, but tickets are often sold through DMs, bank transfers and paper lists. Buyers worry about fake tickets, organisers chase payments, and the door turns into a bottleneck.</p>"""),
    ("decisions","Key decisions","""
"""+d("Approved organisers only","Merchants apply and get approved before they can sell, which keeps fake events off the platform and builds trust with buyers.")+
d("QR tickets, delivered instantly","Every ticket arrives straight away with a QR code, so buyers have proof and the door can scan and validate in seconds.")+
d("Organisers stay in control","Each merchant manages their own inventory, pricing and refunds, and can see their payouts.")+
d("Discovery by city","Events are filtered by state and party type, with a live \"Nightlife Pulse\" showing where demand is building.")),
    ("built","What I built","""<ul>
<li><b>An event marketplace</b> with trending events across Lagos, Abuja, Port Harcourt, Uyo and beyond.</li>
<li><b>Instant QR tickets</b> and shareable links for every purchase.</li>
<li><b>A merchant dashboard</b> for inventory, pricing, refunds and payout visibility.</li>
<li><b>Door check-in:</b> scan and validate tickets at the entrance.</li>
<li><b>Branded sales links</b> for each event, so organisers can sell from their own socials.</li>
<li><b>Nightlife Pulse:</b> a live demand heatmap across cities.</li>
</ul>"""),
    ("results","Results so far","""<p>Lions Vogue is live at <a href="https://lionsvogue.com">lionsvogue.com</a> and registered with the Corporate Affairs Commission.</p>
<div class="note">Numbers to add: events listed, tickets sold and organisers on board.</div>"""),
    ("learned","What I learned","""<p>In a marketplace, trust is the product. Approving organisers and giving every buyer a scannable ticket did more for sales than any feature on the page.</p>"""),
  ],
  next=("/rezzo/","Rezzo"))

LP_MOCK = '''<div class="mock">{body}</div>'''
MOCKS = {
 "lastprice": [
  ('<div class="mock"><div style="display:flex;gap:8px;align-items:center"><div style="width:30px;height:30px;border-radius:9px;background:#0d7a4a;color:#fff;display:grid;place-items:center;font-weight:800">T</div><div><b>Tolu\'s Closet</b><br><span style="color:#777">Ankara &amp; Aso-oke</span></div></div><div class="m-item"><span>Ankara two-piece</span><b>₦12,000</b></div><div class="m-item"><span>Aso-oke gele</span><b>₦6,500</b></div><div class="m-item"><span>Delivery, Lagos</span><b>₦2,000</b></div><div style="display:flex;justify-content:space-between;padding:4px 2px"><span>Order #K7Q2</span><b>₦20,500</b></div><div class="m-btn" style="background:#25a35a">Send order on WhatsApp</div></div>',"A seller's shop link"),
  ('<div class="mock"><div class="m-title" style="color:#0d7a4a">Your shop and bookings in one link</div><p style="margin:0;color:#555">Customers see your prices, pick what they want, and the order lands in your WhatsApp.</p><div class="m-btn" style="background:#0d7a4a">Create my free shop</div><div class="m-item"><span>1. Add items or services</span></div><div class="m-item"><span>2. Share your link or QR</span></div><div class="m-item"><span>3. Get orders on WhatsApp</span></div></div>',"Sign up in three steps"),
 ],
 "lionsvogue": [
  ('<div class="mock dark"><div class="m-title">Discover trending parties in Nigeria</div><div><span class="m-pill" style="background:#1b2033">All party types</span> <span class="m-pill" style="background:#1b2033">All states</span></div><div class="m-item"><span><b>Lagos</b><br><span style="color:#9aa">Trending this weekend</span></span><b style="color:#f5c84c">→</b></div><div class="m-item"><span><b>Abuja</b><br><span style="color:#9aa">Trending this weekend</span></span><b style="color:#f5c84c">→</b></div><div class="m-btn" style="background:#f5c84c;color:#080b12">Explore events</div></div>',"Discover events by city"),
  ('<div class="mock dark"><div class="m-title">Your ticket</div><div style="background:#fff;border-radius:12px;padding:14px;display:grid;place-items:center"><svg viewBox="0 0 21 21" width="110" height="110" shape-rendering="crispEdges"><path fill="#080b12" d="M0 0h7v7H0zM14 0h7v7h-7zM0 14h7v7H0z"/><path fill="#fff" d="M1 1h5v5H1zM15 1h5v5h-5zM1 15h5v5H1z"/><path fill="#080b12" d="M2 2h3v3H2zM16 2h3v3h-3zM2 16h3v3H2zM9 1h2v2H9zM8 4h3v2H8zM9 8h4v2H9zM14 9h3v2h-3zM8 12h2v3H8zM12 13h3v2h-3zM16 15h3v3h-3zM10 17h4v2h-4zM18 11h2v2h-2z"/></svg></div><div class="m-btn" style="background:#22c55e">Scan at the door</div></div>',"Instant QR ticket"),
 ],
}

for slug, p in PAGES.items():
    if slug in MOCKS:
        p["gallery"] = MOCKS[slug]
    (OUT / slug).mkdir(parents=True, exist_ok=True)
    (OUT / slug / "index.html").write_text(page(p))
    print("built", slug)
