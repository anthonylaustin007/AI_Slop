# Changelog

## 1.3.0 — 2026-08-24

Vocabulary and whole documents.

- `SKILL.md`: new "Vocabulary" section. The old list was eleven words. The new
  one is 118 words and phrases, in five groups named for the job the word does:
  verbs that inflate an action (leverage, spearhead, streamline), adjectives
  that assert quality with the evidence removed (robust, seamless,
  comprehensive), nouns that gesture at scale (landscape, ecosystem, journey),
  stock phrases that fill the slot where the point should be (at its core,
  it's worth noting, moving forward), and transitions doing work the sentences
  should do (Additionally, Moreover, Firstly). Each group says what to put in
  the word's place, and the section keeps the rule that no word is banned:
  the signal is three or more in a paragraph with no number, source, or
  decision. A "Keep" list covers terms of art.
- `SKILL.md`: two sub-patterns added. Reader flattery as an opener (failure
  mode 1): praise for the reader's company or work before anything the reader
  needs. Echoing the brief (failure mode 4): the request's own phrases
  returned as if they were findings.
- `references/failure-modes.md`: section 8, the vocabulary list with a
  before/after pair for each group. Section 10, two complete documents (an
  internal status memo, an email to a customer) rewritten start to finish,
  with every cut labeled by failure mode, a list of what survived, and, for
  the memo, what a rewrite cannot fix: the original was hiding two facts the
  writer did not have, and the rewrite leaves brackets rather than inventing
  them. The cadence section is now numbered 9 and listed in the contents.
- `scripts/cadence.py`: three false positives fixed. A bare `>` between
  quoted paragraphs, a horizontal rule, and a line that is only an HTML tag
  (the anchors in the reference file) were each being read as a one-word
  sentence. Run over `failure-modes.md`, hits drop from 18 to 11, none of them
  in the new sections.

## 1.2.0 — 2026-08-21

- `slop-free-writing/scripts/cadence.py`: the cadence checks as a runnable
  script. No dependencies, reads files or stdin, exits non-zero on a hit so it
  can gate CI. Skips code fences, frontmatter, headings, tables, lists and
  blockquotes, where short lines are correct rather than staccato.
- `SKILL.md`: the cadence section now points at the script, and says plainly
  that it flags rather than judges — a paragraph genuinely about two sentences
  trips check 4 and is right to.
- `references/failure-modes.md`: a "do not flag" counterexample showing exactly
  that case, so the output is not read as a linter that must reach zero.

Run against the three articles that prompted version 1.1.0, the script found a
fourth passage the hand edit had missed ("It does not need to be long. It needs
to be the same.") and caught one bug in itself: headings deeper than `#` were
being parsed as prose.

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
