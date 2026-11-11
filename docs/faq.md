# FAQ

**What is veyUI?**
A skill (a folder of instructions, data and scripts) that teaches an AI coding agent a real UI design process: discover, recommend, prototype three concepts, let you choose, implement and verify.

**Which agents does it work with?**
Any agent that supports the Agent Skills format, plus agents that can read `AGENTS.md` or a file path. See [platforms.md](platforms.md).

**Does it generate images?**
Not without your permission. Image generation always needs explicit approval. It prefers your real assets, product UI and approved media.

**Does it need an account, API key or paid service?**
No. The reference library is offline and local. Your agent's own model is the only paid piece.

**Does it send my code anywhere?**
veyUI itself makes no network calls to a service of its own. Your agent works as it normally does. The `skills` CLI sends anonymous install telemetry when you install (opt out with `DISABLE_TELEMETRY=1`).

**How is it different from Taste Skill?**
veyUI is built on Taste Skill's web engine, which it downloads at a pinned commit and uses unmodified, with credit to Leonxlnx. veyUI adds an offline reference library, product discovery and recommendation, the three-concept hosted review, evidence checks, native and app guidance, and packaging for many agents.

**Why are some references text only?**
31 concept studies describe images whose redistribution rights are unverified, so the images are not in this repo. The studies remain as original notes. Third-party app-store and website images are linked, not copied.

**It says it could not host or render. What now?**
Concept building needs a way to serve files and a renderer. veyUI states the missing capability and keeps going with design and draft files, but it will not claim the concept milestone is done. Install Chrome, Edge or Chromium, or enable your agent's preview tools.

**Does it work on macOS and Linux?**
The design is portable and uses Python and Node. It has been exercised on Windows 11. Please report macOS or Linux problems.

**How do I update or remove it?**
See the end of [installation.md](installation.md).

**Will it guarantee great design?**
No. It enforces an evidence-based workflow. Final quality still depends on the model, your inputs and your choice, and a passing check is not visual approval.

**How do I contribute references or modules?**
See [contributing-references.md](contributing-references.md) and [../CONTRIBUTING.md](../CONTRIBUTING.md).
