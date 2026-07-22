#!/usr/bin/env python3
"""Generates every sub-page of the Seafarer Realty prototype from shared
nav/footer templates so the whole site stays visually and structurally
consistent with index.html."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

def nav(prefix):
    return f'''<nav class="nav" id="mainNav">
  <a href="{prefix}index.html" class="nav-logo">
    <img src="{prefix}assets/img/logo.png" alt="Seafarer Realty logo">
    <span class="nav-logo-text">Seafarer Realty</span>
  </a>
  <ul class="nav-links">
    <li><a href="{prefix}index.html">Home</a></li>
    <li><a href="{prefix}listings/index.html">Buy</a></li>
    <li><a href="{prefix}index.html#contact">Sell</a></li>
    <li><a href="{prefix}index.html#communities">Communities</a></li>
    <li><a href="{prefix}index.html#lifestyle">Lifestyle</a></li>
    <li><a href="{prefix}index.html#market">Market Reports</a></li>
    <li><a href="{prefix}index.html#alexia">About</a></li>
    <li><a href="{prefix}blog/index.html">Blog</a></li>
    <li><a href="{prefix}index.html#contact">Contact</a></li>
    <li><a href="{prefix}index.html#contact" class="nav-cta">Home Valuation</a></li>
  </ul>
  <button class="nav-toggle" id="navToggle" aria-label="Open menu">☰</button>
</nav>

<div class="mobile-menu" id="mobileMenu">
  <button class="mobile-close" id="mobileClose" aria-label="Close menu">✕</button>
  <a href="{prefix}index.html">Home</a>
  <a href="{prefix}listings/index.html">Buy</a>
  <a href="{prefix}index.html#contact">Sell</a>
  <a href="{prefix}index.html#communities">Communities</a>
  <a href="{prefix}index.html#lifestyle">Lifestyle</a>
  <a href="{prefix}index.html#market">Market Reports</a>
  <a href="{prefix}index.html#alexia">About</a>
  <a href="{prefix}blog/index.html">Blog</a>
  <a href="{prefix}index.html#contact">Contact</a>
</div>
'''

def footer(prefix):
    return f'''<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="{prefix}assets/img/logo.png" alt="Seafarer Realty">
        <p>Authentic Florida Keys Living</p>
        <div class="footer-social">
          <a href="https://instagram.com/seafarerrealty" target="_blank" rel="noopener" aria-label="Instagram">IG</a>
          <a href="https://facebook.com/seafarerrealty" target="_blank" rel="noopener" aria-label="Facebook">FB</a>
          <a href="https://youtube.com/@seafarerrealty" target="_blank" rel="noopener" aria-label="YouTube">YT</a>
          <a href="https://linkedin.com/company/seafarerrealty" target="_blank" rel="noopener" aria-label="LinkedIn">IN</a>
        </div>
      </div>
      <div class="footer-col">
        <h5>Quick Links</h5>
        <a href="{prefix}index.html#communities">Communities</a>
        <a href="{prefix}index.html#lifestyle">Lifestyle</a>
        <a href="{prefix}listings/index.html">Buying</a>
        <a href="{prefix}index.html#contact">Selling</a>
        <a href="{prefix}index.html#market">Market Reports</a>
      </div>
      <div class="footer-col">
        <h5>Company</h5>
        <a href="{prefix}index.html#alexia">About</a>
        <a href="{prefix}blog/index.html">Blog</a>
        <a href="{prefix}index.html#contact">Contact</a>
        <a href="{prefix}listings/index.html">MLS</a>
      </div>
      <div class="footer-col">
        <h5>Contact</h5>
        <p>Islamorada, Florida Keys</p>
        <p>hello@seafarerrealty.com</p>
        <p>(305) 555-0148</p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Seafarer Realty, LLC. All rights reserved.</span>
      <div class="footer-bottom-links">
        <a href="{prefix}privacy-policy.html">Privacy Policy</a>
        <a href="{prefix}accessibility.html">ADA Accessibility</a>
        <a href="{prefix}realtor-code-of-ethics.html">Realtor Code of Ethics</a>
      </div>
    </div>
  </div>
</footer>

<div class="prototype-banner" id="prototypeBanner">Prototype build for client review — <b>Seafarer Realty</b> · imagery &amp; copy are placeholders pending final assets<button class="prototype-banner-close" id="prototypeBannerClose" aria-label="Dismiss">✕</button></div>
'''

def page(title, description, prefix, body, extra_head=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/css/style.css">
{extra_head}</head>
<body>
{nav(prefix)}
{body}
{footer(prefix)}
<script src="{prefix}assets/js/main.js"></script>
</body>
</html>
'''

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w') as f:
        f.write(content)
    print("wrote", path)

# ---------------------------------------------------------------------------
# COMMUNITIES
# ---------------------------------------------------------------------------
communities = [
    dict(slug="key-largo", name="Key Largo", hero="mangrove-beach.jpg",
         tagline="The first breath of island life, and the dive capital of the world.",
         intro="Key Largo is where the mainland exhales and the Keys begin. It's the closest island to South Florida, which makes it a favorite for buyers who want waterfront living without giving up an easy drive to Miami — and it's home to the largest living coral barrier reef in the continental United States.",
         love="Key Largo moves at the pace of a dive boat schedule. Mornings start early at the marina, afternoons belong to John Pennekamp Coral Reef State Park, and the canal-front communities here offer some of the most approachable waterfront price points in the entire chain.",
         neighborhoods=["Ocean Reef Club", "Rock Harbor", "Largo Sound", "Key Largo Beach Estates"],
         lifestyle=["Snorkeling & diving the reef", "Glass-bottom boat tours", "Waterfront tiki bars", "Everglades backcountry access"],
         stats=[("$1.1M","Median Waterfront"), ("38 mi","To Miami"), ("11,000+","Year-Round Residents")],
         img2="drift.jpg", img3="beachin.jpg"),
    dict(slug="islamorada", name="Islamorada", hero="freedom.jpg",
         tagline="The sportfishing capital of the world.",
         intro="Islamorada is actually a string of islands — Plantation Key, Windley Key, Upper and Lower Matecumbe — stitched together by the same Overseas Highway, and united by a fishing culture that runs generations deep.",
         love="This is where the boat leaves the dock before the sun clears the mangroves. Islamorada balances world-class backcountry and offshore fishing with a genuinely upscale dining and boutique scene, drawing both serious anglers and design-forward second-home buyers.",
         neighborhoods=["Plantation Key", "Windley Key", "Upper Matecumbe", "Lower Matecumbe"],
         lifestyle=["Backcountry & offshore charters", "Founders Park", "Morada Way arts district", "Historic Robbie's Marina"],
         stats=[("$1.9M","Median Waterfront"), ("70 mi","To Miami"), ("Sportfishing","Capital of the World")],
         img2="mangrove-beach.jpg", img3="water.jpg"),
    dict(slug="marathon", name="Marathon", hero="causeway.jpg",
         tagline="The heart of the Keys.",
         intro="Sitting almost exactly at the midpoint of the island chain, Marathon is the practical heart of the Keys — a real working town with its own airport, hospital, and schools, alongside some of the most family-friendly beaches in the region.",
         love="Marathon draws buyers who want the lifestyle without the crowds: quiet canal homes, a slower pace, and easy access to both the Gulf and Atlantic sides. Sombrero Beach and the Turtle Hospital are neighborhood fixtures, not tourist stops.",
         neighborhoods=["Key Colony Beach", "Duck Key", "Boot Key", "Sombrero Beach area"],
         lifestyle=["Sombrero Beach", "Turtle Hospital", "Marathon Airport day trips", "Boot Key Harbor sunsets"],
         stats=[("$820K","Median Waterfront"), ("50 mi","To Key West"), ("Full-Service","Town Amenities")],
         img2="fred-bridge.jpg", img3="seven-mile-sunset.jpg"),
    dict(slug="big-pine-key", name="Big Pine Key", hero="drift.jpg",
         tagline="Backcountry, quiet, and wild.",
         intro="Big Pine Key and the Lower Keys are the wild, unhurried side of the chain — home to the National Key Deer Refuge, sprawling backcountry flats, and a noticeably slower rhythm than the Upper Keys.",
         love="Buyers come here for privacy, nature, and value. Lots tend to be larger, the deer wander through front yards at dusk, and the sunsets over the backcountry are, locals will tell you, the best in the Keys.",
         neighborhoods=["No Name Key", "Ramrod Key", "Cudjoe Key", "Summerland Key"],
         lifestyle=["National Key Deer Refuge", "Bahia Honda State Park nearby", "Backcountry flats fishing", "Quiet canal living"],
         stats=[("$690K","Median Waterfront"), ("30 mi","To Key West"), ("Largest","Average Lot Size")],
         img2="water.jpg", img3="mangrove-beach.jpg"),
    dict(slug="key-west", name="Key West", hero="seven-mile-sunset.jpg",
         tagline="The end of the road, and the beginning of everything else.",
         intro="Key West is the terminus of US-1 and the cultural capital of the Keys — Old Town charm, a working harbor, and a level of walkability found nowhere else in the chain.",
         love="From historic conch houses to modern harbor-front condos, Key West offers the widest range of property types in the Keys, all wrapped in a nightly sunset celebration at Mallory Square that never gets old.",
         neighborhoods=["Old Town", "New Town", "Truman Annex", "Casa Marina area"],
         lifestyle=["Mallory Square sunset celebration", "Duval Street dining & galleries", "Historic Seaport", "Fort Zachary Taylor beach"],
         stats=[("$1.4M","Median Home Price"), ("0 mi","End of US-1"), ("Old Town","Historic District")],
         img2="freedom.jpg", img3="fred-bridge.jpg"),
]

def community_page(c, all_c):
    others = [x for x in all_c if x["slug"] != c["slug"]][:3]
    related = "\n".join(
        f'<a class="related-card" href="{o["slug"]}.html"><img src="../assets/img/{o["hero"]}" alt="{o["name"]}"><span>{o["name"]}</span></a>'
        for o in others
    )
    neigh = "".join(f"<li>{n}</li>" for n in c["neighborhoods"])
    life = "".join(f"<li>{l}</li>" for l in c["lifestyle"])
    stats = "".join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v, l in c["stats"])
    body = f'''
<section class="page-hero">
  <img src="../assets/img/{c["hero"]}" alt="{c["name"]}, Florida Keys">
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="../index.html">Home</a> / <a href="../index.html#communities">Communities</a> / {c["name"]}</div>
    <h1>{c["name"]}</h1>
    <p class="lede">{c["tagline"]}</p>
  </div>
</section>

<section class="page-body">
  <div class="container page-cols">
    <div class="page-main reveal">
      <h2>Why You'll Love Living Here</h2>
      <p>{c["intro"]}</p>
      <p>{c["love"]}</p>

      <div class="stat-row">{stats}</div>

      <h2>Featured Neighborhoods</h2>
      <ul>{neigh}</ul>

      <h2>Lifestyle Highlights</h2>
      <ul>{life}</ul>

      <h2>Waterfront Living</h2>
      <p>Canal, oceanfront, and bayfront options all exist within {c["name"]} — each with different flood zone, dockage, and insurance considerations. We walk every buyer through the real cost of waterfront ownership here before an offer is ever written.</p>

      <img src="../assets/img/{c["img2"]}" alt="{c["name"]} waterfront" style="border-radius:2px;margin:28px 0;width:100%;height:340px;object-fit:cover;">

      <h2>Frequently Asked Questions</h2>
      <div class="faq">
        <div class="faq-item">
          <div class="faq-q">What's the flood insurance situation like in {c["name"]}?</div>
          <div class="faq-a"><p>Flood zone and elevation certificates vary block-by-block in the Keys. We pull the flood zone and, where available, the elevation certificate for every listing before you tour it.</p></div>
        </div>
        <div class="faq-item">
          <div class="faq-q">Is {c["name"]} a good fit for a vacation rental?</div>
          <div class="faq-a"><p>Short-term rental rules differ by municipality and even by neighborhood in unincorporated Monroe County. We'll confirm current zoning and any licensing requirements for any property you're considering.</p></div>
        </div>
        <div class="faq-item">
          <div class="faq-q">How far is {c["name"]} from the airport?</div>
          <div class="faq-a"><p>Most buyers fly into Miami International or Key West International, depending on which end of the chain they're settling near. We're happy to talk through the drive times for {c["name"]} specifically.</p></div>
        </div>
      </div>
    </div>

    <aside>
      <div class="sidebar-card">
        <h4>Market Snapshot</h4>
        <div class="sidebar-fact"><span>Median Price</span><b>{c["stats"][0][0]}</b></div>
        <div class="sidebar-fact"><span>Days on Market</span><b>44</b></div>
        <div class="sidebar-fact"><span>Active Listings</span><b>—</b></div>
        <p style="margin-top:16px;">Figures shown are illustrative for this prototype and will connect to live FLEXMLS data at launch.</p>
        <a href="../listings/index.html" class="btn btn-outline-green" style="width:100%;text-align:center;">View {c["name"]} Listings</a>
      </div>
      <div class="sidebar-card">
        <h4>Talk to Alexia</h4>
        <p>Ready to explore {c["name"]}? Get a local's honest read before you tour a single home.</p>
        <a href="mailto:hello@seafarerrealty.com?subject={c['name'].replace(' ','%20')}%20Inquiry" class="btn btn-gold" style="width:100%;text-align:center;">Schedule a Call</a>
      </div>
    </aside>
  </div>

  <div class="container" style="margin-top:20px;">
    <h2 style="color:var(--green);margin-bottom:6px;">Explore Other Communities</h2>
    <div class="related-grid">{related}</div>
  </div>
</section>
'''
    return page(f"{c['name']} Real Estate | Seafarer Realty",
                f"Explore {c['name']} real estate — waterfront homes, neighborhoods, and local life in the Florida Keys.",
                "../", body)

for c in communities:
    write(f"communities/{c['slug']}.html", community_page(c, communities))

# ---------------------------------------------------------------------------
# LISTINGS
# ---------------------------------------------------------------------------
listings = [
    dict(slug="waterfront-estate-islamorada", tag="Waterfront Estate", price="$2,495,000",
         loc="Islamorada, FL", beds="4", baths="3.5", sqft="3,120", lot="0.42 acre",
         img="fred-bridge.jpg", img2="freedom.jpg", img3="water.jpg",
         desc="A quietly grand canal-front estate on Upper Matecumbe, built for a boat, a dock party, and a very long dinner outside. Deep water access puts you minutes from backcountry flats and blue water alike.",
         features=["Private dock with 13,000 lb boat lift","Impact windows & doors throughout","Chef's kitchen with waterfront island","Saltwater pool & summer kitchen","Whole-home generator"]),
    dict(slug="luxury-condo-key-west", tag="Luxury Condo", price="$975,000",
         loc="Key West, FL", beds="2", baths="2", sqft="1,410", lot="—",
         img="flagler.jpg", img2="seven-mile-sunset.jpg", img3="beachin.jpg",
         desc="A turnkey Old Town condo two blocks from Duval Street, with a private balcony built for the nightly sunset show. Ideal as a lock-and-leave second home or a licensed short-term rental.",
         features=["Private balcony with harbor glimpse","Deeded parking space","Community pool & hot tub","Walkable to Duval Street & the Seaport","Furnished, turnkey option available"]),
    dict(slug="oceanfront-villa-big-pine-key", tag="Oceanfront Villa", price="$3,850,000",
         loc="Big Pine Key, FL", beds="5", baths="4", sqft="4,006", lot="0.65 acre",
         img="drift.jpg", img2="mangrove-beach.jpg", img3="water.jpg",
         desc="A sprawling Lower Keys retreat set directly on open water, with the kind of privacy and lot size that's increasingly rare closer to Key West. Wraparound decking frames a backcountry sunset every night.",
         features=["300 ft of oceanfront","Wraparound elevated decking","Detached guest cottage","Deep-water dock, no bridges to open water","Whole-property hurricane shutters"]),
    dict(slug="new-listing-marathon", tag="New Listing", price="$1,290,000",
         loc="Marathon, FL", beds="3", baths="2", sqft="2,050", lot="0.28 acre",
         img="causeway.jpg", img2="fred-bridge.jpg", img3="seven-miles.jpg",
         desc="A freshly updated canal-front home minutes from Sombrero Beach — the kind of easy, low-maintenance layout that works equally well as a family home or a well-managed rental.",
         features=["Open-concept living & kitchen","New metal roof (2025)","Concrete dock with davits","Fenced yard, room for a pool","Golf-cart distance to Sombrero Beach"]),
]

def listing_page(l, all_l):
    others = [x for x in all_l if x["slug"] != l["slug"]][:3]
    related = "\n".join(
        f'<a class="related-card" href="{o["slug"]}.html"><img src="../assets/img/{o["img"]}" alt="{o["tag"]}"><span>{o["price"]} — {o["loc"]}</span></a>'
        for o in others
    )
    feats = "".join(f"<li>{f}</li>" for f in l["features"])
    body = f'''
<section class="page-hero" style="height:44vh;min-height:320px;">
  <img src="../assets/img/{l["img"]}" alt="{l["tag"]} in {l["loc"]}">
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">Listings</a> / {l["tag"]}</div>
    <h1>{l["price"]}</h1>
    <p class="lede">{l["tag"]} · {l["loc"]}</p>
  </div>
</section>

<section class="page-body">
  <div class="container">
    <div class="gallery-grid reveal">
      <div class="g-main"><img src="../assets/img/{l["img"]}" alt="{l["tag"]} main photo"></div>
      <div class="g-side">
        <div><img src="../assets/img/{l["img2"]}" alt="{l["tag"]} secondary photo"></div>
        <div><img src="../assets/img/{l["img3"]}" alt="{l["tag"]} additional photo"></div>
      </div>
    </div>

    <div class="page-cols" style="margin-top:20px;">
      <div class="page-main reveal">
        <div class="stat-row">
          <div class="stat"><b>{l["beds"]}</b><span>Bedrooms</span></div>
          <div class="stat"><b>{l["baths"]}</b><span>Bathrooms</span></div>
          <div class="stat"><b>{l["sqft"]}</b><span>Sq Ft</span></div>
          <div class="stat"><b>{l["lot"]}</b><span>Lot Size</span></div>
        </div>
        <h2>About This Home</h2>
        <p>{l["desc"]}</p>
        <h2>Features</h2>
        <ul>{feats}</ul>
        <h2>Frequently Asked Questions</h2>
        <div class="faq">
          <div class="faq-item">
            <div class="faq-q">Is flood insurance required for this property?</div>
            <div class="faq-a"><p>Most waterfront and near-water homes in the Keys carry flood insurance. We'll provide the flood zone and, where available, elevation certificate for this listing during your showing.</p></div>
          </div>
          <div class="faq-item">
            <div class="faq-q">Can I see this home virtually first?</div>
            <div class="faq-a"><p>Yes — ask Alexia for a video walkthrough before booking travel to tour in person.</p></div>
          </div>
        </div>
      </div>
      <aside>
        <div class="sidebar-card">
          <h4>Interested in this home?</h4>
          <p>Get pricing history, HOA details, and a private showing time.</p>
          <a href="mailto:hello@seafarerrealty.com?subject=Inquiry:%20{l['price'].replace('$','').replace(',','')}%20{l['loc'].replace(' ','%20').replace(',','')}" class="btn btn-gold" style="width:100%;text-align:center;">Request a Showing</a>
        </div>
        <div class="sidebar-card">
          <h4>Mortgage Estimate</h4>
          <div class="sidebar-fact"><span>List Price</span><b>{l["price"]}</b></div>
          <div class="sidebar-fact"><span>Est. Down (20%)</span><b>—</b></div>
          <div class="sidebar-fact"><span>Est. Monthly</span><b>—</b></div>
          <p style="margin-top:14px;">A full affordability calculator connects here at launch.</p>
        </div>
      </aside>
    </div>

    <h2 style="color:var(--green);margin-top:60px;">More Homes You May Like</h2>
    <div class="related-grid">{related}</div>
  </div>
</section>
'''
    return page(f"{l['tag']} — {l['price']} | {l['loc']} | Seafarer Realty",
                f"{l['tag']} in {l['loc']}: {l['beds']} bed, {l['baths']} bath, {l['sqft']} sq ft. {l['desc'][:120]}",
                "../", body)

for l in listings:
    write(f"listings/{l['slug']}.html", listing_page(l, listings))

# Listings index (search results stand-in)
def listings_index():
    cards = "\n".join(f'''
      <a class="listing-card reveal" href="{l['slug']}.html">
        <div class="listing-img">
          <img src="../assets/img/{l['img']}" alt="{l['tag']} in {l['loc']}">
          <span class="listing-tag">{l['tag']}</span>
        </div>
        <div class="listing-body">
          <div class="price">{l['price']}</div>
          <div class="loc">{l['loc']}</div>
          <div class="meta"><span>{l['beds']} bd</span><span>{l['baths']} ba</span><span>{l['sqft']} sf</span></div>
        </div>
      </a>''' for l in listings)
    body = f'''
<section class="page-hero" style="height:44vh;min-height:320px;">
  <img src="../assets/img/seven-mile-sunset.jpg" alt="Florida Keys listings">
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="../index.html">Home</a> / Listings</div>
    <h1>All Florida Keys Listings</h1>
    <p class="lede">Every home currently offered by Seafarer Realty, Key Largo to Key West.</p>
  </div>
</section>
<section class="page-body">
  <div class="container">
    <div class="simple-filter">
      <span class="chip active">All</span>
      <span class="chip">Waterfront</span>
      <span class="chip">Luxury</span>
      <span class="chip">Condo</span>
      <span class="chip">Investment</span>
    </div>
    <div class="listings-grid">{cards}</div>
    <p style="margin-top:44px;color:#7c7a71;font-size:14px;">This prototype shows four sample listings. At launch, this page pulls live inventory directly from FLEXMLS.</p>
  </div>
</section>
'''
    return page("All Listings | Seafarer Realty",
                "Browse every current Seafarer Realty listing across the Florida Keys.",
                "../", body)

write("listings/index.html", listings_index())

# ---------------------------------------------------------------------------
# BLOG
# ---------------------------------------------------------------------------
posts = [
    dict(slug="cost-of-waterfront-living", cat="Buying Guide",
         title="What It Actually Costs to Live on the Water in the Keys",
         img="seven-mile-sunset.jpg",
         excerpt="A candid look at insurance, flood zones, and dock permitting.",
         body=[
             "Waterfront living in the Florida Keys is genuinely different from waterfront living almost anywhere else in the country, and the costs reflect it. Before you fall in love with a dock and a view, it helps to understand the three line items that surprise most buyers: flood insurance, wind insurance, and dock or seawall maintenance.",
             "Flood insurance premiums are driven by your flood zone designation and, critically, your elevation certificate. Two homes on the same canal can carry very different premiums depending on how high the finished floor sits relative to base flood elevation. We pull the flood zone and, where one exists, the elevation certificate before you ever write an offer.",
             "Wind insurance in Monroe County is typically a separate policy from flood coverage, and it's priced based on roof age, opening protection (impact windows versus shutters), and construction type. Newer, impact-rated homes routinely see meaningfully lower premiums than older block construction with plywood shutters.",
             "Finally, budget for the water side of the property. Seawalls, davits, and docks all have a lifespan in salt water, and a marine contractor's inspection is worth every dollar before closing on any waterfront home.",
         ]),
    dict(slug="hidden-beaches", cat="Lifestyle",
         title="Seven Hidden Beaches Locals Won't Tell You About",
         img="drift.jpg",
         excerpt="The quiet stretches of sand between the mile markers.",
         body=[
             "The Keys aren't really known for wide sandy beaches — most of the shoreline is rocky hammock and mangrove — which is exactly why the handful of quiet sandy pockets that do exist stay so lightly visited.",
             "Some of our favorites require a short kayak paddle or a walk down an unmarked access path rather than a parking lot, which keeps them wonderfully uncrowded even in peak season. Ask Alexia for the current list — some of these spots move or close seasonally for nesting shorebirds, so a local, current answer beats an old blog post every time.",
             "If you're househunting with beach access on your list, we can also flag which canal-front and oceanfront listings have realistic walking or paddling distance to sand, since 'near the beach' means something different on each island.",
         ]),
    dict(slug="moving-to-florida-keys", cat="Relocation",
         title="A First-Timer's Guide to Moving to the Florida Keys",
         img="flagler.jpg",
         excerpt="What to know before the moving truck crosses the Card Sound Bridge.",
         body=[
             "Moving to the Keys is equal parts exciting and logistically unlike moving anywhere else in Florida. There's really one road — the Overseas Highway — connecting every island, and that single fact shapes everything from grocery runs to hurricane planning.",
             "Start with hurricane season realities: know your evacuation zone, understand storm shutters or impact glass on the home you're buying, and build a real evacuation plan before you need one, not during your first storm watch.",
             "From there, think about which stretch of the Keys actually matches your life. Key Largo suits a Miami commute. Islamorada and Marathon suit families and anglers who want space. Key West suits walkability and nightlife. We're always glad to talk through which island fits before you start touring homes.",
         ]),
]

def blog_post_page(p, all_p):
    others = [x for x in all_p if x["slug"] != p["slug"]][:2] or [x for x in all_p if x["slug"] != p["slug"]]
    related = "\n".join(
        f'<a class="related-card" href="{o["slug"]}.html"><img src="../assets/img/{o["img"]}" alt="{o["title"]}"><span>{o["title"]}</span></a>'
        for o in others
    )
    paragraphs = "\n".join(f"<p>{para}</p>" for para in p["body"])
    body = f'''
<section class="page-hero">
  <img src="../assets/img/{p["img"]}" alt="{p["title"]}">
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">Journal</a> / {p["cat"]}</div>
    <span class="blog-cat" style="margin-bottom:14px;">{p["cat"]}</span>
    <h1>{p["title"]}</h1>
    <p class="lede">{p["excerpt"]}</p>
  </div>
</section>
<section class="page-body">
  <div class="container page-cols">
    <div class="page-main reveal">
      {paragraphs}
    </div>
    <aside>
      <div class="sidebar-card">
        <h4>Talk to Alexia</h4>
        <p>Questions about this topic, or ready to start touring homes in the Keys?</p>
        <a href="mailto:hello@seafarerrealty.com?subject=Question%20about%20{p['slug'].replace('-','%20')}" class="btn btn-gold" style="width:100%;text-align:center;">Ask a Question</a>
      </div>
      <div class="sidebar-card">
        <h4>Newsletter</h4>
        <p>Monthly market insight and island stories, straight from Islamorada.</p>
        <form class="news-form" onsubmit="return false;" style="flex-direction:column;">
          <input type="email" placeholder="Your email address" required style="margin-bottom:10px;">
          <button type="submit" style="width:100%;">Subscribe</button>
        </form>
      </div>
    </aside>
  </div>
  <div class="container" style="margin-top:20px;">
    <h2 style="color:var(--green);">Related Reading</h2>
    <div class="related-grid">{related}</div>
  </div>
</section>
'''
    return page(f"{p['title']} | Seafarer Realty Journal",
                p["excerpt"], "../", body)

for p in posts:
    write(f"blog/{p['slug']}.html", blog_post_page(p, posts))

def blog_index():
    cards = "\n".join(f'''
      <a class="blog-card reveal" href="{p['slug']}.html" style="height:320px;">
        <div class="blog-img" style="min-height:320px;">
          <img src="../assets/img/{p['img']}" alt="{p['title']}">
          <div class="blog-content">
            <span class="blog-cat">{p['cat']}</span>
            <h3>{p['title']}</h3>
            <span class="blog-date">{p['excerpt']}</span>
          </div>
        </div>
      </a>''' for p in posts)
    body = f'''
<section class="page-hero" style="height:44vh;min-height:320px;">
  <img src="../assets/img/mangrove-beach.jpg" alt="Seafarer Realty Journal">
  <div class="container page-hero-content">
    <div class="breadcrumb"><a href="../index.html">Home</a> / Journal</div>
    <h1>The Journal</h1>
    <p class="lede">Island stories, buying guides, and market insight from Seafarer Realty.</p>
  </div>
</section>
<section class="page-body">
  <div class="container">
    <div class="blog-grid" style="grid-template-columns:repeat(3,1fr);">{cards}</div>
  </div>
</section>
'''
    return page("The Journal | Seafarer Realty",
                "Island stories, buying guides, and Florida Keys market insight from Seafarer Realty.",
                "../", body)

write("blog/index.html", blog_index())

# ---------------------------------------------------------------------------
# LEGAL PAGES
# ---------------------------------------------------------------------------
def legal_page(title, heading, html_body):
    body = f'''
<section class="legal-body container">
  <h1>{heading}</h1>
  <div class="updated">Last updated July 2026 · Prototype placeholder text</div>
  {html_body}
</section>
'''
    return page(f"{title} | Seafarer Realty", f"{title} for Seafarer Realty, LLC.", "", body)

privacy_body = '''
<p>Seafarer Realty, LLC ("Seafarer Realty," "we," "us") respects your privacy. This placeholder policy outlines, at a prototype level, the kinds of information a finished privacy policy for this site would cover.</p>
<h2>Information We Collect</h2>
<p>Contact details submitted through inquiry forms, newsletter sign-ups, and general site analytics (pages viewed, general location, device type).</p>
<h2>How We Use It</h2>
<ul>
  <li>To respond to property inquiries and schedule showings</li>
  <li>To send the monthly newsletter to subscribers who opt in</li>
  <li>To improve site content and performance</li>
</ul>
<h2>Third Parties</h2>
<p>We do not sell personal information. Listing data is shared with the MLS as required for syndication once IDX/FLEXMLS integration is live.</p>
<h2>Your Choices</h2>
<p>You may unsubscribe from the newsletter at any time, and may request removal of your contact information by emailing hello@seafarerrealty.com.</p>
<p style="margin-top:40px;font-style:italic;color:#8a887f;">This is placeholder copy for prototype purposes. A finished privacy policy should be reviewed by counsel before launch.</p>
'''
write("privacy-policy.html", legal_page("Privacy Policy", "Privacy Policy", privacy_body))

ada_body = '''
<p>Seafarer Realty, LLC is committed to ensuring digital accessibility for people with disabilities. We are continually improving the user experience for everyone and applying the relevant accessibility standards.</p>
<h2>Conformance Target</h2>
<p>This site is designed with the goal of conforming to WCAG 2.1 Level AA, including keyboard navigability, visible focus states, sufficient color contrast, and descriptive alt text on imagery.</p>
<h2>Feedback</h2>
<p>If you encounter an accessibility barrier anywhere on this site, please contact us at hello@seafarerrealty.com so we can address it.</p>
<p style="margin-top:40px;font-style:italic;color:#8a887f;">This is placeholder copy for prototype purposes. A full accessibility audit is recommended before launch.</p>
'''
write("accessibility.html", legal_page("ADA Accessibility", "ADA Accessibility Statement", ada_body))

ethics_body = '''
<p>Seafarer Realty, LLC and its agents are committed to the professional standards set out in the National Association of REALTORS® Code of Ethics, covering duties to clients, the public, and fellow REALTORS®.</p>
<h2>Duties to Clients &amp; Customers</h2>
<p>Honesty, competent service, and protection of client interests above the agent's own.</p>
<h2>Duties to the Public</h2>
<p>Fair housing practice without regard to race, color, religion, sex, disability, familial status, national origin, sexual orientation, or gender identity.</p>
<h2>Read the Full Code</h2>
<p>The complete NAR Code of Ethics is maintained by the National Association of REALTORS® and available at their official site.</p>
<p style="margin-top:40px;font-style:italic;color:#8a887f;">This is placeholder copy for prototype purposes; link to the official NAR Code of Ethics page before launch.</p>
'''
write("realtor-code-of-ethics.html", legal_page("Realtor Code of Ethics", "REALTOR® Code of Ethics", ethics_body))

print("\nAll pages generated.")
