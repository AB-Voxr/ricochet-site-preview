import json
import os

CDN = "https://cdn.shopify.com/s/files/1/0801/6933/7062/files/"

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title} | Ricochet Supplements</title>
<meta name="description" content="{desc}">
<link rel="icon" href="https://ricochetsupplements.com/cdn/shop/files/Draft_Final.png?height=64&v=1776456821">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow:wght@400;500;600;700&family=Barlow+Condensed:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<div class="announce">Every order helps fund care packages for deployed service members</div>
<header>
  <div class="wrap nav">
    <a href="/"><img src="https://ricochetsupplements.com/cdn/shop/files/Draft_Final.png?height=100&v=1776456821" alt="Ricochet Supplements"></a>
    <nav>
      <a href="/shop" class="hideM on">Shop</a>
      <a href="/inside" class="hideM">What's Inside</a>
      <a href="/mission" class="hideM">Our Mission</a>
      <a href="/#faq" class="hideM">FAQ</a>
      <a class="btn" href="/shop">Shop Now</a>
    </nav>
  </div>
</header>
"""

FOOT = """
<footer>
  <div class="wrap">
    <div class="fGrid">
      <div>
        <img src="https://ricochetsupplements.com/cdn/shop/files/Draft_Final.png?height=100&v=1776456821" alt="Ricochet Supplements">
        <p>Veteran-owned tactical fitness nutrition. Built in the Rio Grande Valley, Texas. Redirect your health.</p>
      </div>
      <div><h4>Shop</h4><ul>
        <li><a href="/shop">All Collections</a></li>
        <li><a href="/products/ballistic-pre-workout">Ballistic Pre-Workout</a></li>
        <li><a href="/products/creatine-monohydrate">Creatine Monohydrate</a></li>
        <li><a href="/products/afterburn-mach-i">Afterburn Mach-I</a></li>
        <li><a href="/products/tango-protocol-testosterone-booster">Tango Protocol</a></li>
      </ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="/mission">Our Mission</a></li>
        <li><a href="/inside">What's Inside</a></li>
        <li><a href="https://www.instagram.com/ricochetsupplements/">Instagram</a></li>
        <li><a href="https://www.facebook.com/ricochetsupplements">Facebook</a></li>
        <li><a href="https://www.tiktok.com/@ricochetsupplements">TikTok</a></li>
      </ul></div>
      <div><h4>Support</h4><ul>
        <li><a href="/policies/shipping-policy">Shipping Policy</a></li>
        <li><a href="/policies/refund-policy">Refund Policy</a></li>
        <li><a href="/policies/subscription-policy">Subscriptions</a></li>
        <li><a href="/policies/privacy-policy">Privacy</a></li>
        <li><a href="/policies/terms-of-service">Terms</a></li>
      </ul></div>
    </div>
    <div class="legal">
      <span>These statements have not been evaluated by the Food and Drug Administration. These products are not intended to diagnose, treat, cure, or prevent any disease.</span>
      <span>&copy; 2026 Ricochet Supplements. Redesign preview by AJ Marketing.</span>
    </div>
  </div>
</footer>
<script>
const io = new IntersectionObserver(es => es.forEach(e => {{if (e.isIntersecting) {{e.target.classList.add('in'); io.unobserve(e.target)}}}}), {{threshold: .12}});
document.querySelectorAll('.rv').forEach(el => {{el.style.transitionDelay = (el.dataset.d || 0) + 'ms'; io.observe(el)}});
const mainImg = document.getElementById('mainImg');
document.querySelectorAll('.thumbs button').forEach(b => b.addEventListener('click', () => {{
  document.querySelectorAll('.thumbs button').forEach(x => x.classList.remove('on'));
  b.classList.add('on');
  mainImg.src = b.dataset.img;
}}));
const cartBtn = document.getElementById('cartBtn');
document.querySelectorAll('.flavorPills .pill[data-variant]').forEach(p => p.addEventListener('click', () => {{
  document.querySelectorAll('.flavorPills .pill').forEach(x => x.classList.remove('on'));
  p.classList.add('on');
  if (cartBtn) cartBtn.href = 'https://ricochetsupplements.com/cart/' + p.dataset.variant + ':1';
  if (p.dataset.img) mainImg.src = p.dataset.img;
}}));
</script>
</body>
</html>
"""

PDP = """
<section>
  <div class="wrap pdp" style="padding-top:60px;padding-bottom:80px">
    <div class="gal rv">
      <div class="main pdpImg" style="position:static;padding:0;border:none"><div class="main" style="margin:0"><img id="mainImg" src="{mainimg}" alt="{title}"></div>
      <div class="thumbs">
{thumbs}
      </div></div>
    </div>
    <div class="pdpInfo">
      <span class="flag">{flag}</span>
      <h1>{title}</h1>
      <div class="price">{price}</div>
      <div class="revBand"><svg viewBox="0 0 24 24"><path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg><div><b>{revhead}</b><br><span>{revsub}</span></div></div>
      <p class="lede">{lede}</p>
      <ul class="points">
{points}
      </ul>
{flavors}
      <div class="buyRow">
        {buybtn}
        <span class="buyNote">{buynote}</span>
      </div>
      <div class="pdpTicks"><span>Veteran Owned</span><span>Made in the U.S.</span><span>No Proprietary Blends</span></div>
    </div>
  </div>
