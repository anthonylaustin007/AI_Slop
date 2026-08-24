---
name: slop-free-writing
description: Write clear, concrete, professional prose and strip out AI-slop patterns (formulaic slogans, vague inflated claims, jargon, filler framing). Use this skill whenever writing or revising any prose deliverable — reports, memos, emails, summaries, briefs, blog posts, slide text, meeting notes, web copy — and whenever the user asks to improve, tighten, edit, de-slop, or humanize text, or says writing "sounds like AI." Apply it even when the user doesn't mention slop; any substantive writing task benefits.
---

# Slop-Free Writing

## The standard

Professional reviewers grade AI writing on one blunt test: would an expert believe a human professional wrote this? In the grading rubric this skill is built from, a document with **any** conspicuous slop scores below 60/100, no matter how strong its structure or formatting. One slop-free page beats ten polished pages of filler.

The core rule behind everything below: **every sentence must carry meaning the reader can recover, verify, or act on.** Slop is what happens when rhythm, vocabulary, or structure substitutes for that meaning.

Treat the patterns below as contextual signals, not forbidden tokens. Flag a pattern when it is conspicuous, repeated, or unearned — an isolated phrase or punctuation mark in otherwise strong writing is fine.

## The four failure modes

### 1. Formulaic, slogan-like, or figurative language

The claim is understandable but packaged as a stock formula, slogan, staged cadence, canned emotional phrase, or strained metaphor instead of plain analysis. Includes colons, semicolons, and em dashes used to manufacture rhythm rather than clarify meaning.

Watch for:

- Inflated contrast: "This isn't just a calendar - it's a gateway to a more intentional life."
- Stock formulas: "not only saves time, but also transforms how teams collaborate"
- Negative parallelism: "not X, but Y" / "not just X, but Y" / "no X, no Y, just Z" / "It's not X, it's Y"
- Slogan fragments: "One team. One vision. Limitless possibilities." / "Pipeline is flat. Spend isn't." / "From paper-bound practicals to a shared digital workspace."
- Staged cadence and mannered punctuation: "Owners are set; risks are checked; approval is granted — and the launch moves forward." / "Universities: reinforce guidance. Students: reduce social activity."
- Rhetorical triads: "Faster, smarter, and more intuitive."
- Canned empathy: "I completely understand how frustrating this must feel."
- Reader flattery as an opener: praise for the reader's company, mission, or work before anything the reader needs. "I have long admired your team's commitment to excellence." The reader learns nothing about the writer and nothing they did not already know about themselves.
- Synthetic balance with no real tradeoff: "While remote work offers flexibility, it also presents unique challenges."
- Inflated significance: mundane facts recast as "legacy," "pivotal moments," an "evolving landscape"
- Promotional adjectives: vibrant, rich, renowned, groundbreaking, nestled
- Vague authorities: "experts argue," "observers note," "research consistently shows" with no source
- Canned endings: generic "challenges," "legacy," or "future outlook" conclusions
- AI-vocabulary clusters: delve, pivotal, robust, tapestry, underscore, showcase, foster, intricate, landscape, testament, vibrant, and the rest of the list under "Vocabulary" below. One is fine; three in a paragraph with no number, source, or decision is the signal.
- Overlong parallel enumerations — rhythmic catalogues that simulate exhaustiveness after the point is made
- Mechanical bold-label bullet walls (**Label:** explanation, repeated) when nobody asked for that structure

**Fix:** state the claim once, plainly. "The checklist is not just a tracker—it is the gateway to a more reliable release." → "The checklist shows which requirements are complete for release."

**Keep:** contrast and parallelism that state a real distinction. "The bug is in the parser, not the tokenizer" is good writing. So is "The red light means stop, and the green light means go."

### 2. Vague, inflated, or unsupported substance

The reader cannot tell what changed, why the benefit follows, what evidence supports the claim, or what reason drove the decision. Evidence, causality, actors, or observable meaning are missing.

Watch for:

- Empty abstraction: "This unlocks value, fosters alignment, and drives meaningful impact."
- Tacked-on benefits: "…ensuring a seamless user experience."
- Unsupported significance: "This represents a profound shift."
- Aphoristic compression that hides the point: "Public filings anchor the baseline. Controlled experiments must earn the forecast." / "Reliability and risk control are shipper value, not back-office hygiene."
- Process instead of reason: "After several rounds of cross-functional review, we aligned on the next phase."
- Metaphor instead of the number: "The next guide resets the bar higher" instead of "The next guide projects Q2 revenue at $91B."
- Oversimplification that loses the actual meaning: "Where to draw the line on speed investments" trimmed to "Where to draw the line."

**Fix:** name the observable change, the source, the deciding constraint, or the actual tradeoff. "The new intake form removes one approval step, unlocking value and driving meaningful impact." → "The new intake form removes one approval step."

