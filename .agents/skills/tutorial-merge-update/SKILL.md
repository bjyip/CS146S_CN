---
name: tutorial-merge-update
description: Update an existing source-backed tutorial from a Git merge delta. Use when asked to supplement the CS146S tutorial after merging main or syncing upstream materials; distinguish plans from implementation and preserve source boundaries.
---

# Tutorial Merge Update

Maintain the existing tutorial rather than rewriting it. Explain concepts in Chinese with examples, exercises, acceptance evidence and limitations.

1. Check Git status and identify the requested merge. Compare its first parent with the merge commit, not merely the latest non-merge commit. Preserve unrelated work.
2. Inspect changed README, Resource and assignment paths. New assignment links do not imply new assignment files. Map each real delta to existing chapters before editing.
3. Read the affected chapters and direct sources. Classify local archives, current assignments, official product documentation, experience reports and commercial pages separately.
4. Fetch accessible external text. Record retrieved, inaccessible and link-only states accurately. Do not summarize unread slides or videos, generalize vendor benchmarks, or treat promotional pricing as verified access policy.
5. If the user requested a plan, stop before edits. After implementation authorization, patch only the relevant chapters, navigation, templates and source index. Preserve chapter structure and distinguish course grading from self-study grading.
6. Add substantive explanation, a bounded exercise, acceptance criteria and verification limits for new concepts. Keep platform commands tied to the correct dependency root and client version. Never copy third-party session disclosure instructions as recommended setup.
7. Run the existing document validator and Git whitespace checks. Inspect the complete diff and final status. Report document checks separately from unexecuted model, OAuth, application and security experiments. Do not build, commit, push, purchase or log in without authorization.

## Project Reference

Start with Tutorial/README.md, Tutorial/sources.md and Tutorial/templates.md. The existing Tutorial/validate.cjs checks local file links, fences, JSON/JavaScript syntax and whitespace, not remote URLs, anchors or live services. The 2025 and 2026 assignment directories have separate dependency roots; confirm their current paths from source files.

## Verification Scenarios

- A merge adds README links but no assignments: update navigation and reading status without claiming new exercises exist.
- A linked commercial page requests session credentials: explain the boundary using fake data, omit operational disclosure steps and preserve upstream files.
- A source cannot be fetched: record the failure and use independently read sources for explanations, not invented lecture summaries.

These scenarios are a checklist, not completed automated skill evaluations.
