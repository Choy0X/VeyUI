# Design coaching inside the skill

Use this during material design and redesign. The skill teaches through selected examples, explicit decisions, construction, critique and correction in the current context. It does not train model weights or require a separate dataset, paid reference service, MCP, or new image lookup.

## Build a compact working brief

Run `scripts/design_library.py brief "task and difficult state" --platform web|desktop|mobile`. It returns reviewed screen anatomy, a relevant documented flow when present, and original decision guides. Default maximum is 7,500 characters. The narrower `search` command remains available at 5,000. Do not load every record or every specialist reference.

Read the evidence labels. A screen establishes visible arrangement. A publisher flow establishes what the publisher documents. A decision guide proposes what to build and verify. These layers answer different questions; none proves conversion, usability or performance for the target product.

Choose a structural lead that fits the user's task, not the most famous brand. Use complementary references only for a named compatible need. Reject mismatched density, navigation, platform conventions, risk or audience. A popular product is a precedent to examine, not universal authority.

## Turn examples into decisions before implementation

For each important decision, write one concise record:

**task/constraint → observed relationship → target choice → reason/tradeoff → rendered or interaction check**

Example: a plan-selection reference places billing cadence above comparable plans. For the target, keep cadence above the comparison, align billing units and retain the selected plan in checkout. The reason is understandable comparison, not a claimed conversion increase. Check long plan names, annual totals, compact layout and real billing data.

Resolve the following for the actual surface, with values from the target design system or explicit proposed tokens:

- Composition: primary focal object, reading order, shared edges, containment, density and wide/compact navigation model.
- Typography: role hierarchy, readable line length, line-height, wrap behavior and numeric alignment.
- Geometry: spacing relationships, control sizes, gutters, radii, boundaries, elevation and inset alignment.
- Identity: target palette, semantic states, asset treatment, tone and one coherent expressive idea. Source palettes stay excluded unless the user explicitly changes that rule.
- Interaction: actual actions/routes, focus, keyboard/touch, loading, empty, error, disabled, success, recovery and persistence.
- Motion: purpose, trigger, persistent object, entry/settled states, interruption and reduced-motion alternative.

Apply [Seven craft passes](seven-craft-passes.md) to carry these decisions through calibration, review and integration. Use the existing Visual system and Design decisions references for detailed execution. Do not substitute adjectives such as premium, next-gen or clean for these decisions.

## Worked corrections

| Weak proposal | Better decision process | Required check |
|---|---|---|
| Three pricing cards with different colors and a Popular badge | Identify real audience/limit differences, align comparable values, justify emphasis and disclose the billing commitment. Use the pricing screen plus payment guide. | Compare the same attribute across plans at wide and compact sizes; verify real totals. |
| Add a toast when payment fails | Distinguish invalid input, definite rejection and unknown transaction status. Place correction locally; reconcile unknown outcomes before retry. | Exercise those states using the actual processor contract. |
| Put every desktop function in large rounded cards | Identify repeated inspection or editing tasks. Consider a list/detail workspace, command search, contextual inspector and restrained row density. | Keyboard navigation, window resizing, selection continuity and long content. |
| Copy a screenshot's settings form | Determine personal/workspace/organization scope and immediate versus explicit save behavior. Show modified or managed values appropriately. | Change scope, reset, leave with pending edits, and handle a denied update. |
| Use the public-sharing control for filesystem permissions | Identify whether the target uses roles/public links, POSIX mode bits, ACLs, or OS capability prompts; choose the corresponding model. | Verify the actual authorization semantics and recover from rejected changes. |
| Add animation to make it professional | Identify what relationship the transition explains. Choose restraint for repeated tasks and expressive scenes only where they support the message. | Observe intermediate frames, interruption, compact playback and reduced motion. |
| Combine the hero of one reference, cards of another and dashboard of a third | Select one organizing idea; translate complementary details into the same type, spacing, shape and interaction system. | Review the whole page/task rhythm, not isolated attractive crops. |

These are original coaching examples, not measured outcomes from the source products.

## Concept construction and review gates

1. Establish the product facts, target context and open choices. Preserve the project's standing preferences; ask only about unresolved consequential facts. Do not restart a generic taste questionnaire.
2. Develop three distinct complete concepts automatically in an isolated workspace, as required by Concept delivery. Use equivalent content and scope, with real visual and interaction differences. Keep image generation subject to the user's permission requirement.
3. Render and inspect each candidate's complete task/page, details, compact/wide variants and important states. Static parsing, screenshots that were not viewed and a neat plan are not visual evidence.
4. Review composition/identity, typography, spacing/alignment, target palette/contrast, component anatomy, assets, motion, task completeness and accessibility. Record `meets`, `needs work`, or `unverified` with actual observations. Do not average a serious failure away with other strengths or invent numeric taste scores.
5. Correct every in-scope material issue and re-render the changed version before presenting a choice. If all candidates are weak, revise their structure or identity rather than asking the user to pick the least weak one. Preserve verified strengths while addressing the limiting defect.
6. Host the reviewed candidates with direct links and keep them available during selection. An inaccessible preview or missing render is a blocker to a visually approved handoff; disclose the blocker and supply the concrete work already completed.
7. After selection/delegation, implement in the real project and compare the integrated result with the selected concept. Recheck shared components, realistic data and interactions. A beautiful mock does not establish production readiness.

The enforceable commitment is the process and evidence boundary: no silently skipped review, no unreviewed concept labeled approved, no known major defect hidden behind a completion claim. A skill cannot guarantee subjective aesthetic judgment, user success or production reliability for every task. Report what actually met the brief and what remains unverified.

## Apply the built-in modules

Choose the local module for the limiting decision: Craft for hierarchy and composition; Component selection for control behavior; Motion design for state continuity; Product demonstrations for staged proof; Interface audit for implementation findings. Apply it to the actual artifact, fix the defect and inspect the changed result. No external skill or source fetch is required.

Store project decisions and rejected mismatches in the project's design record. Reuse them within that project; do not silently mutate this shared collection or generalize an unverified preference into a universal rule.
