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
<meta property="og:title" content="{title} | Ricochet Supplements">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{ogimg}">
<meta property="og:type" content="product">
<meta name="twitter:card" content="summary_large_image">
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
const io = new IntersectionObserver(es => es.forEach(e => {if (e.isIntersecting) {e.target.classList.add('in'); io.unobserve(e.target)}}), {threshold: .12});
document.querySelectorAll('.rv').forEach(el => {el.style.transitionDelay = (el.dataset.d || 0) + 'ms'; io.observe(el)});
const mainImg = document.getElementById('mainImg');
document.querySelectorAll('.thumbs button').forEach(b => b.addEventListener('click', () => {
  document.querySelectorAll('.thumbs button').forEach(x => x.classList.remove('on'));
  b.classList.add('on');
  mainImg.src = b.dataset.img;
}));
const cartBtn = document.getElementById('cartBtn');
document.querySelectorAll('.flavorPills .pill[data-variant]').forEach(p => p.addEventListener('click', () => {
  document.querySelectorAll('.flavorPills .pill').forEach(x => x.classList.remove('on'));
  p.classList.add('on');
  if (cartBtn) cartBtn.href = 'https://ricochetsupplements.com/cart/' + p.dataset.variant + ':1';
  if (p.dataset.img) mainImg.src = p.dataset.img;
}));
</script>
</body>
</html>
"""

PDP = """
<section>
  <div class="wrap pdp" style="padding-top:60px;padding-bottom:80px">
    <div class="gal rv">
      <div class="main"><img id="mainImg" src="{mainimg}" alt="{title}"></div>
      <div class="thumbs">
{thumbs}
      </div>
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

{reviewsec}
<section class="shopBand">
  <div class="wrap" style="padding-top:80px;padding-bottom:80px">
    <div class="secHead center rv">
      <span class="eyebrow">What's Inside</span>
      <h2>{insidehead}</h2>
      <p>{insidesub} <a href="{insidelink}" style="color:var(--greenInk);font-weight:600">Full ingredient breakdown</a>.</p>
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

REVSEC = """
<section>
  <div class="wrap" style="padding-top:80px;padding-bottom:80px">
    <div class="secHead center rv">
      <span class="eyebrow">Customer Reviews</span>
      <h2>What the unit says</h2>
      <p>Pulled word for word from customer reviews on the Ricochet store; verified purchases are marked.</p>
    </div>
    <div class="revGrid">
%s
    </div>
  </div>
</section>
"""

def rev_card(i, name, date, body, verified=True):
    vrf = '<span class="vrf">Verified</span>' if verified else ""
    return ('      <div class="rev rv" data-d="%d"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>'
            '<p>"%s"</p><div class="who"><b>%s</b>%s<span>%s</span></div></div>'
            % (i * 70, body, name, vrf, date))

