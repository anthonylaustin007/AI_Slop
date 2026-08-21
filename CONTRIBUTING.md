# Contributing

Contributions that make the skill sharper are welcome. The most valuable ones are labeled examples, because the skill's judgment lives in its example bank.

## Adding examples

New examples go in `slop-free-writing/references/failure-modes.md`, under the category they belong to. A good submission has three parts:

1. The flagged sentence, quoted exactly, with its sub-pattern named (for example "staged cadence" or "tacked-on benefit").
2. A rewrite that keeps the meaning and drops the slop. If the meaning cannot be recovered, say so — that is itself the diagnosis.
3. When the example is borderline, a note on why it falls on the slop side of the line.

Counterexamples are just as useful. If you find a construction the skill would wrongly flag — a real contrast, an accurate technical term, a hedge that marks a genuine unknown — add it to the relevant "Do not flag" list with a sentence on why it survives.

## Editing the skill itself

`slop-free-writing/SKILL.md` is what Claude loads on every writing task, so keep it under roughly 500 lines and push long material into `references/`. Two rules for edits:

- Explain why a pattern is a problem rather than adding bare prohibitions. The skill works by giving the model judgment, and judgment needs reasons.
- Follow the skill's own standard in your prose. A guide to slop-free writing that contains slop will not be merged.

## Testing changes

Test edits before opening a pull request: give Claude the updated skill and a few realistic writing prompts (a memo, an edit of deliberately sloppy text, a review request), and check that flagged patterns disappear while legitimate constructions survive. Claude's `skill-creator` skill can run this comparison systematically — with-skill against without-skill — if you want measured results. Include a before/after sample in the pull request description.

## Repackaging

After any change under `slop-free-writing/`, rebuild the distributable so it stays in sync:

```bash
zip -r dist/slop-free-writing.skill slop-free-writing
```

## Pull requests

Keep them small and single-purpose: one category of examples, or one section of the skill, per pull request. Describe what the change fixes with at least one concrete sentence the current version handles badly.
