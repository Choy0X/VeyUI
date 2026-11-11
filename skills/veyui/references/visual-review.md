# Visual review before selection or completion

Apply Quality contract, [Seven craft passes](seven-craft-passes.md), Unslop workflow and Review team. Use this for each material design candidate and for the implemented result. Treat visual craft, behavior, and engineering verification as separate evidence streams. A pass in one does not imply a pass in another.

## Render, inspect, correct

1. Open the artifact in its real browser or platform runtime. Confirm fonts and assets loaded, the intended route/state is displayed, and review controls do not obscure the design. Label an HTML simulation of native or product UI as a simulation.
2. Capture the actual rendered candidate at matched wide and compact views and any intermediate width, theme, or state promised by the brief. Inspect images yourself at readable scale, including the opening viewport and full-page rhythm. A thumbnail can show rhythm but cannot verify type, alignment, or detail.
3. Exercise the interaction being evaluated. Inspect start, changed, and settled states and important recovery. For motion, watch playback or a temporal sequence, including repeated/interrupted input and reduced motion. For prototype actions outside scope, label the boundary. A dead hash link is not evidence of a working primary CTA.
4. Review the dimensions below against the brief, supplied references, and incumbent. Identify the highest-impact defects with visible locations and specific corrections. Make corrections and re-render affected views. Continue while material defects remain and fixes are feasible within scope. Do not manufacture an arbitrary number of iterations or claim a critique pass without findings.
5. Record actual evidence and only then present viable choices or completion. If all candidates are weak, improve them rather than making the user choose the least weak option.

| Review dimension | Inspect in the render |
|---|---|
| Identity and composition | Is the promised idea visible? Is there a clear focal point, intentional balance, and strong relative scale? Would the page still be identifiable without its logo? For fixed-brand product UI, does it feel coherent with that product? |
| Hierarchy and typography | Can a visitor scan the message and next action? Check headline line breaks, text measure, reading size, label/data hierarchy, alignment, weight, and fallback-font changes. |
| Spacing and geometry | Check shared edges, optical alignment, related versus unrelated group gaps, card padding, control baselines, repeated radii, icon geometry, and cramped or empty areas. |
| Color and depth | Check actual contrast pairs, accent distribution, surface separation, status meaning, shadow consistency, and whether depth or decoration supports the composition. |
| Content and authenticity | Check actual claims, readable product proof, realistic text/data, correct destinations, honest sample labels, and visibly incomplete assets or sections. |
| Rhythm and adaptation | Check the whole page or task sequence, repeated layouts, section lengths, mobile cropping, overflow, text wrapping, scale changes, and compact control reachability. |
| Interaction and motion | Check focus/keyboard/touch where relevant, visible feedback, continuity, end states, interruptions, motion purpose, and reduced-motion parity. |

Use concrete observations such as “the hero proof is below two screenfuls on the compact view” or “three consecutive sections use the same two-column framed-card composition.” Avoid substituting subjective numeric scores for evidence. Expert aesthetic judgment is still judgment, not a measured conversion improvement or user research result.

Review each applicable craft pass against the planned decision and rendered evidence. Describe the first focal area, the actual grouping gaps, type roles and readable line breaks, emphasis/status colors, coherent product content, close component detail and spatially connected motion. Fix the highest-impact defect first and inspect the resulting state. Seven affirmative labels alone do not establish readiness.

## Keep an evidence record

For each candidate or implemented version record **artifact/version | runtime | viewport/device | theme/state | capture or recording | observed defect | correction | recheck result**. Keep this compact and scoped. Store captures with the work where possible. For `check_evidence.py`, set `expected_versions` for every required view and `expected_interaction_versions` for required interactions. Each resolved finding records `fixed_in_version` and points to an inspected recheck view of that version. Preserve actual version provenance rather than relabeling old captures. A capture path proves a file exists only after checking it; personally viewing it is a separate requirement.

Apply Reference calibration against the selected compiled screen facts and recorded target decisions. Use actual source images only for explicitly image-based matching work; always inspect the candidate itself. Reject materially mismatched art direction, unfinished skeleton sections and low-fidelity substitutions for defining assets.

Before calling a candidate ready for selection, require:

- A working gallery and direct preview URL verified from the user-accessible review surface, with its lifetime disclosed and server retained. Hosting and visual inspection are separate checks.

- Rendered wide and compact compositions personally inspected, or the appropriate native window/device classes.
- The complete landing page or representative end-to-end app task, including promised states, motion and adaptations; a hero-only render does not satisfy coverage.
- Promised distinguishing visuals and interactions actually present at the stated fidelity.
- Current-version visual and UX/engineering findings resolved and rechecked; identify independent review or the reason for self-review.
- No known material visual defects obscuring the proposed direction.
- Important claims, simulated components, and out-of-scope actions clearly identified.
- A recommendation supported by comparable reviewed views. Show these views alongside the preview when available.

An incomplete baseline does not automatically block unrelated exploration, but it cannot establish improvement for uncaptured states. Track the missing coverage. Missing runtime access prevents a “visually reviewed” claim even when code looks plausible. Use **draft — visual review blocked** or **specification only**, name the actual blocker, and complete other authorized work. Do not ask the user for final visual approval of an uninspected artifact. They may explicitly choose a draft despite that limitation, which must remain recorded.

## Present the decision, not the internal process

Show the reviewed candidates, describe the specific visible differences, state the strongest recommendation and its tradeoff, and ask only for the unresolved decision the user owns. Retain approved choices and delegated authority. Do not ask the user to resolve a font/color heuristic conflict that the agent should handle.

For an implementation request, a prototype milestone is not the final landing page. State that boundary clearly. If the approved plan explicitly requires concept selection, pause there only after providing reviewed candidates. If approval/delegation already covers the design and implementation, continue within it rather than restarting approval. New material scope or image generation remains separately governed.

A prototype review must not claim CMS, billing, native permissions, production components, or real navigation were integrated solely because a mock shows them. A source audit, build, or syntax check cannot prove rendered quality. An ASCII-only check is unrelated to design readiness.
