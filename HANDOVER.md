# Handover: effmarvel.com portfolio

Started 22 November 2026 in the Rezzo project. Read this first in any new project.

## Who and what
- Owner: Marvelous Effiong (GitHub Effmarv). Not a terminal user: give ONE step at a time, explained very clearly. Secrets go into services, never into chat.
- Framing: "product founder who builds with AI". Light colours.
- Case studies: TAVOLA.VIP (tavola.vip, event planner software, repo Effmarv/Tovola.vip, screenshots taken from its /demo run locally), Rezzo (rezzo.co.uk, UK booking + shop link, £9/month, no commission), LastPrice.ng (Nigerian WhatsApp shop link, free / Pro ₦2,500), Lions Vogue (lionsvogue.com, Nigerian nightlife ticketing with QR tickets).
- Product repos: Effmarv/rezzo, Effmarv/Lastprice.ng, Effmarv/lions-vogue.

## How the site works
- Plain HTML/CSS in `public/`. Case study text lives in `src/build.py`: edit it, then run `python3 src/build.py`.
- Hosting: Cloudflare (free), using `wrangler.jsonc` to serve `public/` with no build command. Domain effmarvel.com was bought on Cloudflare.

## Still to do
1. Cloudflare: Workers & Pages, then Create, then import this repo (no build command, deploy command `npx wrangler deploy`), then add the custom domain effmarvel.com.
2. Email: Cloudflare Email Routing so hello@effmarvel.com forwards to the owner's Gmail.
3. Replace the drawn phone mock-ups on /lastprice/ and /lionsvogue/ with real phone screenshots from the owner.
4. Add real numbers to each "Results so far" section. Never invent them.
5. Add the LinkedIn URL (the contact button on the homepage marked data-todo="linkedin").
6. Add an og:image (public/img/og.png is referenced but doesn't exist yet).
7. tavola.vip: owner chose a case study (done). Check whether tavola.vip is actually live; the Visit button links there.
