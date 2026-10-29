---
name: design
description: Use when building dashboards (Streamlit/Plotly) or matplotlib plots in notebooks, to apply consistent visual design — layout, color, typography — and load the Light/Dark theme files from Notebooks/Themes/.
---

# Design — Dashboards & Plots

## Theme files

Two matplotlib style sheets live in `Notebooks/Themes/`: `Dark.mplstyle` and `Light.mplstyle`. Always load one at the top of a notebook rather than re-declaring `rcParams` inline:

```python
plt.style.use('../Notebooks/Themes/Dark.mplstyle')
```

Default to `Dark.mplstyle` unless the user specifies otherwise — it matches the GitHub dark-theme-rendered notebooks and the dashboard's default look.

## Color palette

A single `Colors` dict, consistent across every plot, every notebook, every dashboard:

```python
Colors = {
    'orange' : '#F4583E',
    'blue'   : '#62C1FE',
    'purple' : '#8957E5',
    'green'  : '#2EA043',
    'grey'   : '#444C56',
    'gold'   : '#D29922',
    'pink'   : '#F92672'
}
```

Never hardcode a hex value inline in a plot call — always reference `Colors['name']`. When a plot needs more than 7 series, cycle the dict rather than introducing new ad-hoc colors.

## Matplotlib conventions (notebooks)

- **Figure size**: large by default — `figsize = (24, 6)` for wide single-row plots, `(26, 8)` for grid layouts.
- **Titles**: left-aligned, not centered — `ax.set_title('Title', loc = 'left', fontsize = 14, pad = 20)`.
- **Spines**: hidden on all sides for a clean, open look — `for spine in ax.spines.values() : spine.set_visible(False)`.
- **Bar labels**: always annotate bars directly rather than relying on a y-axis alone — `ax.bar_label(bars, padding = 4, fontsize = 10, fmt = '%.0f')`.
- **Value annotations**: `ax.text(x, y, f'{int(val):,}', ha = 'center', fontweight = 'bold')` for anything not covered by `bar_label`.
- **Log scale**: switch to it whenever values span more than ~2 orders of magnitude — `ax.set_yscale('log')`.
- **Gridlines**: y-axis only, dashed, subtle — `ax.grid(True, axis = 'y', linestyle = '--', alpha = 0.5)`.
- **Always close with**: `plt.tight_layout()` then `plt.show()`.
- **Composite figures**: use `fig.add_gridspec` for multi-panel layouts with mismatched panel sizes (e.g. two small summary panels above one wide detail panel), rather than forcing uniform `subplots` grids.

## Dashboard design (Streamlit / Plotly)

A dashboard should read as a cohesive product, not a stitched-together set of notebook plots. Principles, in priority order:

### 1. Visual hierarchy
- One clear focal point per page/section — don't give five charts equal visual weight.
- KPIs/headline numbers go first, large and simple (big number + label), before any chart.
- Group related panels; use whitespace (not borders/boxes) to separate groups.

### 2. Color discipline
- One accent palette per theme (reuse the `Colors` dict / theme file — don't invent dashboard-specific colors).
- Color encodes meaning, not decoration: one color per category consistently across every chart on the page, so "poverty rate" is always the same color everywhere it appears.
- Reserve the most saturated color for the thing the user should look at first; everything else recedes (greys, muted tones).

### 3. Interactivity as a design tool, not an afterthought
- Favor a single global filter/selector (e.g. a region click on a map) that cascades to every panel, over separate filters per chart — reduces cognitive load and keeps the page coherent.
- Default state should already tell a complete story before any interaction — don't ship an empty dashboard waiting for input.
- Hover tooltips carry detail; the chart itself carries the headline. Don't cram every number onto the visible chart.

### 4. Typography & spacing
- One font family throughout (inherit from Streamlit's theme config, don't mix).
- Consistent heading scale: page title > section header > panel title > label. Never skip a level.
- Generous padding around panels — cramped dashboards read as unfinished regardless of chart quality.

### 5. Motion & feedback
- Loading states for anything that takes >300ms (model inference, large data filtering) — a spinner or skeleton, never a frozen UI.
- Transitions on filter changes (map re-render, chart update) should feel immediate; debounce rapid interactions rather than firing on every intermediate state.

### 6. Maps specifically
- Clip to the actual region of interest with a transparent/neutral outer area — don't show irrelevant surrounding geography at full opacity.
- Choropleth color scale should be perceptually uniform (avoid rainbow scales) and match the theme's accent palette where possible.
- Always pair a map with a synced, keyboard-accessible alternative selector (dropdown/selectbox) — maps alone aren't accessible.

### 7. Light vs. Dark theme parity
- Whatever is designed in Dark must be re-checked in Light, not assumed to translate — contrast ratios, accent color legibility, and shadow/elevation cues often break when flipped.
- Keep the same `Colors` hues in both themes; only the background/surface/text values swap between `Dark.mplstyle`/`Light.mplstyle`.

## What to avoid
- Rainbow or default matplotlib/Plotly color cycles — always the defined `Colors` palette.
- Centered titles, visible spines, unlabeled bars.
- Dashboards with more than one dominant accent color competing for attention.
- Charts that require a legend to explain more than 4–5 categories — simplify or split the chart instead.
- Pie charts for anything with more than ~4 categories.
