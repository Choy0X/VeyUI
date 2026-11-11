# Precedent selection and synthesis

Use the bundled library as prepared reference knowledge. This adapts a screen/flow research approach to offline, bounded text retrieval; it is not a live Mobbin connection or equivalent catalog size. Default retrieval sends no source screenshots or URLs to the model.

## Ask the right reference question

Identify whether the decision concerns a screen, a section, a control in context or a journey. Search one primary job/state at a time and apply the actual platform filter. Start with the user's problem rather than your assumed solution: `plan selection` before `three pricing cards`, `sharing access` before `modal with email chips`. Add only constraints needed by the task. For a journey, retrieve documented flows separately. Local ranking is lexical, not semantic embeddings; if weak, use the vocabulary of nearby pattern tags and report genuine gaps.

```sh
python3 scripts/design_library.py brief "sharing permissions" --platform desktop
python3 scripts/design_library.py search "pricing" --platform web --limit 3
python3 scripts/design_library.py flows "settings" --platform desktop
python3 scripts/design_library.py decisions "validation recovery"
```

Run from the installed skill path or use absolute script paths. Read only returned records; retrieve a specific ID if its detail is needed. Preserve the default character budget. A missing category is not permission to rename a vaguely similar screen into the required evidence.

## Use the evidence at its real strength

- Reviewed screen description: visible anatomy transcribed during ingestion. It does not prove interaction behavior, conversions or usability.
- Documented flow: publisher-described sequence with linked screen IDs where available. It is not a runtime-tested user journey.
- Decision guide or pattern: original design advice. It may fill a gap but must stay labeled as judgment.
- User concept: visual ambition and composition; it may be an unshipped design rather than production evidence.

Count distinct products when discussing precedent breadth; many screenshots of one app are one product example. Name the actual platform. Cross-domain or cross-platform references can support a spatial relationship, but do not establish the target's business rules or host behavior. Keep source palettes out of target palette selection.

## Synthesize, do not collage

For a redesign, freeze what must survive: task, data semantics, routes/actions, supported states, explicit brand constraints and unaffected consumers. Inherited visual defaults can change within authorized scope; verified product facts cannot. Capture baseline evidence before edits.

Group useful references by the structural decision they make. Choose a coherent direction for each concept rather than one unrelated reference per component. For a narrow component, vary one main decision for a readable comparison. For a whole page/app concept, vary composition, identity and appropriate UX together while keeping facts and scope equal. Do not introduce novelty into familiar controls merely to make candidates differ.

For each major move record `problem | reference ID and observed relationship | proposed change | preserved behavior | tradeoff | verification`. One observed example is an example, not an industry consensus. Where no precedent exists, propose original work honestly. The user's concept can legitimately support a creative direction even when no shipped-screen match exists.

## Stop researching and build

After a compact packet supports the key decisions, move into calibration and actual prototypes. More references do not repair an unrendered design. Use Recommended directions to resolve open inspiration proactively with a small verified live-link shortlist. Beyond that planning step, request new-source inspection only for a genuinely missing decision or when the user explicitly wants a new link/image interpreted. Do not repeatedly fetch already compiled screenshots. Source audits and collection expansion use Research/ingestion; normal design uses this module.