</section>

<section class="shopBand">
  <div class="wrap" style="padding-top:80px;padding-bottom:80px">
    <div class="secHead center rv">
      <span class="eyebrow">What's Inside</span>
      <h2>{insidehead}</h2>
      <p>{insidesub} <a href="/inside" style="color:var(--greenInk);font-weight:600">Full ingredient breakdown</a>.</p>
    </div>
    <div class="ingList" style="max-width:780px;margin:0 auto">
{ingrows}
    </div>
  </div>
</section>

<section>
  <div class="wrap" style="padding-top:80px;padding-bottom:80px">
    <div class="secHead center rv">
      <span class="eyebrow">Complete the Loadout</span>
      <h2>You might also like</h2>
    </div>
    <div class="carousel rv">
{related}
    </div>
  </div>
</section>

<section class="missionMini">
  <div class="wrap">
    <div class="txt rv">
      <span class="eyebrow" style="color:var(--green)">The Mission</span>
      <h2 class="disp">Every order fuels those who serve</h2>
      <p>Ricochet ships fitness care packages at no cost to deployed service members. When this order lands, part of it goes downrange.</p>
      <a class="btn ghostD" href="/mission">Read the full mission</a>
    </div>
    <div class="imgSide"></div>
  </div>
</section>

<section class="gtee">
  <div class="wrap" style="padding-top:80px;padding-bottom:90px">
    <div class="secHead center rv">
      <span class="eyebrow">Zero-Risk Order</span>
      <h2>The Ricochet Guarantee</h2>
    </div>
    <div class="gGrid">
      <div class="g rv" data-d="0"><h3>The No-Crash Guarantee</h3><div class="hook">All the energy. None of the wreckage.</div><p>Run it as directed for two weeks. If the crash is real, send it back for a full refund.</p><p><small>Within 30 days of delivery, one claim per customer.</small></p></div>
      <div class="g rv" data-d="70"><h3>The First Scoop Guarantee</h3><div class="hook">Decide on the sample, not the tub.</div><p>First orders ship with a sample scoop. Don't love it? Return the unopened tub for a full refund.</p><p><small>First-time orders only, tub unopened, within 30 days.</small></p></div>
      <div class="g rv" data-d="140"><h3>The Flavor Guarantee</h3><div class="hook">If it tastes like chemicals, it goes back.</div><p>If your flavor misses, swap it for another once, on us.</p><p><small>One swap per order, or return unopened within 30 days.</small></p></div>
      <div class="g rv" data-d="210"><h3>The Money Back Guarantee</h3><div class="hook">30 days. Clear terms. No games.</div><p>30 days from delivery to change your mind on any unopened product for a full refund.</p><p><small>Unopened products, one claim per customer per order.</small></p></div>
    </div>
  </div>
