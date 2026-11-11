# Planning protocol

Read this before drafting any UI plan. Use it for a new interface, redesign, shared component change, or review. Load Quality contract first, preserve its established preferences, and ask only for missing project facts. Keep one decision record. Link the selected design from the implementation plan if the repository keeps them in separate files.

## 1. Discover the project

| Inspect | Record |
|---|---|
| Project instructions, product docs, design system, brand assets, approved references | Audience, job, desired outcome, brand constraints, and the references that govern this surface. Reuse compiled reference descriptions; inspect newly supplied images or clips only when their extraction is part of the task. Name the rules they contribute and distinguish observed values from proposed ones. |
| Entry routes or screens, data and action handlers, navigation and return paths | What the product actually supports, including the primary action and destination, prerequisite data or permissions, and current success and failure behavior. |
| Running UI and affected shared components | Baseline screen, width or device, state, and concrete issues. Identify consumers of shared tokens and components. Record evidence gaps if the runtime cannot be inspected. |
| Stack, asset sources, environments, tests, release requirements | Existing components and motion APIs, supported devices or windows, available test commands, dependencies, and release constraints. |

Write a short evidence ledger with **fact or unknown | source | consequence**. For consequential unknowns, record **decision needed | owner | affected scope | fallback or unblock condition**. Group independent questions when the user's input is needed. Mark a delegated judgment as a proposed decision and give the reason. Avoid treating a user's preference for speed as evidence about current behavior.

Before choosing a visual structure, use Design coaching and a compact offline `brief` to connect the task to observed anatomy, documented transitions and explicit target decisions. Name the tradeoff and the check for each risky choice.

## 1a. Discover the content opportunity

For a public site, use [Product story](product-story.md) before fixing page order. Map the relevant whole project, trace promising capabilities beyond the current landing page and record what is actually available. Identify the audience's strongest supported benefits, missing proof and buying objections. Draft real narrative alternatives and full working copy; do not preserve weak headings or onboarding-heavy order by default. Keep product behavior/CMS contracts intact while improving the marketing argument.

## 1b. Recommend references instead of demanding them

Apply [Recommended directions](recommended-directions.md) before freezing composition. Offer agent recommendations, user-provided references or a combination. With no references, automatically prepare three tailored directions with existing, checked public example links, specific regions to inspect, transferable traits, project adaptation and tradeoffs. Present a recommendation and a concrete choice before concept construction unless selection is already delegated. Use [Direction shortlist](../templates/direction-shortlist.md); a mood label or generic inspiration-site homepage is not sufficient.

This limited source-link verification is allowed even though implementation reference retrieval is normally offline. Do not load hundreds of source screenshots. Reference choice and later generated-concept choice are separate decisions; preserve prior approvals and explicit delegation. Once the territory is chosen, build the three complete hosted concepts automatically. Each must retain an existing-example link as well as its own preview link.

## 2. Compare directions before choosing

Use Art direction before locking the page structure or visual tokens. Distinguish hard constraints, defaults, user-approved freedom, and agent proposals. Develop verified product content with composition. Name the complete page or task scope each candidate must finish. Summarize the visual hypothesis, reference observations, concrete type/color/geometry choices, and asset/motion strategy. A section list plus accessibility and implementation rules is not a resolved visual design.

Read Automatic concept delivery and Reference calibration before the Concepts and prototypes reference. Concept creation and preview hosting are mandatory default tasks for material redesigns, not questions to ask the user. Use the Concept adaptation and redesign reference for existing interfaces or imported concepts.

For a new or substantially redesigned surface with open visual choices, automatically build and host three materially different high-fidelity options unless the user specifies a count. Vary the composition, flow, interaction model, or visual story. Use the same evaluation criteria for all candidates. State the main benefit, drawback, and evidence for the recommendation. For a fixed, narrow change, give the concrete proposal and rationale.

Apply Craft, Visual system, Component selection and Motion design during this phase. Record the actual composition, control and state-change decisions. Explain why the approved design reuses, extends, or replaces existing patterns. Keep a single design system and track any intentional exceptions.

