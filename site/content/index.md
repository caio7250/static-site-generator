# Static Site Generator

A lightweight Python generator that turns markdown into a clean, consistent site with one template.

## Quick start

1. Add or edit markdown in `site/content/`
2. Run `python3 src/main.py`
3. Serve the output from `docs/`

## Project structure

- `site/content/` markdown pages
- `site/templates/base.html` layout
- `site/static/index.css` styling
- `docs/` generated output

## Customize

- Update the HTML layout in `site/templates/base.html`
- Adjust styles in `site/static/index.css`
- Add new pages by creating folders in `site/content/`

Want to see it in action? [Read the use case](/use-case/).
