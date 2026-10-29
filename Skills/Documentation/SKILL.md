---
name: documentation
description: Use whenever writing markdown cells in a notebook, or generating/updating a project's README.md, to keep documentation style consistent, professional, and complete across all projects.
---

# Documentation — Notebook Cells & README Generation

Two distinct but related jobs: **narrating a notebook** as it's built, and **writing the README** that summarizes the finished project. Both aim for the same voice: clear, structured, slightly formal, never dry or filler-heavy.

## Part 1 — Notebook markdown cells

Every notebook opens with a single title cell, then gets a markdown cell before each major code section explaining what that section does and why. Never document after the fact in one giant pass — write the markdown cell right before (or right after) the code cell it describes, matching the step-by-step build.

### Title cell (first cell, always)
```markdown
# **Project or Notebook Title: Short Descriptive Subtitle**
One to two sentences framing the whole notebook: what it does, what techniques it uses, and why that combination is interesting or necessary. End with what the reader should take away.
```

### Section cells
Use `###` for a major section, `####` for a subsection within it. Structure depends on what the section does:

**For a function / class being introduced:**
```markdown
### The `FunctionName` Function: Short Description of What It Does

One to two sentence paragraph giving context — why this exists, what problem it solves.

#### Function Purpose
- To do X.
- To do Y.

#### Parameters
- `param` (`type`): what it controls, default if any.

#### Functionality Breakdown
1. **Step name**: what happens in this step.
2. **Step name**: what happens next.
```

**For a conceptual/methodology section (not a single function):**
```markdown
### Section Title

Short framing paragraph.

#### Subsection Name
*   **Bolded concept**: explanation of that concept, often naming the exact library/method used (e.g. `scipy.signal.convolve2d`, `boundary = 'wrap'`).
*   **Bolded concept**: explanation.
```

**For results / conclusion sections:**
- Open with a short recap of the notebook's journey (what was built, in order).
- Follow with a `####`-headed explanation of *why* results look the way they do — not just what the numbers are, but the underlying reason (e.g. forward vs. inverse problems, determinism vs. ambiguity). This is the most important part: always explain mechanism, not just outcome.

### Style rules for notebook prose
- Bold key terms and function/parameter names inline using backticks for code identifiers (`` `ColumnName` ``) and `**bold**` for concepts.
- Prefer bullet lists with a bolded lead-in phrase over long paragraphs: `- **Term**: explanation.`
- Numbered lists only when order genuinely matters (steps in a pipeline); bullets otherwise.
- Every parameter gets its type annotated in backticks: `` `steps` (`int | None = 2`) ``.
- Always state defaults explicitly when documenting a function's parameters.
- End major model/result sections with a short "why" paragraph, not just a restatement of metrics.
- No emoji, no exclamation points, no marketing language ("amazing," "powerful," "cutting-edge").

## Part 2 — README generation

A README should read as a professional package/library document, written for someone deciding whether to use or trust the project in under two minutes.

### Structure (in order)
1. **Title + one-line description** — `# Project Name` then a bolded one-paragraph summary of what it is and its core mechanism (not just domain — the actual approach).
2. **Install / entry point** — where to get it, one command.
3. **Why [Project]** — a short section contrasting it against the naive/common approach, explaining the specific design choice that makes it different. Often includes a small comparison table (dimension vs. standard).
4. **Installation** — copyable shell commands, plain and dev/editable install both if relevant.
5. **Quick Start** — a minimal, runnable code example. Show typical usage, not every option.
6. **How It Works** — numbered list of the pipeline's actual steps, short and mechanical, no fluff.
7. **Reference tables** — for anything with multiple modes/branches/models (e.g. "Model Selection" table, "Dashboard Sections" table), use a markdown table: left column = the case, right column = what handles it or what it does.
8. **API Reference** (if a library) — table of method → return type → one-line description.
9. **Tests / validation** (if applicable) — how to run them, what they check, as a bullet list.
10. **Repository Layout** — a fenced ```text tree block of the actual folder structure, generated via `Scripts/tree.py`, not retyped by hand.
11. **Requirements** — plain list, Python version floor first.
12. **Contributing** — short numbered steps (fork, branch, test, PR).
13. **License** — just the name (e.g. `MIT`).

### Style rules for README
- Horizontal rules (`---`) between major sections.
- Tables over prose whenever comparing more than 2 things side by side.
- Code blocks are copy-pasteable as-is — no placeholder angle brackets unless genuinely user-specific (e.g. `<your-api-key>`).
- Bold the project name on first mention, never after.
- Section headers are `##`, never `#` after the title.
- Keep sentences short. No padding sentences that exist only to transition ("Now let's talk about...").
- A one-line disclaimer where relevant (e.g. "probabilities are policy research estimates, not individual ground-truth labels") — flag limitations plainly, don't bury them.
- For multi-component projects (e.g. a dashboard with a companion library), add a short "Companion Project" section linking out, rather than duplicating its docs.

### When generating a README from scratch
1. Read the actual repo structure (`tree.py` output) — don't guess folder names.
2. Read the notebooks' title/conclusion cells for the accurate description of what the project does and why.
3. Pull real function/class names from the code, not paraphrased ones.
4. Match the table-heavy, mechanism-first style — avoid generic "this project uses machine learning to..." openers.
