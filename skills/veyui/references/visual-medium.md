# Choose and compose the visual before building its container

Use this for image-led marketing, product illustrations and any brief where the references look substantially more crafted than the generated UI. Read after the reference target, before selecting a card, phone frame or animation. For a functional application, preserve native/accessible controls; do not turn working screens into pictures.

## The decision that generic prototypes skip

A component answers “how can I implement this?” A visual concept first answers “what should the viewer see and understand?” Choose the subject, medium, crop, scale, context and composition before choosing a component. A new border radius cannot repair the wrong subject or medium.

For each visually important section, write one short row in `templates/visual-direction.md`:

**communication job | reference relationship | subject and settled outcome | medium and reason | composition at delivered size | source/permission | compact treatment**.

Keep these rows in the main design brief; do not create a separate approval ceremony or paperwork for every small component. Important rows include the hero, signature proof and any setup/feature scene used to sell the product. Pricing, forms and FAQs can remain clear ordinary UI. Their usefulness is not improved by forced decoration.

## Choose the medium deliberately

| Need | Usually suitable | Failure to avoid |
|---|---|---|
| Atmosphere, believable material, landscape, people, organic light, complex 3D form | Approved photograph, illustration, rendered scene, video or model-generated image after permission | Approximating difficult imagery with gradients, CSS blobs, emoji or a token icon to save effort |
| Evidence of an actual product capability | Accurate project render or screenshot with meaningful fixture data, selectively cropped and art-directed | Invented dashboard fragments, empty account state or generic labels posing as evidence of usefulness |
| Photo/material plus legible precise product details | Hybrid: licensed/approved/generated background or object plus separate actual UI, SVG or HTML overlay | Asking an image model to draw exact interface text, controls, prices or charts |
| Relationship, topology, sequence, data | Designed SVG/HTML/canvas or real UI when precise structure matters | Assuming all code-native graphics are low quality, or replacing a useful diagram with an unrelated photograph |
| User-operated task, navigation, settings or form | Real semantic/native components and actual states | Rasterized controls, decorative fake inputs, misleading click targets |

Images are not automatically better. The delivered composition determines suitability. A screenshot can be a dull rectangle; a carefully authored HTML scene can be excellent. If the selected reference's appeal depends on photography or rendered material, however, a pile of basic controls is not an equivalent substitute. Make that dependency explicit.

## Asset planning must cover the body of the experience

Do not spend the entire visual effort on a cinematic hero and use default cards below it. Inventory the strongest image/proof moments throughout the page. Decide where to reuse one consistent environment, where a distinct crop is enough, and where a new scene is necessary. Reusing one image everywhere is not a coherent visual system unless the crops and narrative genuinely support it.

For each missing important asset, propose its subject, intended placement, medium, aspect/crop needs, protected negative space, lighting/material, allowed text and source route. State which part must stay in code. Batch related image requests into one concrete permission question, with approximate asset/variant count. Image generation is permission-gated even for internal drafts. Do not ask the user to source the assets as the default.

If permission is declined, choose available suitable assets or propose a materially different direction that succeeds without them. If permission is pending or generation/rights are unavailable, continue unrelated work and label the affected scene unfinished. Never quietly substitute low-detail code because asking for imagery is inconvenient. Existing supplied assets are evaluated before asking for more.

## Art-direct a scene instead of decorating a card

Work through these choices in order:

1. **Meaning:** one useful action or outcome; a concrete object/person/data state that makes it legible.
2. **Focal hierarchy:** one dominant subject, bounded support and intentional empty space. Explain why each floating fragment is needed.
3. **Frame and crop:** decide what enters/leaves the frame. A close crop of one meaningful panel often communicates more than a tiny complete app. Avoid arbitrary tilted phones and fake window dots.
4. **Plane and material:** backgrounds, UI and objects need coherent light, depth and edges. Glass is a material decision, not a blur applied to every surface.
5. **Content density:** enough detail to make the scene credible, little enough to read at placement size. Keep important copy and data crisp and large enough; do not fill space with category chips.
6. **Integration:** fit surrounding type, captions, alignment anchors and transitions. Avoid the default `outer card > inner card > icon tile > label > button` when those layers communicate nothing.
7. **Compact version:** recompose or crop deliberately. Define which subject remains and how the story stays understandable. Do not scale an entire desktop scene until its labels vanish.
8. **Settled state first:** render and inspect the still. Add motion only after the frame works; movement cannot rescue an empty story.