**Keep:** claims carried by a concrete result, source, constraint, or approval requirement: "In Q1, fraud incidents fell 20% after tighter carrier onboarding." / "Legal and Security must approve the exception before release."

### 3. Wordy, jargon-filled, or indirect language

The rationale is clear but the wording is longer, more bureaucratic, more hedged, or more abstract than the meaning requires.

Watch for:

- Bureaucratic phrasing: "Stakeholders should be informed of the operational implications associated with this transition."
- Unnecessary verbosity: "At this point in time, it would be advisable for the team to begin the process of reviewing the draft." → "The team should review the draft."
- Unexplained jargon: "The workflow operationalizes a cross-functional enablement layer for downstream value realization."
- Compressed abstraction: "Events remain anchored to dual capacity constraints." → "Events are limited by both a headcount cap and a room-capacity percentage."
- Stacked hedges: "It may potentially be worth considering whether the team could possibly delay the launch."
- Overcomplicated sentence architecture — colon-and-semicolon towers where one plain sentence would do.

**Fix:** concrete subjects, strong verbs, the shortest accurate wording. Keep only uncertainty markers that correspond to real unknowns.

**Keep:** accurate technical terms, legal conditions, and explained uncertainty: "The API returns 429 when the client exceeds the rate limit." / "The estimate is preliminary because two regions have not reported."

### 4. Unnecessary framing, repetition, or structure

Setup, recap, or formatting delays the point or makes the document harder to scan.

Watch for:

- Generic scene-setting: "In today's fast-paced digital landscape…"
- Restating the request: "When it comes to improving employee onboarding, there are several strategies to consider."
- Echoing the brief: the request's own phrases returned as if they were findings. A brief that asks for "a customer obsessed roadmap" and gets back "this customer obsessed roadmap" has been quoted, not answered. Say what the roadmap does instead.
- Meta-announcements: "Below is a polished and comprehensive rewrite tailored to your needs."
- Redundant conclusions: "In conclusion, adopting these strategies can help organizations achieve their goals."
- Excessive structure: a two-sentence answer split across six headings and twelve bullets.

**Fix:** start with the answer or decision. Delete setup and recaps. Use the lightest structure that helps the reader act or find information.

**Keep:** framing that narrows scope, corrects the request, or helps readers navigate reference material: "This memo covers the two launch decisions due Friday."

## Vocabulary

These words are not banned. They are common in model output for one reason: each lets a sentence sound finished without saying what happened. When one appears, ask what plain word or fact it is standing in for. When three or more appear in a paragraph that has no number, source, or decision, rewrite the paragraph.

- Verbs that inflate an ordinary action: leverage, utilize, harness, unlock, empower, elevate, streamline, spearhead, bolster, foster, facilitate, drive, navigate, delve, underscore, showcase, embark, revolutionize, transform, optimize, ensure, enable. Each hides what was actually done. "Leveraged cross-functional partnerships" was, in fact, "asked Sales for the churn list."
- Adjectives that assert quality with the evidence removed: robust, seamless, comprehensive, holistic, transformative, innovative, cutting edge, dynamic, pivotal, crucial, critical, key, vital, essential, meaningful, impactful, actionable, scalable, powerful, strategic, intricate, nuanced, multifaceted, vibrant, rich, renowned, groundbreaking, world class, best in class, state of the art, ever evolving. If the system is robust, say what it survived.
- Nouns that gesture at scale instead of naming the thing: landscape, tapestry, testament, journey, realm, ecosystem, synergy, paradigm, cornerstone, beacon, game changer, north star, framework, solution, insights, value, impact, outcomes, alignment, stakeholders, the space. Name the customer, the number, the team, or the decision instead.
- Stock phrases that occupy the slot where the point should be: at its core, at the end of the day, it's worth noting, it's important to note, in today's world, in the ever evolving, in the realm of, dive into, deep dive, a wide range of, plays a crucial role, serves as, stands as, boasts, is a testament to, moving forward, going forward, navigate the complexities, the intersection of, when it comes to, whether it's X or Y, look no further, rest assured, I hope this finds you well, let's dive in, in a world where. Delete the phrase and read the sentence again: if it still stands, the phrase was filler; if it collapses, there was no sentence.
- Transitions doing work the sentences should do on their own: Additionally, Moreover, Furthermore, Firstly, Secondly, Lastly, Ultimately, Overall, In summary, In conclusion, In essence, Notably, Importantly, Crucially, Interestingly, That said, That being said, Simply put. A paragraph that needs Moreover three times is a list wearing prose; either make it a list or find the relationship between the sentences and state it.

