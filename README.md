# Natural Wellness Group — Lightweight Website Redesign

A lightweight static redesign of the existing Natural Wellness website, prepared as a client-approved preview and migration direction.

## Preview architecture

- Plain HTML, CSS and a tiny amount of vanilla JavaScript
- No frontend framework
- No external font files
- No analytics or tracking in the preview
- Responsive desktop/mobile layout
- `noindex,nofollow` while this is only a preview
- Enquiry form prepares an email to the company's published enquiry address

## Why the site was restructured

The current public website has useful company history and technical content, but its information architecture is fragmented across many old WordPress pages. The redesign turns the site into a clearer B2B manufacturing journey:

1. Value proposition
2. Research / formulation / manufacturing / distribution / commercialisation
3. Private label, white label and contract manufacturing
4. Product capabilities
5. Quality and compliance
6. Company credibility
7. Qualified product enquiry

See [`AUDIT.md`](AUDIT.md) for the detailed content and UX audit.

## Asset strategy

For the first GitHub preview, approved legacy images are referenced from the existing Natural Wellness media library so the repo stays extremely small. The discovered asset inventory is in [`ASSET-MANIFEST.md`](ASSET-MANIFEST.md).

Before production migration:

- Download original source images from the approved media library
- Remove duplicates and unused theme/plugin assets
- Convert photography to AVIF/WebP with responsive fallbacks
- Keep the brand mark as SVG/PNG as appropriate
- Self-host all production assets
- Add explicit width/height metadata to prevent layout shift
- Replace or reshoot low-resolution 2014–2016 photography where appropriate

## Content safeguards

The existing website contains old therapeutic/product claims, old certificate standard revisions, historical metrics and old leadership material. This preview deliberately avoids presenting those as newly verified facts.

Before going live, Natural Wellness should confirm:

- Current product catalogue and MAL registrations
- Current certificate numbers, standards, issue/expiry dates
- Current company metrics and market coverage
- Current leadership team and titles
- Current client list and permission to display client logos
- Current manufacturing approvals/capabilities
- Current phone numbers, emails and responsible departments

## Production launch checklist

- [ ] Replace remote legacy images with optimized local assets
- [ ] Remove `noindex,nofollow`
- [ ] Connect enquiry form to approved CRM/email workflow
- [ ] Add spam protection to enquiry endpoint
- [ ] Add Privacy Policy and any required consent language
- [ ] Add analytics only after consent/measurement plan is approved
- [ ] Confirm metadata, Open Graph image and favicon set
- [ ] Generate sitemap.xml and robots.txt
- [ ] Add structured Organization / LocalBusiness data where appropriate
- [ ] Validate all product and regulatory copy
- [ ] Validate all certificates and quality marks
- [ ] Validate client logo usage permissions
- [ ] Run accessibility, performance and browser QA
- [ ] Point the production domain only after stakeholder sign-off

## Source material reviewed

Primary public sources used for the preview include the existing Natural Wellness website (`mynaturalwellness.com`) and the current Natural Wellness Group of Companies LinkedIn company profile. The old site remains the source of the reused visual assets.
