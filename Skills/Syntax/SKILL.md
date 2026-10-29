---
name: syntax
description: Use whenever writing or editing Python code in notebooks or scripts for this user, to match their personal coding style — conceptual (how they think about code) and technical (exact formatting rules).
---

# Syntax — Personal Coding Style

This is not generic "clean code" advice. It's one person's specific style, and it should be followed exactly, not loosely approximated. When in doubt between "idiomatic Python" and "what this file says," follow this file.

## Conceptual philosophy

- **Minimalistic over complete.** No boilerplate, no defensive programming for cases that won't happen, no over-abstraction. A notebook cell should do one clear thing.
- **Comprehension-driven.** Prefer dict/list comprehensions over explicit loops whenever the logic fits on one readable line. A `for` loop is a signal the logic got too complex for a comprehension — only reach for it then.
- **Short, one-line algorithms, to an extent.** Compress logic into dense one-liners when it stays readable. Don't chain comprehensions so deep they need re-reading three times — there's a line between "elegant" and "golfed," stay on the elegant side.
- **Idempotent by default.** Any code that writes a file, trains a model, or creates an artifact checks whether it already exists first. Re-running a notebook cell should never redo expensive work or duplicate output.
- **Notebook-first.** Logic lives in cells, not hidden in imported modules, unless something is genuinely reused across many notebooks. One clear purpose per cell.
- **Comprehension over commentary.** Code should explain itself. Comments are rare — only for genuinely non-obvious logic (e.g. a batch-pairing trick, a toroidal-wrap convolution), never to restate what a line already says.
- **No unnecessary error handling.** Skip try/except for things that won't realistically fail in a notebook context. Defensive code is a last resort, not a default.

## Technical formatting rules

### Spacing
- Always a space before **and** after `=` — both in assignments and keyword arguments.
  ```python
  fig, ax = plt.subplots(figsize = (24, 6), facecolor = '#22272E')
  df = pd.DataFrame({column : values}, dtype = 'float64')
  ```
- Always a space before `:` in single-line `for` / `if`, no space required after (standard).
  ```python
  for column in columns : df[column] = df[column].astype('float64')
  if not pathlib.Path(path).exists() :
      joblib.dump(model, path)
  ```

### Naming
- **Essential / meaningful variables start with a capital letter** — datasets, dataframes, models, config dicts. Think of it as marking "this is a named entity in the project," not a throwaway.
  - Datasets: UPPERCASE (`ENCDM`, `RGPH`)
  - Derived dataframes: `Clean` + dataset name (`CleanENCDM`)
  - Maps/metadata: `Map` + dataset name (`MapENCDM`)
  - Model dicts: `Models` + dataset name (`ModelsENCDM`)
  - Config dicts: dataset + `Config` (`RGPHConfig`)
  - Classes: PascalCase (`CleanDataset`, `Hypernetwork`)
- **Throwaway / local variables: lowercase, concatenated, short, but still meaningful** — not snake_case. `batchsize`, `hiddendim`, `epochloss`, `encdmiter`, not `batch_size` or `b`. The goal: as much meaning as possible in as few characters as possible, without abbreviating into noise.
- **Plot colors:** a single `Colors` dict, referenced as `Colors['blue']`, never hardcoded hex inline in a plotting call.
- **Data-native naming:** keep original column names exactly as the source data has them (including non-English characters, accents, spaces-as-underscores) — never rename to "cleaner" English equivalents.
- **File naming:** `{Method}_{target}.joblib` style for saved models (`KNN_Quintileurbain.joblib`, `SS_Taille_ménage.joblib`).

### Imports
- Standard library first, then third-party, no blank-line-per-import padding.
- Combine related stdlib imports on one line: `import joblib, json, pathlib`
- Alias long names: `from lightgbm import LGBMClassifier as LGBMC, LGBMRegressor as LGBMR`
- Suppress known noisy warnings explicitly rather than ignoring them silently:
  ```python
  import warnings
  warnings.filterwarnings("ignore", category = UserWarning, module = "sklearn")
  ```

### Data inspection
- `display()`, never `print()`, for inspecting DataFrames or data structures in a notebook.
- Set pandas display options once near the top of a notebook:
  ```python
  pd.set_option('display.max_columns', 50)
  pd.set_option('display.max_colwidth', 150)
  pd.set_option('display.max_rows', 100)
  pd.set_option('display.width', 1000)
  ```

### File I/O
- Paths are relative from `Notebooks/` (`'../Data/Processed/...'`).
- Every write is gated on an existence check:
  ```python
  if not pathlib.Path('../Assets/Maps/MapENCDM.json').exists() :
      with open('../Assets/Maps/MapENCDM.json', 'w', encoding = 'utf-8') as file :
          json.dump(data, file, indent = 4, ensure_ascii = False)
  ```
- JSON maps: label → code on save, inverted (code → label) on load.

### Common patterns to reach for
- Dict comprehensions for building per-column maps, encodings, and config structures rather than loop-and-append.
- Sorting dicts by a derived key via `sorted(d.items(), key = lambda item : ...)`, rebuilt as a dict comprehension.
- Auto-tuned hyperparameters from data size rather than hardcoded constants, when it's a one-liner:
  ```python
  leaves = min(31, max(7, int(np.sqrt(len(train)))))
  ```

## What to avoid
- Long docstrings or type hints inside notebooks.
- Helper functions for genuinely one-off operations — inline them.
- `print()` for data inspection.
- Renaming source-data columns to English or "nicer" names.
- snake_case for simple/local variables.
- Try/except blocks used defensively rather than for a real, expected failure mode.
- Comments that explain obvious code.
- Writing a file or training a model without checking if it already exists first.
