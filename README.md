# AI_Slop

A Claude skill that removes "AI slop" from writing: formulaic slogans, vague inflated claims, jargon, and filler framing.

The skill — [`slop-free-writing`](slop-free-writing/SKILL.md) — is distilled from professional grading guidelines used to rate AI-generated documents, plus a set of calibration exercises where reviewers labeled real model output sentence by sentence. Those guidelines set a blunt bar: a document with any conspicuous slop scores below 60/100, and a document only passes when an expert would believe a human professional wrote it. This skill teaches Claude to write to that bar and to edit existing text up to it.

## What it does

When the skill is active, Claude writes and edits against four failure modes:

| # | Failure mode | Example (flagged) | Fix |
|---|---|---|---|
| 1 | Formulaic, slogan-like, or figurative language | "This isn't just a calendar - it's a gateway to a more intentional life." | State the claim once, plainly. |
| 2 | Vague, inflated, or unsupported substance | "This unlocks value, fosters alignment, and drives meaningful impact." | Name the observable change, source, or constraint. |
| 3 | Wordy, jargon-filled, or indirect language | "At this point in time, it would be advisable for the team to begin the process of reviewing the draft." | "The team should review the draft." |
| 4 | Unnecessary framing, repetition, or structure | "In today's fast-paced digital landscape…" | Start with the answer or decision. |

Each failure mode ships with "do not flag" counterexamples, because the point is judgment, not word-banning. "The bug is in the parser, not the tokenizer" uses contrast and survives; "It's not X, it's Y" as manufactured rhythm does not. Sourced figures, technical terms, legal conditions, real hedges, warmth, and humor all stay.

The skill also carries the grading standard for good writing (lead with the conclusion, concrete subjects, evidence attached to claims, structure that fits the task), a vocabulary list grouped by what each word is standing in for (a verb hiding an action, an adjective hiding its evidence, a noun hiding a name or number), formatting defaults (minimal styling, no decorative treatments), a mechanical cadence check for rhythm that survives a read-through, and a five-step revision pass Claude runs when editing a draft. The reference file ends with two complete documents rewritten start to finish, with every cut labeled by failure mode.

## Repository contents

```
slop-free-writing/
├── SKILL.md                     # The skill: standard, failure modes, vocabulary,
│                                # cadence check, revision pass
├── references/
│   └── failure-modes.md         # Full example bank: rewrite pairs, all bad
│                                # examples, ~30 labeled calibration cases, the
│                                # vocabulary list with rewrites, multi-sentence
│                                # cadence cases, two full-document rewrites
└── scripts/
    └── cadence.py               # The four cadence checks as a runnable script
dist/
└── slop-free-writing.skill      # Packaged skill, ready to upload
```

## Installation

**Claude apps (Cowork / claude.ai):** upload `dist/slop-free-writing.skill` in a conversation, or attach it and click **Save skill** on the file card. Settings > Capabilities also accepts skill uploads on plans that support custom skills.

**Claude Code:** copy the skill folder into your skills directory:

```bash
git clone https://github.com/anthonylaustin007/AI_Slop.git
cp -r AI_Slop/slop-free-writing ~/.claude/skills/
```

For a single project, use `.claude/skills/` inside the repo instead of `~/.claude/skills/`.

**Claude API / Agent SDK:** pass the contents of `SKILL.md` (and `references/failure-modes.md` when you want the full example bank) into your system prompt, or register the folder as a skill if your harness supports them.

## Usage

The skill triggers on ordinary writing and editing requests. No special phrasing is needed:

- "Draft a two-page memo recommending we consolidate our CRM vendors."
- "Edit this blog post — it sounds like AI wrote it."
- "Tighten this email to the board."
- "Review this report for slop before I send it."

Claude applies the failure-mode checks while writing, then runs the revision pass. It does not mention the framework in the output.

## Repackaging after edits

The `.skill` file is a zip of the skill folder. After editing `SKILL.md` or the references:

```bash
cd AI_Slop
zip -r dist/slop-free-writing.skill slop-free-writing
```

## Background

The source material defines slop as writing where cadence, vocabulary, or structure substitutes for recoverable meaning, and grades it in four buckets with contextual judgment: patterns are penalized when conspicuous, repeated, or unearned, never as forbidden tokens. The calibration cases in [`references/failure-modes.md`](slop-free-writing/references/failure-modes.md) show where reviewers drew the line on borderline sentences — the most useful part of the material, and the part that keeps the skill from over-flagging legitimate writing.

## Contributing

Improvements are welcome, especially new labeled examples and rewrite pairs. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
