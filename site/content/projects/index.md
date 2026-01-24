# Guide

[< Back Home](/)

## Create a page

- Add a folder under `site/content/`
- Place an `index.md` inside it
- Use markdown headings and links normally

Example: `site/content/getting-started/index.md` becomes `/getting-started/`.

## Run the generator

```
python3 src/main.py
```

The HTML output is written to `docs/`.

## Serve locally

```
cd docs && python3 -m http.server 8888
```

## Deploy

Upload the `docs/` folder to any static host, or build with a base path if you publish under a subpath.
