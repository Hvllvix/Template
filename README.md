# Template

**A clean starting structure for Python data science and ML projects.** Organized folders for data, notebooks, models, and dashboards, a consistent plotting theme, and a set of Skills that keep code style, documentation, and design consistent across every project built from this template.

---

## Why This Template

Starting a new project usually means re-deciding folder names, re-writing the same `rcParams` block, and re-establishing documentation conventions from scratch. This template fixes that once:

| Concern | Handled By |
| :--- | :--- |
| **Folder structure** | Fixed layout for data, models, notebooks, dashboard, and scripts |
| **Plot styling** | `Notebooks/Themes/`: Light and Dark `.mplstyle` sheets, one `Colors` palette |
| **Code style** | `Skills/Syntax/`: comprehension-driven, idempotent, consistently formatted |
| **Notebook & README writing** | `Skills/Documentation/`: consistent markdown structure, auto-generatable README |
| **Dashboard & plot design** | `Skills/Design/`: layout, color, and interactivity conventions |

---

## Getting Started

```bash
git clone <your-new-repo-url>
cd <your-new-repo>
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

1. Drop raw data into `Data/Raw/`.
2. Build the pipeline in order: `Notebooks/Pre-Processing.ipynb`, `Modeling.ipynb`, `Evaluation.ipynb`.
3. Load the plot theme at the top of any notebook:
   ```python
   from matplotlib import pyplot as plt
   plt.style.use('../Notebooks/Themes/Dark.mplstyle')
   ```
4. Save trained models to `Models/`, generated reports/figures to their respective folders.
5. If the project needs a dashboard, build it under `Dashboard/`, following the conventions in `Skills/Design/`.

---

## Repository Layout

```text
Template/
├── Dashboard
│   ├── Pages
│   │   └── .gitkeep
│   └── app.py
├── Data
│   ├── Maps
│   │   └── .gitkeep
│   ├── Processed
│   │   └── .gitkeep
│   └── Raw
│       └── .gitkeep
├── Models
│   └── .gitkeep
├── Notebooks
│   ├── Themes
│   │   ├── Dark.mplstyle
│   │   └── Light.mplstyle
│   ├── Evaluation.ipynb
│   ├── Modeling.ipynb
│   └── Pre-Processing.ipynb
├── Scripts
│   └── tree.py
├── Skills
│   ├── Design
│   │   └── SKILL.md
│   ├── Documentation
│   │   └── SKILL.md
│   └── Syntax
│       └── SKILL.md
├── .gitignore
├── README.md
├── requirements.txt
└── tree.txt
```

Regenerate this tree anytime with:

```bash
python Scripts/tree.py
```

---

## Notebooks

| Notebook | Purpose |
| :--- | :--- |
| `Pre-Processing.ipynb` | Data ingestion, cleaning, vocab/mapping construction, EDA |
| `Modeling.ipynb` | Model definition, training, ablations |
| `Evaluation.ipynb` | Final metrics, error analysis, result plots |

Each starts empty, scaffolded for the pipeline, not pre-filled.

---

## Skills

Skill folders under `Skills/` each hold a `SKILL.md` that defines a consistent convention to follow when working in this repo:

- **Syntax**: how code should be written, comprehensions, spacing, naming, idempotent I/O.
- **Documentation**: how notebook markdown cells and `README.md` files should be structured and written.
- **Design**: how plots and dashboards should look, the `Colors` palette, theme files, layout and interactivity rules.

---

## Requirements

- Python 3.10+
- See `requirements.txt` for the full dependency list

---

## License

MIT
