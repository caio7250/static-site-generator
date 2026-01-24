# Static Site Generator

This repository contains a lightweight Python static site generator with a documentation-style template focused on practical usage.

## Project structure

- `src/` generator source code
- `site/content/` markdown pages
- `site/static/` static assets (CSS, images)
- `site/templates/` HTML templates
- `docs/` generated site output

## Run locally

```
python3 src/main.py
cd docs && python3 -m http.server 8888
```

## Example site and use cases

A live example site generated from this repo is available here:

- https://caio7250.github.io/static-site-generator/

Use cases include product launches, internal documentation, and public developer portals.

## Build for a hosted subpath

If you are publishing under a subpath (for example, GitHub Pages project sites), pass the base path:

```
python3 src/main.py "/static-site-generator/"
```

Or use the existing script:

```
./build.sh /static-site-generator/
```

## Tests

```
./test.sh
```

## Customize the site

- Update page content in `site/content/`
- Adjust layout in `site/templates/base.html`
- Tweak styling in `site/static/index.css`