For new or materially changed layouts, show a representative annotated frame, wireframe, or ordered layout with explicit dimensions or token references where they matter. Cover the narrow and wide compositions or the native equivalents. If visuals cannot be rendered during planning, use a structured layout labeled specification only. Record the blocker and defer final visual selection. Do not treat the specification as a visually reviewed candidate. Image generation, including concept frames, follows the separate approval gate in the main skill.

## 2b. Resolve imagery and supporting scenes before construction

For image-led references or staged product proof, read `visual-medium.md` and add its section-level rows to the main brief. Specify the medium for the opening, signature proof and hardest supporting scene before choosing components. Asset planning must include setup/features when their visual quality matters, not just hero and closing backgrounds. Batch concrete requests for any model-generated assets and wait for explicit permission for those calls. Continue unaffected work. A missing defining asset is a dependency, not permission to substitute generic cards.

Calibrate the opening and hardest supporting scene at actual wide/compact placement sizes before expanding all candidates. This is internal work, not an extra mandatory user-approval stop. The complete concepts still need normal hosted review and selection.

## 3. Write the design contract

Apply [Seven craft passes](seven-craft-passes.md) in the same brief. Before construction, name the screen’s dominant task/area and action hierarchy, spacing relationships, text/color roles, content and proof sources, component geometry/materials, and motion anchors with enter/exit and reduced-motion behavior. A token list needs these relationships to become an implementable design. Scope this record to the actual task and preserve settled choices.

Give each material requirement a short ID. Use the following sections at the detail needed for the scope.

| Section | Decisions the implementer needs |
|---|---|
| Outcome and scope | Name the audience, primary task or conversion, successful result, affected entry points, and scope boundaries. Trace a primary CTA or action to its real route, event, or handler. Record the chosen approach, the decisive tradeoff, and any major assumptions. |
| Flow and states | Describe the trigger, current state, user action, next state, and recovery. Select applicable default, loading, empty, populated, error, offline, permission, destructive, and success states. Specify navigation, focus, persistence, interruption, and recovery when they affect behavior. |
| Layout and visual system | Set the screen or section order, shared alignment edges, hierarchy, density, and semantic token choices for color, typography, spacing, sizing, shape, and focus. Define how the composition reflows or changes navigation across actual target widths or window classes, with long content and larger text where relevant. |
| Components, data, and copy | Map major elements to existing or new components, data sources, and actions. Specify critical labels, validation and feedback, any library change, and important product claims. Name what can be verified in the project. |
| Assets and motion | List each material asset's source or approval state, placement, crop, and fallback. Storyboard significant motion with trigger, phases, timing or tokens, end state, mobile or native behavior, interruption, and reduced-motion behavior. Agree on asset or performance budgets when they affect the direction and name how to measure them. |
| Accessibility and release evidence | Define relevant keyboard, touch, focus, semantics, contrast, reflow, reduced motion, and platform checks. For each critical requirement, name the setup, interaction or measurement, expected result, target runtime, and evidence to capture. Record device, data, tool, or access gaps. |

Choose the right emphasis:

- **Marketing** — For each material section, name the job it does, message, product evidence, and next action. Specify the opening composition, the real CTA destination, responsive image treatment, and any signature motion with a usable static fallback.
- **Product** — Define the primary path plus alternate and failure paths. Give states an action or recovery where appropriate. Set component anatomy and variants, data density, keyboard or touch behavior, and adaptive navigation. Include shared or downstream surfaces affected by the change.
- **Native** — Pin screen sizes or window classes, input methods, system back, insets, text scaling, semantics, and motion preferences relevant to the change. Distinguish simulator coverage from checks that require a physical device.
- **Targeted change** — Record the exact current and expected behavior or token, affected consumers, smallest scope, and check that would catch a regression. Fold this into the existing plan or use a short brief. Preserve an exact decision the user already authorized.

