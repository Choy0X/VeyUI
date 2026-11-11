# One design lead, independent reviewers

Use this for substantial design work when delegation tools and host authorization are available. This skill prefers one lead with independent critique, rather than three designers creating incompatible systems. Do not create or claim unavailable agents. Without delegation, perform the same perspectives sequentially and label them as self-review, not independent review.

## Ownership and evidence

The lead owns project understanding, reference selection, content, all concept directions, implementation and reconciliation of findings. Reviewers advise; they do not silently edit shared design files or invent new brand requirements.

Give each reviewer the actual user brief, selected compiled reference descriptions (or source images only for explicit image-matching tasks), the quality contract, candidate URLs/versions, complete captures and relevant scope. Include constraints and known simulation boundaries. Do not send the lead's preferred winner, expected score, desired verdict or a flattering justification. Reviewers must inspect the work, not repeat its description.

| Reviewer | Inspect | Return |
|---|---|---|
| Visual design | Reference fit, composition, typography, palette, spacing, component geometry, imagery and whole-page rhythm | Ranked concrete defects with screen/section/capture location, why they matter, correction and required recheck |
| UX and engineering | Task path, truthful content/data, state coverage, keyboard/touch, semantics, responsiveness, motion behavior and relevant implementation risks | Reproducible action/state, expected vs observed behavior, severity and proposed fix; distinguish source inspection from runtime tests |

Share current artifacts directly when tools permit; screenshots alone cannot prove interaction behavior. If a reviewer cannot render, provide actual captures for visual review and mark runtime checks unverified. Never present code-only review as a visual assessment.

## Review cycle

1. The lead first removes obvious defects so reviewers see meaningful work.
2. Run independent reviews on the same candidate versions. They can be parallel when their tools and resources allow it. Do not let reviewers mutate the shared project.
3. Consolidate duplicate findings into one small defect list. Preserve disagreement with its evidence. Compare it to user requirements and the chosen reference; do not resolve it by majority vote or taste labels alone.
4. Fix blockers and major in-scope defects. Record accepted minor limitations or an evidence-backed rejection of a finding. Do not dismiss a reference mismatch merely because the implementation is accessible or builds successfully.
5. Re-render changed states and return the corrected artifacts to the appropriate reviewer. An unchanged old screenshot cannot close a new-version defect.
6. Present the concepts when material findings are resolved and the hosting/selection contract is satisfied. Do not report approval from a reviewer who never saw the corrected result.

Use this prompt shape, adapted to the actual job:

> Review these candidate artifacts against the supplied brief, references and quality contract. Inspect the actual images and use the available runtime for the interactions in your scope. Report your strongest concrete findings with evidence and location, severity, correction and recheck. Separate observations from assumptions. Do not edit the candidate files. If you cannot inspect something, mark it unverified. Compare candidate tradeoffs only after reviewing each one.

After integration, review the actual application against the selected concept and product contracts. A concept review does not approve a later implementation automatically. Independent reviewers improve scrutiny; they do not certify user preference, commercial outcomes or universal visual quality.
