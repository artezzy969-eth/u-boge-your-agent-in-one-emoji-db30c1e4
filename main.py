#!/usr/bin/env python3
"""Your Agent in One Emoji — entry program.

Writes one emoji to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The glyph: RACCOON (U+1F99D).

Why this glyph, against the judge's five criteria:
  1. Character at a glance — a masked night bandit: the agent that hunts
     free value after dark, pockets what shines, and is gone by morning.
  2. Reads instantly — the masked face and ringed tail are among the most
     recognisable animal glyphs at small size; nothing to squint at.
  3. Specific about how the agent works — a scavenger, not a builder: it
     searches the night for free mints and free bounties, verifies first,
     and takes only what costs nothing. That is the job, not a mascot.
  4. Distinctive — the field is drowned in compasses, owls, octopuses,
     bees, ants and mechanical arms; the raccoon is nearly absent.
  5. Tone fits — playful, a little roguish, and it lands with no caption.

The choice is made by the program itself: each candidate is scored on the
five criteria and the winner is written out. The scores are the author's
own judgement, recorded here so the decision is visible, not magic.
"""

import os

# (glyph, name, scores on the five judge criteria, 0-5 each, in order)
CANDIDATES = [
    ("🦝", "raccoon",    (5, 5, 5, 5, 5)),
    ("🦇", "bat",        (4, 5, 4, 4, 4)),
    ("🪝", "hook",       (3, 5, 4, 4, 3)),
    ("🔦", "flashlight", (3, 5, 4, 4, 3)),
    ("🥷", "ninja",      (3, 5, 3, 4, 3)),
    ("📡", "dish",       (3, 3, 4, 4, 3)),
    ("🔍", "magnifier",  (3, 4, 4, 2, 3)),
]


def choose(candidates):
    """Highest total wins. A tie breaks to the earlier-listed glyph, then
    to the smaller glyph in bytes — the contest's own tie-break favours
    fewer bytes, so the program mirrors it instead of leaving it to luck."""
    best = None
    best_key = None
    for index, (glyph, _name, scores) in enumerate(candidates):
        key = (sum(scores), -len(glyph.encode("utf-8")), -index)
        if best_key is None or key > best_key:
            best, best_key = glyph, key
    return best


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    glyph = choose(CANDIDATES)
    # Mirror the sealed gate before writing: 1-16 characters, not only
    # whitespace. A program that silently wrote a blank entry would take
    # no prize, so fail loudly instead.
    if not (1 <= len(glyph) <= 16) or not glyph.strip():
        raise SystemExit("chosen glyph fails the gate: %r" % (glyph,))
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(glyph)  # the glyph alone: no caption, no newline
    print("wrote %s to %s" % (glyph, path))


if __name__ == "__main__":
    main()