</section>
"""

def v(url):
    return url if "?" in url else url + "?width=700"

products = [
    dict(slug="ballistic-pre-workout", title="Ballistic Pre-Workout", flag="Flagship / High-Stim Pre-Workout",
         price="$49.99", mainimg="/img/ballistic-card.jpg",
         gallery=[("/img/ballistic-card.jpg", "Splash"),
                  (CDN + "Ballistic_PRE_SC_1.png?v=1779111666&width=700", "Sour Cherry"),
                  (CDN + "Ballistic_PRE_HB_2-2.png?v=1779111629&width=700", "Hawaiian Blitz"),
                  (CDN + "Ballistic_PRE_RP_1.png?v=1784857721&width=700", "Rocket Pop")],
         desc="High-stim pre-workout with 6,000 mg L-Citrulline and a 300 mg dual-source caffeine matrix. Every dose on the label.",
         lede="The flagship. Max pumps, a caffeine curve engineered against the crash, and dialed-in focus, with every single dose printed on the label.",
         points=["6,000 mg L-Citrulline for pumps and blood flow",
                 "300 mg dual-source caffeine: fast onset, long burn, no crash",
                 "Alpha-GPC plus L-Tyrosine for locked-in focus",
                 "Pink Himalayan Salt for hydration and fullness"],
         flavors=[("Sour Cherry Rush", "47667740901606", CDN + "Ballistic_PRE_SC_1.png?v=1779111666&width=700"),
                  ("Hawaiian Blitz", "47667740934374", CDN + "Ballistic_PRE_HB_2-2.png?v=1779111629&width=700"),
                  ("Rocket Pop", "48036105978086", CDN + "Ballistic_PRE_RP_1.png?v=1784857721&width=700")],
         variant="47667740901606", available=True,
         revhead="6 verified customer reviews", revsub="Live on the current store; full review import lands with the store build.",
         insidehead="Every dose on the label. Nothing hidden.",
         insidesub="The full Ballistic formula, disclosed to the milligram.",
         ings=[("6,000 mg", "L-Citrulline", "Max nitric oxide for blood flow, vascularity and pumps that actually show up."),
               ("300 mg", "Dual-Source Caffeine", "Caffeine Anhydrous for the hit, Infinergy Di-Caffeine Malate for the long burn."),
               ("Alpha-GPC", "Focus", "Sharper mind-to-muscle connection when the set gets heavy."),
               ("L-Tyrosine", "Stress Focus", "Holds concentration under fatigue, late in the session."),
               ("Pink Salt", "Hydration", "Himalayan salt for cell hydration and fuller pumps.")],
         related=["creatine-monohydrate", "ricochet-shaker-bottle", "tango-protocol-testosterone-booster"]),
    dict(slug="creatine-monohydrate", title="Creatine Monohydrate", flag="Daily Essential",
         price="$32.99", mainimg="/img/creatine-card.jpg",
         gallery=[("/img/creatine-card.jpg", "Splash"),
                  (CDN + "RicochetCreatineThumbnail_1.jpg?v=1776453028&width=700", "Tub"),
                  (CDN + "Creatine_1.jpg?width=700", "Detail"),
                  (CDN + "SF_Panel_Creatine_1.png?width=700", "Label panel")],
         desc="5 g micronized creatine monohydrate. Unflavored, dissolves clean, nothing else in the tub.",
         lede="The daily foundation. One ingredient at the gold-standard dose: 5 g of micronized creatine monohydrate, and nothing else.",
         points=["5 g micronized creatine monohydrate per scoop",
                 "Unflavored, mixes clean, no grit",
                 "Supports strength, power and recovery",
                 "Non-GMO and gluten free"],
         flavors=[], variant="47547869167846", available=True,
         revhead="7 verified customer reviews", revsub="Live on the current store; full review import lands with the store build.",
         insidehead="One ingredient. Full dose.",
         insidesub="The entire label, in one row:",
         ings=[("5 g", "Micronized Creatine", "The gold standard for strength and power, micronized so it dissolves clean. Nothing else in the tub.")],
         related=["ballistic-pre-workout", "ricochet-shaker-bottle", "afterburn-mach-i"]),
    dict(slug="afterburn-mach-i", title="Afterburn Mach-I", flag="Capsule Formula",
         price="$44.99", mainimg="/img/afterburn-card.jpg",
         gallery=[("/img/afterburn-card.jpg", "Splash"),
                  (CDN + "Ricochet-60Ct-Mockup-F-V3.jpg?v=1776452597&width=700", "Bottle"),
                  (CDN + "Afterburn_1.jpg?width=700", "Detail"),
                  (CDN + "Supplement_Facts.png?width=700", "Label panel")],
         desc="Capsule energy and focus formula. Two capsules, 20 to 30 minutes before training.",
         lede="Session energy in capsule form: a sustained energy matrix with laser focus, two capsules about 20 minutes before you train.",
         points=["Sustained energy matrix, engineered against the crash",
                 "Laser focus without the jitters",
                 "60 vegetarian capsules per bottle",
                 "Simple dosing: 2 capsules, 20 to 30 minutes pre-training"],
         flavors=[], variant="47547869397222", available=True,
         revhead="5 verified customer reviews", revsub="Live on the current store; full review import lands with the store build.",
         insidehead="The label is on the bottle.",
         insidesub="Full supplement facts are in the gallery above; the lab-sheet page lands on What's Inside as it's published.",
         ings=[("2 caps", "Per Serving", "Taken 20 to 30 minutes before training for sustained energy and focus through the session."),
               ("60 caps", "Per Bottle", "30 servings of vegetarian capsules per bottle.")],
         related=["ballistic-pre-workout", "tango-protocol-testosterone-booster", "creatine-monohydrate"]),
    dict(slug="tango-protocol-testosterone-booster", title="Tango Protocol", flag="Recovery / Vitality",
         price="$54.99", mainimg="/img/tango-card.jpg",
         gallery=[("/img/tango-card.jpg", "Splash"),
                  (CDN + "Tango_Protocol_Booster_1.png?v=1783978708&width=700", "Bottle"),
                  (CDN + "T-Booster_1.jpg?width=700", "Detail"),
                  (CDN + "Tango_Protocol_Booster_2.png?width=700", "Angle")],
         desc="Testosterone support with a full 600 mg of KSM-66 Ashwagandha plus Shilajit, Tongkat Ali, D3 and Zinc.",
         lede="Recovery and vitality support built on disclosed doses: a full 600 mg of KSM-66 Ashwagandha with Shilajit, Tongkat Ali, BioPerine, Vitamin D3 and Zinc.",
         points=["KSM-66 Ashwagandha at a full 600 mg",
                 "Shilajit, Tongkat Ali and BioPerine",
                 "Vitamin D3 and Zinc Bisglycinate",
                 "1 to 3 capsules each morning"],
         flavors=[], variant="47903754027238", available=True,
         revhead="Be the first to review", revsub="Reviews open on the current store; import lands with the store build.",
         insidehead="Disclosed doses, no theater.",
         insidesub="The core actives:",
         ings=[("600 mg", "KSM-66 Ashwagandha", "A full dose of the most studied ashwagandha extract."),
               ("Stack", "Shilajit + Tongkat Ali", "Traditional vitality actives with BioPerine for absorption."),
               ("D3 + Zinc", "Foundation", "Vitamin D3 and Zinc Bisglycinate for the hormonal baseline.")],
         related=["afterburn-mach-i", "ballistic-pre-workout", "creatine-monohydrate"]),
    dict(slug="ricochet-shaker-bottle", title="Ricochet Shaker Bottle", flag="Essential Gear",
         price="$9.99", mainimg=CDN + "ShakerBottle_2.png?v=1779197156&width=700",
         gallery=[(CDN + "ShakerBottle_2.png?v=1779197156&width=700", "Shaker"),
                  (CDN + "Shaker_Web_Image_1.jpg?width=700", "Detail")],
         desc="BPA-free shaker with a zero-leak heavy-duty lid.",
         lede="High-grade polypropylene, BPA and phthalate free, odor resistant, with a heavy-duty lid and a zero-leak guarantee.",
         points=["Zero-leak guarantee with heavy-duty lid",
                 "BPA-free and phthalate-free",
                 "Odor-resistant material",
                 "Top-rack dishwasher safe"],
         flavors=[], variant="47691969462502", available=True,
         revhead="Zero-leak guarantee", revsub="If the lid lets go in your bag, it's on us.",
         insidehead="Built like the rest of the line.",
         insidesub="Simple, durable, and honest:",
         ings=[("BPA-Free", "Polypropylene", "High-grade, odor-resistant material that survives the bottom of a gym bag."),
               ("Zero-Leak", "Heavy-Duty Lid", "The one that doesn't open itself in your bag.")],
         related=["ballistic-pre-workout", "creatine-monohydrate", "ricochet-oversized-t-shirt"]),
    dict(slug="ricochet-oversized-t-shirt", title="Oversized T-Shirt", flag="Essential Gear",
         price="$32.99", mainimg=CDN + "TShirt04-Design1Adjustment.jpg?v=1776778142&width=700",
         gallery=[(CDN + "TShirt04-Design1Adjustment.jpg?v=1776778142&width=700", "Front"),
                  (CDN + "TShirt_01-2.jpg?width=700", "Detail")],
         desc="Heavy cotton oversized tee with mineral-wash fabric.",
         lede="Oversized vintage fit in heavy 100 percent cotton, mineral-washed so it resists shrinking and fading.",
         points=["Heavy 100 percent cotton",
                 "Oversized vintage fit",
                 "Mineral-wash finish resists shrinking and fading",
                 "Sizes S through XXL"],
         flavors=[], variant=None, available=False,
         revhead="Restocking now", revsub="Every size is currently sold out on the store; back soon.",
         insidehead="Heavy cotton, mineral wash.",
         insidesub="The build:",
         ings=[("100%", "Heavy Cotton", "Substantial fabric with an oversized vintage fit."),
               ("Mineral", "Wash Finish", "Resists shrinking and fading through real wash cycles.")],
         related=["ricochet-shaker-bottle", "ballistic-pre-workout", "creatine-monohydrate"]),
]

cards = {p["slug"]: p for p in products}

def related_card(slug):
    p = cards[slug]
    img = p["mainimg"]
    return """      <a class="prod" href="/products/%s">
        <div class="ph"><img src="%s" alt="%s"></div>
        <div class="meta"><span class="flag">%s</span><h3>%s</h3>
        <div class="row"><span class="price">%s</span><span class="go">View</span></div></div>
      </a>""" % (slug, img, p["title"], p["flag"], p["title"], p["price"])

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "products")
os.makedirs(OUT, exist_ok=True)

for p in products:
    thumbs = "\n".join('        <button type="button"%s data-img="%s"><img src="%s" alt="%s"></button>'
                       % (' class="on"' if i == 0 else "", u, u, lab) for i, (u, lab) in enumerate(p["gallery"]))
    points = "\n".join('        <li>%s</li>' % x for x in p["points"])
    if p["flavors"]:
        pills = "".join('<span class="pill%s" data-variant="%s" data-img="%s" style="cursor:pointer">%s</span>'
                        % (" on" if i == 0 else "", vid, img, name) for i, (name, vid, img) in enumerate(p["flavors"]))
        flavors = '      <div style="margin-top:6px"><b style="font-family:\'Barlow Condensed\';letter-spacing:.08em;text-transform:uppercase;font-size:14px">Pick your flavor</b></div>\n      <div class="flavorPills">%s</div>' % pills
    else:
        flavors = ""
    if p["available"] and p["variant"]:
        buybtn = '<a class="btn" id="cartBtn" href="https://ricochetsupplements.com/cart/%s:1">Add to cart &nbsp;%s</a>' % (p["variant"], p["price"])
        buynote = "Checkout runs on the secure Ricochet store."
    else:
        buybtn = '<a class="btn ghostL" href="https://ricochetsupplements.com/products/%s">Restocking: check availability</a>' % p["slug"]
        buynote = "Every size is currently sold out; availability updates on the store."
    ingrows = "\n".join('      <div class="ingRow rv" data-d="%d"><span class="dose">%s<small>%s</small></span><p>%s</p></div>'
                        % (i * 60, d, s, t) for i, (d, s, t) in enumerate(p["ings"]))
    related = "\n".join(related_card(s) for s in p["related"])
    html = HEAD.format(title=p["title"], desc=p["desc"]) + PDP.format(
        mainimg=p["mainimg"], title=p["title"], flag=p["flag"], price=p["price"],
        thumbs=thumbs, revhead=p["revhead"], revsub=p["revsub"], lede=p["lede"],
        points=points, flavors=flavors, buybtn=buybtn, buynote=buynote,
        insidehead=p["insidehead"], insidesub=p["insidesub"], ingrows=ingrows, related=related) + FOOT
    path = os.path.join(OUT, p["slug"] + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path, len(html))
