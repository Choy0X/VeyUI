# Experience design and product reasoning

## Start with the task, then shape the experience

Write a concise problem statement using audience, situation, task, friction, desired outcome and constraints. Inspect real product behavior and available research before inventing personas. Label assumptions. Distinguish buyer goals on a landing page from recurring user goals inside an app.

Map the primary path as **entry → understanding → choice/input → commitment → feedback → next step/recovery**. For each step identify the user's question, information needed, action, system response, possible failure and exit. Include the consequential alternate path, not every theoretical edge case. Never use a beautiful screenshot as proof that the path works.

## Resolve information architecture

- Group content by the user's mental model and frequency of use. Name destinations in user language. Separate navigation, object actions and account/workspace settings.
- Decide whether the task needs a list, table, board, canvas, timeline, form or guided flow. Explain the choice using comparison, spatial reasoning, sequence, frequency and data density.
- Define the object model and hierarchy before drawing dashboards. A dashboard should support a decision or next action. Avoid a grid of metrics with no relationship to actual work.
- Decide what stays visible and what is progressively disclosed. Preserve orientation, navigation history, selection and drafts when the layout changes.
- Write representative content early. Long labels, realistic names, localization, zero values and missing data reveal design constraints hidden by lorem ipsum.

## Design the state contract

For each consequential component or task, record applicable states and transitions in one compact table.

| Field | Resolve |
|---|---|
| Trigger and prerequisites | What starts the state and what data/access is necessary? |
| Display and next action | What does the person see, understand and do? |
| Persistence | What survives navigation, reload, window resizing or interruption? |
| Recovery | How do validation failure, lost connectivity, expired sessions or partial success resolve? |
| Semantics and input | What is announced, focused and available through keyboard, touch or assistive technology? |
| Truthfulness | Which values are real, sample, inferred, pending or unavailable? |

Make empty, unavailable, unauthorized, loading and failed states distinct. Explain error recovery near the relevant task and preserve valid input. Confirm actual consequences before destructive or consequential actions. Use undo only when restoration is implemented.

## Content and trust

Use precise action labels and explain commitments at the point of decision. Keep claims traceable to approved product facts. Avoid fabricated social proof, activity, statistics and testimonials. Treat privacy, billing, permissions and AI execution status as product behavior rather than decorative copy. Do not infer legal or compliance claims from a visual benchmark.

For AI interfaces, distinguish drafts from applied changes, sources from generated claims, tool activity from simulated animation, and pending work from success. Give users ways to correct, stop, inspect and recover where supported.

## Evaluate without invented research

Use an expert cognitive walkthrough when user testing is unavailable: start from a realistic goal, attempt the task with representative data, note hesitation or ambiguity, and inspect feedback and recovery. Report this as expert review. Do not call simulated users, self-review or model-generated personas real research.

When user testing is available and authorized, define a neutral task, observe completion and errors, and separate observed behavior from interpretation. Use findings to revise the specific flow. Choose a measurable success signal where useful, such as completion without assistance, error recovery or finding a relevant item. Do not claim conversion uplift before measurement.

## Deliver proportionately

For a significant product redesign, produce the task model, information architecture, primary/alternate flow, state contract and representative high-fidelity views. For a small exact edit, preserve the existing model and inspect affected behavior only. Good UX work reduces unnecessary decisions for both the user and the implementer.
