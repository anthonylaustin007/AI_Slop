# Changelog

## 1.1.0 — 2026-08-21

Cadence: the failure the skill named but could not catch.

- `SKILL.md`: new "The cadence check" section. Four mechanical tests — runs of
  three or more short sentences, repeated sentence openers, one- and two-word
  sentences, and paragraphs whose subjects are *sentence / first / second /
  point*. Failure mode 1 already listed staged cadence and rhetorical triads,
  and the revision pass already said to sweep for manufactured rhythm; naming it
  again would not have helped. The gap was that recognising rhythm by
  re-reading is unreliable, because re-reading is how it gets written.
- `SKILL.md`: revision pass step 3 now routes manufactured rhythm to those
  checks instead of repeating the instruction that did not work.
- `references/failure-modes.md`: three multi-sentence examples. Every existing
  example in the bank is a single sentence, so nothing demonstrated the version
  of this failure where each sentence passes alone and only the shape across
  them is slop. All three are real cases that shipped past a writer with this
  skill loaded.
- Guard against over-correction: the new section states that short sentences
  carrying real facts are not the target, with an example that must not trip.

## 1.0.0 — 2026-08-21

Initial release.

- `slop-free-writing` skill: the grading standard, four failure modes with fixes and do-not-flag rules, good-writing requirements, formatting defaults, and a five-step revision pass.
- `references/failure-modes.md`: 15 rewrite pairs, the full bad-example bank across all four categories, ~30 labeled calibration cases from reviewer exercises, and the formatting/overstyling reference.
- `dist/slop-free-writing.skill`: packaged build for direct upload to Claude.