Turn vague intent into checkable behavior. For example, replace “make it adaptive” with “on compact widths Back returns from detail to the list with its scroll position restored. On expanded widths both panes stay visible and the selection persists through resizing.” Replace “make the hero cinematic” with a named sequence, entry and settled frames, when the CTA is available, and what the visitor sees under reduced motion. Use these examples as patterns and derive the actual behavior from the project.

## 4. Approve, sequence, and review the work

For exact small changes covered by the main skill's compact path, keep the existing approval and verify the scoped change. Use the following design and implementation approvals for new or materially changed work.

1. First present the hosted, inspected alternatives for selection unless selection is already explicitly delegated or a concrete design approved. Keep application source unchanged until that boundary is satisfied. Present the chosen direction as a concrete brief with the representative view, the key tradeoff, and open decisions. Use the concept-selection boundary; do not add a second approval for an unchanged selected design. Record what the user approved or delegated and which version or scope it covers. Approval of an overall visual direction leaves unresolved material choices open. Preserve approval already given and do not ask again for an unchanged decision. Make the next review concrete before pausing. Asset generation has its own authorization.
2. When implementation is requested, write the integration plan after concept selection or explicit delegation. Map requirements to ordered tasks. For each task record **requirement IDs | exact existing or proposed files/screens | prerequisites and interfaces | change | verification and expected result**. Verify existing paths and commands in the repo. Separate proposed paths and steps from confirmed ones. Specify a visible, independently verifiable result per task. Prefer a representative end-to-end slice before replicating it.
3. Mark blocking decisions with an affected task and an explicit unblock condition. If there is an approved fallback, record where it applies. Continue unaffected work if authorized. Reopen only the part of the design affected by a new material decision. Keep intentional deferrals visible at handoff.
4. Self-review before implementation. Trace every critical requirement to a task and a concrete check. Check the primary route and recovery, narrow and wide layouts, input and motion variants, data and asset dependencies, and any approval gates. An implementer should be able to answer what changes, where it changes, and what proves it works. Resolve any placeholder that could change the primary flow, design, or readiness before its dependent task starts.

## Planning completeness gate

Before writing the full candidate, resolve these in one compact project record. Inspect code and prior decisions first; missing evidence produces a targeted question or a labeled assumption, not a ten-question ritual.

| Required decision | What must be concrete |
|---|---|
| Product job | Actor, trigger, task and observable successful outcome |
| Scope/preservation | Actual routes/screens, data/actions, CMS and shared consumers that must survive |
| Audience/context | Familiarity, frequency, risk, input methods and content volume |
| Visual territory | Recommended or supplied directions, checked existing example links, chosen traits, target identity freedom and unacceptable current defects |
| Three directions | Organizing idea, complete scope and differences in composition/identity/appropriate UX |
| Content | Cross-project feature evidence, ranked customer benefits, actual narrative angles and complete copy/proof; release/plan limits and asset dependencies |
| Visual medium | Subject/outcome, image/capture/code/hybrid choice, composition and permission for the hero and important supporting scenes |
| Typography/geometry | Concrete roles, line lengths, gutters, alignment, density, controls, radii and material hierarchy |
| Color | Target semantic palette and state pairs; independent from source palette |
| Interaction | Primary/alternate/recovery flows, focus, persistence, selection and pending/error behavior |
| Motion | Actual sequence, timing intent, interruption and reduced-motion composition |
| Foundations | Existing components versus justified additions; real framework/version constraints |
| Adaptation | Wide/compact or native window classes, long text, keyboard/IME and accessibility variants |
| Delivery | Isolated location, actual hosting/runtime route, gallery and preview lifetime |
| Acceptance | Rendered views and interactions that would falsify the design; critical unresolved dependencies |

Do not freeze a page order first and decorate it later. Resolve content, proof and composition together. Do not turn assumptions such as “no new dependency,” “no imagery,” “same font,” “all static” or “only two views” into constraints without evidence. An execution plan can name pending creative choices, but it cannot present them as approved.

Proceed autonomously with reversible exploration once the project facts support it. The choice should concern actual finished, inspected concepts. Reuse an explicit delegated selection and continue implementation when authorized.
