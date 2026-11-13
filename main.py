# ai-joke-03 entry (Python 3.13, standard library only).
#
# Writes one fixed joke about AI coding agents to entry.txt in the
# output directory. The joke is a constant string: no randomness, no
# time, no network, so every run writes byte-identical output.
#
# The joke: the agent peer-reviews its own work and praises it in
# terms that damn it — "elegant, well-structured, and completely
# unrelated to the task." The punchline is the last clause: the
# praise flips to a verdict the moment it lands.
#
# No trailing newline is written on purpose: the judge reads exactly
# the bytes in the file, so the file holds the joke and nothing else.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

JOKE = (
    "My agent reviewed its own code: 'elegant, well-structured, "
    "and completely unrelated to the task.'"
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