products = [
    dict(slug="ballistic-pre-workout", title="Ballistic Pre-Workout", flag="Flagship / High-Stim Pre-Workout",
         price="$49.99", mainimg="/img/ballistic-card.jpg",
         gallery=[("/img/ballistic-card.jpg", "Splash"),
                  (CDN + "Ballistic_PRE_SC_1.png?v=1779111666&width=700", "Sour Cherry"),
                  (CDN + "Ballistic_PRE_HB_2-2.png?v=1779111629&width=700", "Hawaiian Blitz"),
                  (CDN + "IMG-4832.png?width=700", "Supplement Facts")],
         desc="High-stim pre-workout with 6,000 mg L-Citrulline and a 300 mg dual-source caffeine matrix. Every dose on the label.",
         lede="The flagship. Max pumps, a caffeine curve engineered against the crash, and dialed-in focus, with every single dose printed on the label.",
         points=["6,000 mg L-Citrulline for pumps and blood flow",
                 "3,200 mg Beta-Alanine for rep-after-rep endurance",
                 "300 mg dual-source caffeine: fast onset, long burn, no crash",
                 "1,000 mg L-Tyrosine plus Alpha-GPC and L-Theanine for locked-in focus",
                 "Electrolytes from Pink Himalayan Salt for hydration"],
         flavors=[("Sour Cherry Rush", "47667740901606", CDN + "Ballistic_PRE_SC_1.png?v=1779111666&width=700"),
                  ("Hawaiian Blitz", "47667740934374", CDN + "Ballistic_PRE_HB_2-2.png?v=1779111629&width=700"),
                  ("Rocket Pop", "48036105978086", CDN + "Ballistic_PRE_RP_1.png?v=1784857721&width=700")],
         variant="47667740901606", available=True,
         revhead="6 verified customer reviews", revsub="Live on the current store; full review import lands with the store build.",
         insidehead="Every dose on the label. Nothing hidden.",
         insidesub="The full Ballistic formula, disclosed to the milligram.",
         ings=[("6,000 mg", "L-Citrulline", "Max nitric oxide for blood flow, vascularity and pumps that actually show up."),
               ("3,200 mg", "Beta-Alanine", "Buffers acid in working muscle for endurance deep into the set. Yes, the tingles are real, and they mean it's dosed."),
               ("300 mg", "Dual-Source Caffeine", "225 mg Caffeine Anhydrous for the hit, Infinergy Di-Caffeine Malate for the long burn."),
               ("1,000 mg", "L-Tyrosine", "Holds concentration under fatigue, late in the session."),
               ("300 mg", "Alpha-GPC 50%", "Sharper mind-to-muscle connection, with 100 mg L-Theanine smoothing the stim curve."),
               ("Electrolytes", "Pink Salt + Mag + K", "Sodium from Himalayan salt with magnesium and potassium for hydration and fuller pumps.")],
         reviews=[("Robert Deleon", "08/12/2026", "Amazing flavor! Energy and intensity that lasts! Absolute banger of a preworkout. Highly recommend!", True),
                  ("Joel Orozco", "08/01/2026", "Great preworkout ive been in the preworkout game for 16 years tried multiple across the board this is hands down top 5!", True),
                  ("Rick", "07/31/2026", "Got this pre once and now it's the only pre I get. Good stuff", False),
                  ("Verified Customer", "07/31/2026", "This formula is awesome and it tastes great. Whether you pre measure or dry scoop like a maniac (me) you're about to get that pump! Shout out Mark and his team for providing the RGV with these high quality products!!", True),
                  ("Dustin Valdez", "07/31/2026", "I get the best workouts using this pre workout!!!! LOVE IT!!", True)],
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
         reviews=[("Daniel Montano", "07/18/2026", "Really happy with this creatine so far. It mixes easily, doesn't have a weird taste, and I've definitely noticed better strength and performance during my workouts. No stomach issues either, which is a big plus. Great quality for the price, and I'll definitely be ordering it again.", True),
                  ("John Hernandez", "07/28/2026", "Frequently seeing noticeable gains in workout stamina, muscle recovery, and overall lifting power over time each day in the gym.", True),
                  ("Alexis Exinia", "07/28/2026", "I love that it's not grainy at all like previous ones I have purchased and I mix it up with my pre workout and thermos before a workout!", True),
                  ("Mike Mendez", "07/31/2026", "Great product! No complaints on product, and I also love the T shirt. Awesome fit and fits fantastic. Also the customer service was amazing, they were able to meet for local delivery and followed up asking if the products met my standard.", True)],
         related=["ballistic-pre-workout", "ricochet-shaker-bottle", "afterburn-mach-i"]),
    dict(slug="afterburn-mach-i", title="Afterburn Mach-I", flag="Thermogenic Capsules",
         price="$44.99", mainimg="/img/afterburn-card.jpg",
         gallery=[("/img/afterburn-card.jpg", "Splash"),
                  (CDN + "Ricochet-60Ct-Mockup-F-V3.jpg?v=1776452597&width=700", "Bottle"),
                  (CDN + "Afterburn_1.jpg?width=700", "Detail"),
                  (CDN + "Supplement_Facts.png?width=700", "Label panel")],
         desc="Thermogenic capsules: 275 mg dual-form caffeine, green tea EGCG, Paradoxine, Capsimax and a focus stack, every dose disclosed. Two capsules, 20 to 30 minutes before training.",
         lede="Session energy in capsule form: a nine-active thermogenic with every dose on the label, two capsules about 20 to 30 minutes before you train.",
         points=["275 mg caffeine from two release speeds, engineered against the crash",
                 "Green tea catechins, Paradoxine and Capsimax: the studied thermogenic trio",
                 "Alpha-GPC and L-Theanine for focus without the jitters",
                 "60 capsules per bottle: 30 servings of 2, taken 20 to 30 minutes pre-training"],
         flavors=[], variant="47547869397222", available=True,
         revhead="5 customer reviews", revsub="Live on the current store; full review import lands with the store build.",
         insidehead="Every dose on the label.",
         insidesub="All nine actives, straight from the panel (also in the gallery above):",
         ings=[("275 mg", "Caffeine, 2 forms", "Caffeine anhydrous plus sustained-release caffeine: fast onset and a long tail, roughly three cups of coffee per serving."),
               ("250 mg", "Green Tea Extract", "Standardized to 50 percent polyphenols and 15 percent EGCG, the catechins that pair with caffeine."),
               ("200 mg", "Acetyl-L-Carnitine", "The carnitine form that also crosses into the brain, alongside 25 mg ProGBB, its precursor."),
               ("150 mg", "Alpha-GPC 50%", "The focus half of the formula, with 100 mg L-Theanine smoothing the stim curve."),
               ("30 mg", "Paradoxine", "Grains of paradise extract, at the 30 mg used in the human energy-expenditure research."),
               ("25 mg", "Capsimax", "Capsicum extract, 2 percent capsaicinoids in a beadlet that releases past the stomach, plus 5 mg BioPerine for absorption.")],
         reviews=[("Abel", "07/27/2026", "Mach 1 was critical in helping me shed unwanted body fat while hitting the gym hard. No crash, no jitters, just focus and appetite suppression. If you're trying to take your workouts to the next level. This is the supplement for you!", False),
                  ("Lola", "05/01/2026", "Literally my favorite supplement for Laser focus during lifts, no crash no jitters.", True),
                  ("Blanca", "04/22/2026", "I can feel the difference taking these compared to other fat burners on the market. I am less hungry and I have no midday crash so more energy throughout the day! These work extremely well!", False),
                  ("Kris", "04/21/2026", "Can feel, and see the difference. Keeps energy up during long workouts", False),
                  ("Itzel", "04/21/2026", "Amazing source of energy, without jitters, or the crash afterwards", False)],
         related=["ballistic-pre-workout", "tango-protocol-testosterone-booster", "creatine-monohydrate"]),
    dict(slug="tango-protocol-testosterone-booster", title="Tango Protocol", flag="Recovery / Vitality",
         price="$54.99", mainimg="/img/tango-card.jpg",
         gallery=[("/img/tango-card.jpg", "Splash"),
                  (CDN + "Tango_Protocol_Booster_1.png?v=1783978708&width=700", "Bottle"),
                  (CDN + "T-Booster_1.jpg?width=700", "Detail"),
                  (CDN + "Tango_Protocol_Booster_3_77a0635f-1140-483d-a2b0-388421a6b257.png?width=700", "Supplement Facts")],
         desc="Testosterone support with a full 600 mg of KSM-66 Ashwagandha plus Shilajit, Tongkat Ali, D3 and Zinc.",
         lede="Recovery and vitality support with every dose on the label: KSM-66 Ashwagandha at a full 600 mg, backed by Shilajit, Tongkat Ali, D3, Zinc, Boron and BioPerine.",
         points=["600 mg KSM-66 Ashwagandha, the most studied extract",
                 "400 mg Shilajit and 200 mg Tongkat Ali",
                 "5,000 IU Vitamin D3, 30 mg Zinc Bisglycinate, 10 mg Boron",
                 "5 mg BioPerine for absorption; 3 capsules, 30 servings"],
         flavors=[], variant="47903754027238", available=True,
         revhead="Be the first to review", revsub="Reviews open on the current store; import lands with the store build.",
         insidehead="Every dose on the label.",
         insidesub="The full panel, straight from the bottle (also in the gallery above):",
         ings=[("600 mg", "KSM-66 Ashwagandha", "A full dose of the most studied ashwagandha extract."),
               ("400 mg", "Shilajit Extract", "Traditional mineral-rich vitality active."),
               ("200 mg", "Tongkat Ali", "Eurycoma longifolia extract."),
               ("5,000 IU", "Vitamin D3", "With 30 mg Zinc Bisglycinate and 10 mg Boron for the hormonal baseline."),
               ("5 mg", "BioPerine", "Standardized 95 percent piperine for absorption.")],
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

# Deep-link each supplement's "Full ingredient breakdown" to its tab on /inside (gear links to the page top).
INSIDE_HASH = {"ballistic-pre-workout": "ballistic", "creatine-monohydrate": "creatine",
               "afterburn-mach-i": "afterburn", "tango-protocol-testosterone-booster": "tango"}

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
    revs = p.get("reviews") or []
    reviewsec = REVSEC % "\n".join(rev_card(i, n, d, b, vf) for i, (n, d, b, vf) in enumerate(revs)) if revs else ""
    ogimg = p["mainimg"] if p["mainimg"].startswith("http") else "https://ricochet-supplements.vercel.app" + p["mainimg"]
    insidelink = "/inside#" + INSIDE_HASH[p["slug"]] if p["slug"] in INSIDE_HASH else "/inside"
    html = HEAD.format(title=p["title"], desc=p["desc"], ogimg=ogimg) + PDP.format(
        mainimg=p["mainimg"], title=p["title"], flag=p["flag"], price=p["price"],
        thumbs=thumbs, revhead=p["revhead"], revsub=p["revsub"], lede=p["lede"],
        points=points, flavors=flavors, buybtn=buybtn, buynote=buynote, reviewsec=reviewsec,
        insidehead=p["insidehead"], insidesub=p["insidesub"], insidelink=insidelink,
        ingrows=ingrows, related=related) + FOOT
    path = os.path.join(OUT, p["slug"] + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path, len(html))
