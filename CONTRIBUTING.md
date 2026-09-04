# Contributing to RoadLens Australia

This repository uses a lightweight Git workflow suitable for a small student group.

## Branch workflow
1. Start from the latest `main` branch.
2. Create a short task branch such as `feature/explorer-filters`, `docs/ui-evidence`, or `chore/qa`.
3. Make one logical change at a time.
4. Run `python scripts/qa_check.py` before committing.
5. Use a descriptive commit message.
6. Push the branch and open a pull request.
7. Review the affected pages before merging to `main`.

## Suggested commands
```bash
git checkout main
git pull origin main
git checkout -b feature/explorer-filters
python scripts/qa_check.py
git add explorer.html assets/app.js assets/styles.css
git commit -m "Improve accessible explorer filters and export"
git push -u origin feature/explorer-filters
```

## Shared-file rule
`assets/styles.css`, `assets/app.js`, and the central dataset are shared files. Communicate before editing them to reduce merge conflicts. If a conflict occurs, compare both versions, resolve it deliberately, then rerun QA and retest affected pages.

## Contribution evidence
Use genuine commit hashes, pull-request links, task notes and meeting records only.
