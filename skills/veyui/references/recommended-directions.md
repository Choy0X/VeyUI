# Recommend designs the user can actually inspect

Read this during discovery for new UI or a substantial redesign with open art direction. The user does not need a moodboard, screenshots or knowledge of design terminology. Offer three input routes: **recommend directions for me**, **use my references**, or **combine both**. Default to recommending when references are absent; do not stop at asking the user to find examples. Honor an already chosen design or explicit request to skip reference exploration.

## 1. Establish fit from project context

Inspect the existing project before asking. Resolve the product, audience, primary task, platform, data density, brand freedom, content/assets, motion ambition and actual constraints. If the product itself is unknown, ask the smallest consequential question needed to recommend relevant designs. Do not ask the user for fonts, hex codes or mandatory URLs.

Turn context into a recommendation brief: `what must feel or work differently | fixed constraints | open choices | visual ambition | available proof`. Separate a marketing site from the product it promotes. A polished landing page does not establish good desktop information design.

## 2. Find a small set of existing examples

Use offline screen descriptions and source metadata to shortlist candidates first. Then verify a bounded set of live public URLs with available web tools. This planning step is an explicit exception to normal offline-only retrieval. It does not authorize bulk screenshot research, paid services or Mobbin MCP.

- Default to **three meaningfully different directions**, each with **one primary existing live example**. Add one complementary example only when it resolves a separate important choice. Aim for three to six useful links, not a directory dump.
- Prefer the exact public page, working demo or specific product-tour screen that demonstrates the proposed direction. Use a relevant section anchor when available, and tell the user where to look.
- Marketing: link the actual relevant live landing/product page. Web apps: prefer a public interactive demo, playground or focused product tour. Native desktop/mobile: prefer a public official tour or documentation page showing the specific interface, and explicitly label it **tour/screenshots**, not a browser-interactive native app.
- Use component-library demos for a specific control or motion idea. Do not use a decorative component as the sole evidence for an entire app or landing-page direction. A Dribbble/Awwwards listing is a concept/gallery reference unless its actual live site can be opened.
- Match task, hierarchy, density, asset strategy and platform before fame. Do not routinely send the same fashionable three SaaS homepages. An adjacent industry may contribute structure; explain that limited role.
- If local coverage is weak, perform focused discovery for the missing direction. Do not pad the shortlist with irrelevant links to satisfy a count. Report fewer verified examples and the gap when necessary.

## 3. Verify what the link actually proves

Open every proposed primary URL during this planning session. Check the final destination, meaningful content, relevant surface and access conditions. An HTTP 200, search snippet, brand name or remembered appearance is insufficient to establish a usable example. Replace dead, redirected-to-unrelated, login-only or paywalled links with public alternatives when possible. Do not claim access without checking it.

Record `source title | original/final URL | surface/platform | access status | checked date | evidence basis`. Separate:

- **Live page opened:** the endpoint and relevant content were checked. This alone does not establish current pixels or animation quality.
- **Compiled visual description:** the visual lesson comes from a previously reviewed record; identify that basis and note that the live design may differ.
- **Current visual inspected:** the agent actually viewed the relevant rendered surface. Inspect only a small relevant region when necessary; no mass screenshot ingestion.
- **Motion observed:** the agent actually watched the relevant sequence. Text saying “animated” does not qualify.

The user can open the existing page directly without the agent loading all its screenshots into context. When current visual inspection is unavailable, give the verified public link and state the basis of the proposed lesson honestly. Do not assert current fonts, geometry or motion from text extraction. If all network verification is blocked, provide local proposals or clearly labeled unverified leads, explain the gap and continue unaffected planning; never call those links verified/live-reviewed.

## 4. Present a concrete direction board before building

Use `templates/direction-shortlist.md`. Each direction must include:

1. A descriptive name based on the actual design idea, not just “modern,” “clean” or “premium.”
2. A clickable **View existing example** link with the source name and access type.
3. The exact page section/screen to inspect and the visual or UX relationship it illustrates.
4. Why this fits this project's audience, task, proof and constraints.
5. What to adapt: composition, hierarchy, type character, density, geometry, material, assets or motion—with observations distinguished from proposals.
6. What changes for this project: its own content, platform conventions, identity and independently chosen palette. Do not copy the source brand or palette by default.
7. The principal tradeoff and asset/implementation requirements, including proposed image generation requiring permission.

Recommend one direction with a project-specific reason. Let the user choose A/B/C, name aspects to combine, or delegate the choice. Do not ask for a choice among bare labels without clickable examples. Do not silently assume that no answer means approval. If selection was already delegated, make the reasoned choice and continue without another approval request.

Reference selection settles the inspiration territory, not approval to replace the project. Record the chosen sources, adopted relationships, excluded traits and remaining freedoms. If the user chooses one territory, create three genuinely different complete concepts within it. If they explicitly ask to explore all territories, map the three concepts to those territories. A requested hybrid must be composed coherently and later rendered; it is not permission to collage unrelated sections.

## 5. Keep two kinds of links distinct

The planning board links to **existing third-party examples**. The later concept gallery links to **veyUI's generated runnable candidates**. Both are required when this recommendation route applies; one cannot substitute for the other.

For every generated concept, retain its primary existing-example link and a short explanation of the adaptation in the review notes/gallery, alongside its own direct preview URL. Keep that explanation outside the product UI. Review the actual generated candidate against the selected relationships and show concrete differences rather than claiming it matches because a famous URL is attached.

Continue the normal isolated-build, rendered-review, hosted-preview and selection workflow. Do not present external examples as prototypes you built, a screenshot as an interactive app, or reference preference as final implementation approval.

## 6. Keep the process efficient

Do this once per unresolved design direction, not for each button or refinement. Reuse the chosen brief and checked sources during the project; refresh if the link fails, the user changes direction or a current-source claim requires it. Normal implementation retrieval stays offline. Exact edits, audits and an already approved concrete design do not require a fresh inspiration interview or shortlist.