Concrete values belong in the project brief after seeing its container and assets: actual scene slot width/height, image aspect, safe crop, typography, insets and layer offsets. Do not invent universal magic percentages. Estimate source proportions honestly, then test the proposed target values in the real render.

## Translate these reference relationships accurately

The maintainer-supplied references establish visual expectations, not templates to clone or palettes to copy:

- **Liquid Brokers:** one integrated dimensional focal object, tight headline hierarchy, restrained supporting fragments. This does not imply every following section should be a dark card with a tiny icon.
- **Fiscal.ai:** photographic atmosphere and product UI share the composition. The lower “How it works” examples have image-bearing scenes with selectively readable UI, followed by outside captions. They are not simply three instructions inside generic input cards. Preserve the relationship while using original content and independently chosen colors.
- **Zentro:** landscape and crafted material support precise UI, with different scales and crops across sections. Product context changes with the communication job; the whole page is not repeated full dashboards in rounded containers.

For another brief, replace these relationships with that project's actual targets. Product UI and native settings require different density and behavior from marketing scenes.

## Worked repair: install → pair → useful result

Submitted concepts for a device-pairing product provide a useful negative example. Source inspection found `Install` represented by an icon/label/button strip, `Pair` by six underscores, and `Review` by category names. In one concept, the setup cards are headings/paragraphs and the prominent dashboard is empty. These observations come from the submitted HTML, not a verified browser render. The defect is explanatory and compositional: the visuals repeat the captions without showing a credible task or result.

Better options, chosen against product truth and the selected reference:

| Moment | Subject and composition to explore | Content and verification boundary |
|---|---|---|
| Install | A deliberate device/app installation scene in the chosen material or photographic world, with an accurately rendered app surface; crop to the useful moment and put the instructional caption outside the scene | Use the real supported Android flow if available. Do not invent a store listing, system permission or installed state. If unavailable, label a conceptual illustration and avoid fabricated OS chrome |
| Pair | One coherent scene showing the relationship between the parent's code and the child's entry/confirmation, with a populated, visibly fictional example or approved real fixture; use two linked regions only when both clarify the action | Verify actual code format and setup sequence. Never publish a real active pairing token. Child permissions remain a distinct factual step, not something an animation implies was silently granted |
| Review | A purposeful crop of a useful populated outcome, such as one accurate event and its contextual view, with coherent sample data and a short caption | Use only supported capabilities and plausible non-sensitive fixtures. A list of “Alerts / Places / Timeline” names does not demonstrate the benefit |

For an image-led reference, consider a consistent series of three art-directed images or hybrid scenes with separate live captions. For a process-led reference, consider one larger story that changes by step, with a usable static/reduced-motion equivalent. For a compact utility brief, a restrained text sequence may be best. Do not mandate the same solution for all projects.

A conceptual product illustration is not proof of actual shipped behavior. If the real UI cannot support the proposed visual, revise the visual or clearly label the proposal; do not fabricate proof for aesthetics.

## Review the weakest important section

Before expanding every concept, calibrate the opening **and the hardest lower-page scene**. Once the full candidate is built, inspect the least convincing important section at actual desktop and compact sizes. Compare it with the relevant reference region, not a reference hero unrelated to that section.

Ask: what is visible beyond the caption? Is the medium as resolved as the reference? Is the useful information readable? Does the section have its own composition while belonging to the same system? Would removing the wallpaper expose an unfinished wireframe? Is there a specific repair that would materially improve it?

Record the actual finding and correction in the normal concept review. Do not average a weak body section away with an impressive hero. Do not declare “asset quality passed” because files exist or because the images are large. If visual inspection is unavailable, mark it unverified. A source-level review can identify omissions but cannot certify alignment, rendering or aesthetic quality.
