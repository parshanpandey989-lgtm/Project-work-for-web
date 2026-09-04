# RoadLens Australia — ICT807 Web Technologies

RoadLens Australia is a responsive, data-driven road-safety web application prepared for ICT807 Assessment 2. It transforms aggregate Australian Government road-safety statistics into clear interactive charts, tables and filters while demonstrating semantic HTML5, CSS3, JavaScript, accessibility, privacy and basic web-security principles.

## Run the website
- Quick: open `index.html` directly.
- Recommended: from the project folder run `python -m http.server 8000` and open `http://localhost:8000`.

## 10-page structure
1. `index.html` — Home
2. `dashboard.html` — Dashboard
3. `trends.html` — National trends
4. `states.html` — State comparison
5. `road-users.html` — Road users
6. `demographics.html` — Demographics
7. `risk-factors.html` — Risk factors
8. `explorer.html` — Data explorer and CSV export
9. `about-data.html` — Dataset, integration and limitations
10. `about.html` — Project, architecture, accessibility, privacy and security

## Technology
- HTML5 semantic structure
- CSS3 responsive layouts and custom properties
- Vanilla JavaScript
- Local structured data in `data/roadlens-data.js` and `data/roadlens-data.json`
- Canvas charts with accessible data-table alternatives
- PWA manifest and service worker when served over HTTP/HTTPS

## Responsive design
Each page includes a live Desktop / Tablet / Mobile preview control. The layout also uses CSS media queries for normal responsive behaviour.

## Security, privacy and ethics
- restrictive Content Security Policy on all pages;
- no third-party scripts, advertising, analytics, cookies or logins;
- safe new-tab link attributes;
- aggregate public data rather than individual-level fatality records;
- local-only feedback demonstration;
- transparent source limitations and preliminary-data warning.

See `SECURITY.md`, `PRIVACY.md` and `DATA_SOURCE.md`.

## Git and collaboration workflow
The project is synchronized through the repository using a task branch and pull-request workflow. Guidance is documented in `CONTRIBUTING.md` and `COLLABORATION.md`.

The current final-sync branch is:
`feature/roadlens-final-sync`

## QA
Run:
```bash
python scripts/qa_check.py
```

The same validation runs through `.github/workflows/qa.yml` on GitHub pushes and pull requests. The local final run on 4 September 2026 passed all configured checks.

## Data source
Australian Government National Road Safety Data Hub, *Monthly road deaths*, aggregate data through June 2026. Recent figures are preliminary and subject to revision.

## Academic submission note
Repository history produced on 4 September 2026 is genuine evidence of the final synchronization and repository-preparation process. It should not be presented as proof that earlier development work occurred on those commit dates. SPARK and group-contribution statements should use genuine team records.
