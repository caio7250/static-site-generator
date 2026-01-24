# Reference

[< Back Home](/)

## Template tokens

- `{{ Title }}` uses the first H1 in your markdown
- `{{ Content }}` injects the rendered HTML
- `{{ RootPath }}` ensures assets and links work in nested pages

## Base path builds

For subpath hosting, pass the base path to the generator:

```
python3 src/main.py "/static-site-generator/"
```

## Static assets

Everything in `site/static/` is copied into `docs/`. Keep CSS, images, or fonts there.
