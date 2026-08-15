import os

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
</script>
</body>
</html>
"""

PDP = """
<section>
  <div class="wrap pdp" style="padding-top:70px;padding-bottom:90px">
    <div class="pdpImg rv"><img src="{img}" alt="{title}"></div>
    <div class="pdpInfo">
      <span class="flag">{flag}</span>
      <h1>{title}</h1>
      <div class="price">{price}</div>
      <p class="lede">{lede}</p>
      <ul class="points">
{points}
      </ul>
{flavors}
      <div class="buyRow">
        <a class="btn" href="{buy}">Add to cart &nbsp;{price}</a>
        <span class="buyNote">Checkout runs on the secure Ricochet store.</span>
      </div>
      <div class="pdpTicks"><span>Veteran Owned</span><span>Made in the U.S.</span><span>No Proprietary Blends</span></div>
      <div class="faq pdpAcc">
        <details><summary>What's inside</summary><p>{inside} See the <a href="/inside" style="color:var(--greenInk);font-weight:600">full ingredient breakdown</a>.</p></details>
        <details><summary>Shipping and returns</summary><p>Ships from Texas. 30 days from delivery to return any unopened product for a full refund. Full details in the shipping and refund policies in the footer.</p></details>
        <details><summary>The Ricochet Guarantee</summary><p>Four named guarantees with clear terms: no-crash, first-scoop sample on first orders, one flavor swap, and 30-day money back on unopened products. <a href="/#guarantee" style="color:var(--greenInk);font-weight:600">Read the terms</a>.</p></details>
      </div>
    </div>
  </div>
</section>
"""

products = [
    dict(slug="ballistic-pre-workout", title="Ballistic Pre-Workout", flag="Flagship / High-Stim Pre-Workout",
         price="$49.99", img="/img/ballistic-card.jpg",
         desc="High-stim pre-workout with 6,000 mg L-Citrulline and a 300 mg dual-source caffeine matrix. Every dose on the label.",
         lede="The flagship. Max pumps, a caffeine curve engineered against the crash, and dialed-in focus, with every single dose printed on the label.",
         points=["6,000 mg L-Citrulline for pumps and blood flow",
                 "300 mg dual-source caffeine: fast onset, long burn, no crash",
                 "Alpha-GPC plus L-Tyrosine for locked-in focus",
                 "Pink Himalayan Salt for hydration and fullness"],
         flavors=["Sour Cherry Rush", "Hawaiian Blitz", "Rocket Pop"],
         inside="6,000 mg L-Citrulline, 300 mg dual-source caffeine (Caffeine Anhydrous plus Infinergy Di-Caffeine Malate), Alpha-GPC, L-Tyrosine and Pink Himalayan Salt. No proprietary blends."),
    dict(slug="creatine-monohydrate", title="Creatine Monohydrate", flag="Daily Essential",
         price="$32.99", img="/img/creatine-card.jpg",
         desc="5 g micronized creatine monohydrate. Unflavored, dissolves clean, nothing else in the tub.",
         lede="The daily foundation. One ingredient at the gold-standard dose: 5 g of micronized creatine monohydrate, and nothing else.",
         points=["5 g micronized creatine monohydrate per scoop",
                 "Unflavored, mixes clean, no grit",
                 "Supports strength, power and recovery",
                 "Non-GMO and gluten free"],
         flavors=[],
         inside="5 g micronized creatine monohydrate per scoop. Unflavored. That is the whole label."),
    dict(slug="afterburn-mach-i", title="Afterburn Mach-I", flag="Capsule Formula",
         price="$44.99", img="/img/afterburn-card.jpg",
         desc="Capsule energy and focus formula. Two capsules, 20 to 30 minutes before training.",
         lede="Session energy in capsule form: a sustained energy matrix with laser focus, two capsules about 20 minutes before you train.",
         points=["Sustained energy matrix, engineered against the crash",
                 "Laser focus without the jitters",
                 "60 vegetarian capsules per bottle",
                 "Simple dosing: 2 capsules, 20 to 30 minutes pre-training"],
         flavors=[],
         inside="Full panel on the bottle label; the lab-sheet page for Afterburn lands on the What's Inside page as it's published."),
    dict(slug="tango-protocol-testosterone-booster", title="Tango Protocol", flag="Recovery / Vitality",
         price="$54.99", img="/img/tango-card.jpg",
         desc="Testosterone support with a full 600 mg of KSM-66 Ashwagandha plus Shilajit, Tongkat Ali, D3 and Zinc.",
         lede="Recovery and vitality support built on disclosed doses: a full 600 mg of KSM-66 Ashwagandha with Shilajit, Tongkat Ali, BioPerine, Vitamin D3 and Zinc.",
         points=["KSM-66 Ashwagandha at a full 600 mg",
                 "Shilajit, Tongkat Ali and BioPerine",
                 "Vitamin D3 and Zinc Bisglycinate",
                 "1 to 3 capsules each morning"],
         flavors=[],
         inside="KSM-66 Ashwagandha 600 mg, Shilajit, Tongkat Ali, BioPerine, Vitamin D3, Zinc Bisglycinate."),
    dict(slug="ricochet-shaker-bottle", title="Ricochet Shaker Bottle", flag="Essential Gear",
         price="$9.99", img="https://cdn.shopify.com/s/files/1/0801/6933/7062/files/ShakerBottle_2.png?v=1779197156&width=700",
         desc="BPA-free shaker with a zero-leak heavy-duty lid.",
         lede="High-grade polypropylene, BPA and phthalate free, odor resistant, with a heavy-duty lid and a zero-leak guarantee.",
         points=["Zero-leak guarantee with heavy-duty lid",
                 "BPA-free and phthalate-free",
                 "Odor-resistant material",
                 "Top-rack dishwasher safe"],
         flavors=[],
         inside="High-grade polypropylene shaker with mixing insert."),
    dict(slug="ricochet-oversized-t-shirt", title="Oversized T-Shirt", flag="Essential Gear",
         price="$32.99", img="https://cdn.shopify.com/s/files/1/0801/6933/7062/files/TShirt04-Design1Adjustment.jpg?v=1776778142&width=700",
         desc="Heavy cotton oversized tee with mineral-wash fabric.",
         lede="Oversized vintage fit in heavy 100 percent cotton, mineral-washed so it resists shrinking and fading.",
         points=["Heavy 100 percent cotton",
                 "Oversized vintage fit",
                 "Mineral-wash finish resists shrinking and fading",
                 "Sizes S through XXL"],
         flavors=[],
         inside="100 percent heavy cotton, mineral-wash finish."),
]

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "products")
os.makedirs(OUT, exist_ok=True)

for p in products:
    points = "\n".join('        <li>%s</li>' % x for x in p["points"])
    if p["flavors"]:
        pills = "".join('<span class="pill%s">%s</span>' % (" on" if i == 0 else "", f) for i, f in enumerate(p["flavors"]))
        flavors = '      <div class="flavorPills">%s</div>\n      <span class="buyNote">Flavor is picked at checkout.</span>' % pills
    else:
        flavors = ""
    buy = "https://ricochetsupplements.com/products/" + p["slug"]
    html = HEAD.format(title=p["title"], desc=p["desc"]) + PDP.format(
        img=p["img"], title=p["title"], flag=p["flag"], price=p["price"], lede=p["lede"],
        points=points, flavors=flavors, buy=buy, inside=p["inside"]) + FOOT
    path = os.path.join(OUT, p["slug"] + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path, len(html))