**Keep:** any of these words used for its literal meaning or as a term of art, such as "landscape" in a piece about land, "robust standard errors" in statistics, "critical path" in a schedule, "framework" when it is React, "optimize" when there is a stated objective and a measurement, and "ensure" when it describes a mechanism ("the check ensures the file exists before the job starts"). The word is not the problem; the missing fact behind it is.

## What good writing looks like

A document passes when:

- It answers the task directly and leads with the conclusion or decision.
- Each major claim names a concrete subject and states an observable result, comparison, or constraint.
- Claims carry their evidence: a number, source, example, or approval requirement.
- Facts, interpretation, recommendation, and uncertainty are distinguished; caveats are local and specific, not blanket disclaimers.
- Every heading and bullet adds new information, and the amount of structure fits the task.
- The reader can tell what each finding changes for a decision, an owner, or a next action.
- Sentences are direct, with natural variation in length — prose Strunk and White would grade A+.

While cutting slop, protect what makes writing good: keep useful nuance (don't turn careful writing into overconfident writing), preserve deliberate warmth, humor, informality, and domain-specific terms, and never invent facts, context, commitments, or evidence to fill a gap.

## Structure and formatting defaults

The same rubric grades formatting on restraint. Most workplace documents should be minimal and clear — mostly black text on white, plain headings, native lists.

- Match structure to the document type: bullets suit meeting notes; an investment memo should not read like a news article; a legal brief is legitimately dense.
- Add styling only when the user asked for it or it is standard for the document type and genuinely aids reading.
- Avoid decorative rules, colored callouts and headings, three-part title treatments (eyebrow/title/subtitle), zebra striping, heavy borders, decorative separators (· | •), and charts or tables added for decoration rather than understanding.
- Prefer a simple list over a table unless rows and columns genuinely aid comparison; use native numbered lists, never text-shaped numbering like "1 |".

## The cadence check — run this, do not eyeball it

Failure mode 1 lists staged cadence and rhetorical triads, and the revision pass
says to sweep for manufactured rhythm. That is not enough on its own, because
every example in this skill is a **single sentence** and the hardest version of
this failure is **spread across several**. Each sentence passes inspection alone;
the slop is only visible in the shape they make together. You cannot catch that
by re-reading for meaning — re-reading is how it got written.

So run four mechanical checks over the draft. They take seconds and they do not
depend on taste.

1. **Runs of short sentences.** Three or more consecutive sentences under about
   ten words, in body prose. Real explanation varies in length; cadence does not.
2. **Repeated sentence openers.** Two or more consecutive sentences starting with
   the same word or the same frame — "The first… The second…", "It is… It is…",
   "No X… No Y…".
3. **One- and two-word sentences.** "Five." "Never." "That is the point." Almost
   always a staged reveal of something a full sentence could just say.
4. **Meta-paragraphs.** A paragraph whose subjects are *sentence, first, second,
   point, paragraph, above, below* is describing the text rather than adding to
   it. Delete it and check whether anything was lost.

Then the question that subsumes all four: **for each sentence, name the new fact
it carries.** A sentence that carries none is rhythm. Cut it or merge it.

`scripts/cadence.py` runs checks 1–4 over markdown or plain text, with no
dependencies, and exits non-zero when it finds something:

```
scripts/cadence.py draft.md          # or: cat draft.md | scripts/cadence.py -
```

It skips code fences, frontmatter, headings, tables, lists, blockquotes,
horizontal rules and bare HTML tags, where short lines are correct rather
than staccato. It cannot judge whether a
flagged run earns its rhythm, so treat a hit as "look at this". A paragraph
genuinely *about* two sentences will trip check 4 and be right to.

A caution in the other direction: short sentences are not banned. "The build is
broken. Rollback is at 4pm." is two facts in nine words. The test is whether each
one earns its full stop with information, not whether it is short.

## Revision pass

When editing a draft (yours or the user's), make one deliberate pass:

1. Delete throat-clearing, meta-announcements, restated requests, and redundant conclusions. Move the answer to the first sentence.
2. For each sentence ask: what changed, who did it, and how would the reader verify it? Rewrite around a concrete subject and verb; attach the number, source, or constraint if one exists. If none exists, either cut the claim or mark it honestly as interpretation — never fabricate support.
3. Sweep for the four failure modes above, especially "not X but Y" constructions, AI vocabulary, and tacked-on benefits. For manufactured rhythm run the four cadence checks — that failure hides from a read-through by design.
4. Compress. Keep real qualifications; cut stacked hedges and filler.
5. Final check: no invented facts, nuance intact, and an expert would believe a human professional wrote it.

Do not mention this framework or the editing process in the output unless the user asks.

For the full example bank — rewrite pairs, calibration cases showing which borderline sentences count as slop and which don't, and two documents rewritten start to finish with every cut labeled — read `references/failure-modes.md`.
