# Natural Wellness Website Audit

Audit date: 19 August 2026

## Executive summary

The public Natural Wellness website contains valuable corporate, manufacturing and product information, but it is carrying multiple generations of legacy content and a dated WordPress information architecture. The largest issue is not simply visual design: the site currently under-sells the company’s present B2B manufacturing proposition and exposes content that can reduce trust, including template filler, historical metrics, old certification standard revisions, old news and duplicated site generations.

The lightweight redesign in this repository focuses the website on Natural Wellness as a research, formulation, white/private-label and contract-manufacturing partner.

## Key findings

| Area | Current issue | Risk / impact | Redesign response |
|---|---|---|---|
| Information architecture | Deep multi-level navigation across About, Awards, Products, Services, Media, Opportunities, CSR and Contact | Buyers must assemble the company story themselves | Consolidate around Capabilities, Products, Quality, About and Contact |
| Duplicate legacy architecture | Both root pages such as `/about/`, `/contact/` and newer `/wp/index.php/...` pages remain publicly discoverable | Duplicate/canonical confusion and inconsistent content | Pick one canonical production architecture and redirect retired URLs |
| Company profile | Page contains stock-theme filler text plus an Envato email and Australian phone number | Immediate credibility problem | Remove template content entirely |
| Freshness | Homepage's featured gallery/latest news is still centered on 2016 content | Makes an active manufacturer look dormant | Replace with current case studies/news or remove the module until maintained |
| Business proposition | Current company profile publicly emphasizes 200+ products, white label, private label and contract manufacturing, but the legacy site does not make this the primary conversion path | Missed B2B enquiries | Make these services part of the opening proposition and enquiry flow |
| Metrics | Legacy company profile says 30+ clients, 24 awards and 12 certifications; current company profile elsewhere describes a substantially larger/current portfolio | Conflicting public story | Use only management-approved current metrics |
| Product catalogue | Old pages include specific products and health/therapeutic claims | Claims, availability and registrations may have changed | Treat legacy products as archive material until Regulatory/QA revalidates them |
| Certifications | Page repeats the certificate list twice and cites old revisions such as ISO 9001:2008, MS 1900:2005 and MS 1500:2009 | A current manufacturer should not appear to rely on obsolete certificate information | Publish only current certificate names, numbers, scopes and validity dates after QA confirmation |
| Copy quality | Many pages contain awkward grammar and generic marketing copy | Reduces perceived technical credibility | Rewrite in concise B2B language while preserving approved technical meaning |
| Lead capture | Existing Contact form is generic | No qualification for private label / custom formulation / contract manufacturing leads | Ask need, company, target market, category, quantity and product brief |
| Image system | Photography/assets largely date from 2014–2016 and use JPG/PNG files | Larger payloads, mixed visual quality | Curate approved originals, create AVIF/WebP derivatives and responsive sizes |
| Mixed content | At least one legacy company-profile media reference is served with an `http://` URL | Avoidable security/browser warning risk | Self-host HTTPS assets in production |
| Maintenance | Legacy careers content itself includes web maintenance / web developer responsibilities while much of the site remains stale | Strong sign the old CMS process is not producing current output | Use a simpler site architecture plus clear content ownership/governance |
| Privacy/measurement | No modern measurement/privacy architecture is evident in the public copy | Harder to govern marketing technology cleanly | Add only approved analytics, consent and privacy content in production |

## Current content that is still valuable

### Corporate proposition

- Malaysian pharmaceutical and wellness manufacturing
- Research, development and formulation
- White label and private label
- Contract manufacturing
- Manufacturing, marketing and distribution
- OTC/dietary supplements
- Pharmaceuticals
- Nutraceuticals and cosmeceuticals
- Health food
- Biopharmaceuticals
- Shariah-compliant / halal positioning

### Existing service journey

The legacy homepage already contains a useful end-to-end idea:

Research / R&D → Formulate → Manufacture → Distribute → Market

The redesign keeps this concept but presents it as one coherent sales journey instead of sending visitors through many independent pages.

### Manufacturing / warehouse themes worth retaining

- GMP-controlled production environment
- Quality operations and batch control
- Temperature/humidity-controlled storage where applicable
- Contract-manufacturing capability
- Private-label non-prescription pharmaceutical capability referenced on the GMP page

