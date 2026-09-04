# RoadLens Australia — Validation Notes

The project includes a repeatable local and GitHub Actions QA process.

Validated checks include:
- exactly 10 required HTML pages;
- `lang="en-AU"`, non-empty page titles and semantic `<main>`, `<nav>` and `<h1>` structure;
- Content Security Policy on every page;
- image alternative text and labelled form controls;
- no inline JavaScript or inline `style` attributes;
- all local hyperlinks resolve;
- `data/roadlens-data.json` parses as valid JSON;
- `assets/app.js` passes `node --check`;
- responsive media queries, visible keyboard focus and reduced-motion handling are present.

Run locally with:
```bash
python scripts/qa_check.py
```

The same script is configured in `.github/workflows/qa.yml` to run on GitHub pushes and pull requests. The final local run on 4 September 2026 completed with **ALL CHECKS PASSED**.

The group should still retain any lecturer-requested evidence from W3C HTML/CSS validators and manual accessibility/browser testing because automated structural checks do not prove full WCAG conformance.
