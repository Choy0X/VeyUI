# Motion as state and story

Use one coherent motion system. For web marketing, the bundled foundation supplies actual entrance, hover, moments, scene and effect implementations. This module covers interaction decisions across web and native runtimes. Its prescriptions are original guidance; it does not redistribute a third-party transitions library.

## Motion contract

Before animating, name `purpose | trigger | persistent object | initial state | settled state | properties | duration/easing or spring | interruption | reduced-motion behavior | evidence`. A motion decision must explain feedback, continuity, hierarchy or narrative. Repeated task feedback stays efficient; expressive marketing can hold a meaningful payoff longer.

Use the existing semantic tokens first. When absent, propose an initial scale such as immediate feedback, short control transition, surface transition and narrative beat. Choose exact values by distance, frequency and reading time; a reasonable initial web trial is roughly 100–180 ms for small feedback, 160–260 ms for surfaces and 240–400 ms for larger spatial changes. These are starting hypotheses, not universal requirements or measurements from shipped references. Avoid artificial delays before accepting input.

Prefer CSS for simple state feedback; use an installed motion engine for coordinated layout, exits, springs or gestures. Native APIs preserve host expectations. Avoid adding several engines. Use transform/opacity when suitable; measured size changes may be justified, but profile them and avoid distorting text. Never `transition: all`.

## Choose by relationship

| State change | Construction | Failure to check |
|---|---|---|
| Button hover/press | Subtle surface/contrast change and optional tiny press displacement | Moving hit target, missing keyboard feedback, sticky hover on touch |
| Anchored menu | Origin at trigger, brief entrance, prompt exit; collision-aware placement | Wrong origin after flipping, focus moved before the surface exists |
| Modal | Stable backdrop and clearly elevated content; focus trap and restoration | Background remains interactive, exit unmounts early, scroll position jumps |
| Side panel | Spatial origin from its attached edge; preserve work context | Content under overlay receives input, resize clobbers selection |
| List/detail navigation | Consistent forward/back direction or shared object continuity | Scroll/focus lost, history broken, direction reversed in RTL |
| Tabs/segmented controls | Selection updates immediately; indicator and content remain coherent | Animation completion drives selection, repeated keys lose state |
| Accordion | Content-aware expansion, stable header and chevron | Clipping focusable content or springing to an incorrect cached height |
| Number/value update | Preserve width/alignment or reserve sensible space; readable final value | Units detached, decimals jitter, repeated announcements |
| Text/icon replacement | Stable slot and truthful state; retain semantic control identity | Two announced labels, overlap, stale value after interruption |
| Checkbox/switch | State change immediately, optional brief visual travel | Overlong overshoot suggests uncertainty; visual state differs from data |
| Loading to result | Preserve expected geometry; show progress only when known | Skeleton changes layout, infinite spinner after failure |
| Validation failure | Local message and correction path; restrained optional emphasis | Shake as the only signal, error disappears before correction |
| Success | Confirmation at the action/result; optional brief emphasis | Confetti for routine work, false success before persistence |
| Toast/banner | Clear stacking, readable lifetime, pause/dismiss where needed | Covering primary actions or losing critical information |
| Reorder/drag | Lift selected object, neighbors make space, stable drop target | Layout teleports, no keyboard path, failed save loses original order |
| Streaming output | Stable readable text, meaningful progress, stop/cancel | Animating every word disrupts reading; fake reasoning or fabricated progress |
| Hero/story entrance | Coordinated hierarchy with usable copy/action from the start | Flash of hidden content, long wait, every section repeating one reveal |
| Scroll narrative | Bound the scene and preserve normal page control | Scroll hijacking, inaccessible content, mobile performance collapse |

## Deliver interaction motion, not just page entrances

For a request for modern expressive motion, implement it in the relevant product interactions: anchored menus, dialogs, active/selected indicators, changing values/content and pending/result feedback. Scope choices to what exists in this product. A hero reveal plus static native controls does not fulfill that request. Use the actual compatible Motion package when the user requests it; for other tasks use the existing engine or an appropriate native API. A library import, storyboard or CSS token is not proof the interaction is animated.

Keep a compact implemented map: `component/state change | actual API/file | enter | exit/reverse | interruption | reduced-motion behavior | observed evidence`. Check Component craft for stable control anchors, text fit, dialog layering and field variants. Finish geometry first. Do not animate the whole page on a local selection or stretch labels to morph a surface.

## State correctness precedes animation

Drive visuals from authoritative state. Keep exiting content mounted only as long as needed; remove it from interaction appropriately. Do not rely solely on `transitionend` for business state because reduced motion, interruptions and unmounting may skip it. Cancel stale timers, requests and animation work. Rapid toggle/open-close input must settle to the latest intent. Preserve focus, selection and scroll through resizing and navigation.

Reduced motion must keep content, outcomes and actions available. Replace spatial/continuous decorative movement with a meaningful resting state or restrained immediate feedback. Pause nonessential offscreen/background activity. Provide controls for relevant long-running autoplay and prevent sensory overload. Do not assume silence means reduced motion.

## Rehearsal

Observe opening, mid-transition, settled, reverse and interrupted states. Check rapid repeated input, slow data, long labels, resizing, keyboard, touch, reduced motion and returning to the page. Capture temporal evidence for motion claims; a screenshot cannot verify timing. For a staged demo, use Product demonstrations and separately test actual controls. Inspect the final page, not only a component playground.
