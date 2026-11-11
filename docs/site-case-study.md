# Case study: rebuilding this site with veyUI

The first landing page was assembled from the Taste Skill kit. It worked, but it read as templated: repeated card layouts, no motion, miniature mock-ups instead of real example pages. So the site was rebuilt by running veyUI's own workflow on veyUI. This note records what was done and, as importantly, what was not verified.

## What the workflow produced

1. **Product story.** Facts, install commands, FAQ, limits and credits were fixed first, from the repository, so every concept shared the same content.
2. **Directions with real examples.** Live public pages were opened (Raycast, Resend, Rive, Screen Studio, Linear, Framer, Dub, Supabase). Vercel redirected to a signed-in area and was not used as a reference. Three directions were proposed: Dark Instrument, Spec Sheet and Concept Shuffle. Two were built (Dark Instrument and Concept Shuffle), as chosen by the owner.
3. **Two complete landing concepts**, each with its own type, palette, composition and motion, hosted locally.
4. **One before and after example.** Slackwater is a fictional tide planner. The same page is shown as typical agent output and as a designed tide dashboard, and it rearranges as you scroll, with five named fixes (type, layout, color, proof, copy). It replaces an earlier row of three example pages that the owner judged poor. The After design was developed from one of the owner's own reference images (a dark telemetry dashboard over a horizon light), studying its principles and executing original code. The reference image is not distributed.
5. **Independent review.** A visual reviewer and a UX and engineering reviewer, both separate from the builders, inspected every version over several rounds, for the landing concepts and again for the before and after example. Material findings were fixed and rechecked before the owner chose.
6. **Selection.** The owner chose "Concept Shuffle", and later approved the before and after example. Only then were they integrated into `site/`.

## The hero, rebuilt on the owner's direction

The first hero opened on a pale "typical agent output" page with three generic cards. Even with annotations it looked like bad AI UI, which is the wrong first impression for a design skill. After two rounds the owner chose a direction: a dark, cinematic hero with a before and after teaser. The built version is a two-column layout (headline and install on the left, a glass panel with the sweeping before and after on the right), a lime light and dot field that follows the cursor, and a dark navigation pill that returns to cream below the hero. Two independent reviewers checked it over three rounds. Their findings were fixed before it shipped, for example the cursor dots colliding with small text, the panel sitting below the fold on common laptop sizes, and ink text that fell half on the dark hero and half on the orange section.

## How the chosen page works

- Plain HTML, one stylesheet and one module. GSAP, ScrollTrigger and Flip are vendored locally. The page makes no third-party requests.
- The full page is readable without JavaScript and under reduced motion. Scroll-driven scenes are an enhancement.
- Lenis was evaluated in the other concept and is not used here. Native scrolling is never overridden.

## What was verified

- Headless Chrome at 1440, 1024, 768, 390 and 320 wide: no horizontal overflow, no console errors, no failed requests, no third-party requests.
- Reduced-motion and no-JavaScript runs.
- Frame sequences of the scroll-driven scenes, keyboard use, install tabs, copy buttons and the FAQ.
- Static checks in CI (`tools/check_site.py`): ASCII only, JSON-LD parses, FAQ markup equals FAQ JSON-LD, local links resolve, social images have the right size.

## What was not verified

- Real GPUs and real phones. Rendering used headless Chrome with software rasterization.
- Safari and Firefox. Only Chromium was tested.
- Real touch input, screen readers and find-in-page.
- Load speed on real networks. Under simulated slow-phone throttling, the largest paint measured about 5 seconds, which is slower than desktop.
- Search ranking or conversion. Nothing here measures either, and the page makes no such claims.

The review records are kept with the studio files outside this repository. They are summaries of what two independent reviewers observed, not a certification of design quality.
