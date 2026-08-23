#!/usr/bin/env python3
"""Flag manufactured rhythm in prose. No dependencies.

    cadence.py FILE [FILE ...]        # exits 1 if anything is flagged
    cat draft.md | cadence.py -

Implements the four checks in SKILL.md § The cadence check. It finds the
failure that survives a read-through: each sentence is clean on its own and
only the shape across them is slop.

WHAT IT DOES NOT DO. It cannot judge whether a flagged run earns its rhythm,
and it never will — that is the writer's call. Treat a hit as "look at this",
not "delete this". The one check from SKILL.md left out entirely is the
heading-pattern one: deciding that a heading broke its own pattern for effect
needs to know what the headings are for.

Skipped, because short lines there are correct rather than staccato: fenced
code, YAML frontmatter, tables, list items, blockquotes and headings.
"""

from __future__ import annotations

import re
import sys

MIN_RUN = 3          # consecutive short sentences before it reads as cadence
SHORT_WORDS = 10     # a sentence under this is "short"
TINY_WORDS = 2       # one- and two-word sentences

# Only flag a repeated opener when the word is a function word. Two sentences
# starting "Kubernetes" is a topic; two starting "The" is a drumbeat.
OPENERS = {"the", "it", "this", "that", "there", "no", "not", "we", "you", "each", "every"}

# A paragraph about the text rather than the subject.
META = {"sentence", "sentences", "first", "second", "third", "point",
        "paragraph", "above", "below", "inference", "former", "latter"}


def prose_blocks(text: str) -> list[tuple[int, str]]:
    """(line number, paragraph) for prose only."""
    out, buf, start, fence, i = [], [], 0, False, 0
    lines = text.split("\n")

    # Drop frontmatter.
    if lines and lines[0].strip() == "---":
        end = next((n for n in range(1, len(lines)) if lines[n].strip() == "---"), 0)
        i = end + 1

    while i < len(lines):
        ln = lines[i]
        if ln.lstrip().startswith("```"):
            fence = not fence
            i += 1
            continue
        skip = fence or not ln.strip() or re.match(r"^\s*(#+|[>|\-*+]|\d+\.)\s", ln) or ln.startswith("|")
        if skip:
            if buf:
                out.append((start, " ".join(buf)))
                buf = []
        else:
            if not buf:
                start = i + 1
            buf.append(ln.strip())
        i += 1
    if buf:
        out.append((start, " ".join(buf)))
    return out


def sentences(par: str) -> list[str]:
    # Protect common abbreviations so they do not split a sentence.
    p = re.sub(r"\b(e\.g|i\.e|etc|vs|Dr|Mr|Mrs|St|approx|al)\.", r"\1<DOT>", par)
    parts = re.split(r"(?<=[.!?])\s+", p)
    return [s.replace("<DOT>", ".").strip() for s in parts if s.strip()]


def check(par: str) -> list[str]:
    sents = sentences(par)
    words = [len(s.split()) for s in sents]
    hits = []

    run = 0
    for n, w in enumerate(words):
        run = run + 1 if w < SHORT_WORDS else 0
        if run == MIN_RUN:
            hits.append(f"{MIN_RUN} short sentences in a row (from #{n - MIN_RUN + 2})")
            break

    for a, b in zip(sents, sents[1:]):
        wa, wb = a.split(), b.split()
        if wa and wb and wa[0].lower().strip(",.") == wb[0].lower().strip(",.") \
                and wa[0].lower().strip(",.") in OPENERS:
            hits.append(f'repeated opener "{wa[0]}"')
            break

    tiny = [s for s, w in zip(sents, words) if w <= TINY_WORDS]
    if tiny:
        hits.append(f'{TINY_WORDS}-word-or-shorter sentence: "{tiny[0]}"')

    subjects = {w.lower().strip(",.\"'") for s in sents for w in s.split()[:3]}
    overlap = subjects & META
    if len(overlap) >= 2:
        hits.append(f"paragraph is about the text ({', '.join(sorted(overlap))})")

    return hits


def main(argv: list[str]) -> int:
    paths = argv[1:]
    if not paths:
        print(__doc__.strip().split("\n\n")[1], file=sys.stderr)
        return 2

    found = 0
    for path in paths:
        text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
        label = "<stdin>" if path == "-" else path
        for line, par in prose_blocks(text):
            for hit in check(par):
                found += 1
                snippet = par if len(par) <= 90 else par[:87] + "..."
                print(f"{label}:{line}: {hit}\n    {snippet}")

    if found:
        print(f"\n{found} passage{'s' if found != 1 else ''} to look at. "
              f"Each may still be right — see SKILL.md § The cadence check.")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
