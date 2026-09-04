# Group Collaboration Workflow

## Work board
Use a simple four-stage board: **To do → In progress → Review → Done**.

Each task should record the owner, files likely to be changed, target completion date, review status, and the related branch/commit/pull-request link where applicable.

## Checkpoints
At brief group checkpoints, confirm task ownership, shared-file changes, blockers and completion dates. Decisions affecting multiple pages should be recorded in meeting notes or the approved group communication channel.

## Conflict resolution
When two members edit the same shared file:
1. pull the latest `main`;
2. compare both versions rather than overwriting one;
3. resolve the conflict intentionally;
4. rerun `python scripts/qa_check.py`;
5. manually retest all affected pages;
6. record the resolution in the pull request or task note.

## SPARK evidence
SPARK ratings and comments must be based on genuine contribution records. Repository commits, pull requests, task notes and meeting records can support those statements, but they do not replace honest peer evaluation.