All regulatory wording should be re-approved before production publication.

## Content requiring verification before launch

### Certifications

The current public certificate page lists:

- Ministry of Finance registration / Bumiputera status
- BioNexus
- MS 1900:2005
- MS 1500:2009
- GMP (PIC/S)
- ISO 9001:2008

Do not copy these revisions into the final production site as if they are current. Ask the QA/Regulatory team for current certificate PDFs, scopes, certificate numbers, issuers, issue dates and expiry/renewal dates.

### Products and therapeutic claims

The old catalogue contains product names and claims across Natural, OTC, Islamic Medicine and Cosmetic sections. Production migration should reconcile each product against:

- Current portfolio status
- MAL / NPRA registration where applicable
- Current approved indication/claim copy
- Current artwork and packaging
- Current manufacturing status
- Whether the product is available for white label/private label

### Client references

The current Natural Wellness company profile publicly cites major client names. Before the production site displays client logos, confirm trademark/logo usage permission. Plain-text references can also be reviewed by management.

### Leadership

The legacy site contains long bios for Dr. Amr Yacout and Shahnas Bt. Oli Mohamed. Confirm the current leadership roster, titles, biographies and portraits before launch.

## Proposed production sitemap

### Home
- Clear positioning
- White/private label and contract manufacturing
- Capability journey
- Product categories
- Trust/quality section
- Markets / credibility
- Qualified product enquiry

### Capabilities
- Research & Development
- Formulation
- Regulatory / product development support, if approved
- Manufacturing
- Quality operations
- Warehouse / fulfilment
- Commercialisation support

### Products / Solutions
- Natural / nutraceutical
- OTC
- Cosmeceutical
- Health food / beverage where applicable
- Islamic / Shariah-compliant portfolio if still an active commercial category
- Private-label catalogue gated or downloadable if management prefers

### Quality
- Current certificates
- GMP / PIC/S explanation
- Quality systems
- Halal / Shariah compliance
- QA/QC process

### About
- Group structure
- Company history
- Leadership
- Markets
- R&D / patents / innovation, once verified
- CSR

### Contact / Start Your Product
- Enquiry type
- Company
- Country / intended market
- Product category
- Dosage form
- Custom formulation vs private label
- Estimated volume
- Target launch date
- Contact details

## Redirect / SEO migration plan

When replacing the WordPress site, create 301 redirects from old indexed pages to the closest new canonical destination. Examples:

- `/wp/` → `/`
- `/wp/index.php/company-profile/` → `/about/`
- `/about/` → `/about/`
- `/wp/index.php/our-products/` → `/products/`
- `/wp/index.php/manufacture/` → `/capabilities/manufacturing/`
- `/wp/index.php/formulate/` → `/capabilities/formulation/`
- `/wp/index.php/warehouse/` → `/capabilities/warehouse/`
- `/wp/index.php/certifications/` → `/quality/`
- `/wp/index.php/about-gmp/` → `/quality/gmp/`
- `/wp/index.php/contact/` and `/contact/` → `/contact/`

Before launch, export the full WordPress URL list and build a complete redirect map so existing search equity and external links are not discarded.

## Lightweight technical direction

The preview intentionally proves that the public-facing corporate site does not require a heavy frontend stack.

Recommended production options:

- Static site generator or pre-rendered framework only if content-management needs justify it
- CDN delivery
- Responsive AVIF/WebP assets
- Minimal client JavaScript
- System/local brand fonts
- Server-side or managed form endpoint
- No unnecessary plugins
- Explicit image dimensions
- Cache immutable assets aggressively
- HTML compression + Brotli/Gzip at CDN

A CMS can still sit behind a static frontend if the marketing team needs content editing. The main goal is to avoid rebuilding another plugin-heavy WordPress installation that becomes difficult to keep current.

## Governance recommendation

Assign an owner and review cadence for each content class:

- Marketing: homepage, services, case studies, news
- Regulatory/QA: certificates, product claims, registrations
- HR: careers
- Management: company metrics, leadership, markets, client references
- IT/vendor: uptime, forms, security, redirects, dependencies and performance

Quarterly content review plus immediate review when a certificate/product/leadership fact changes will prevent the same freshness problem recurring.
