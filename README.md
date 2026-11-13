# Make the AI judge laugh — ai-joke-03

One joke about AI coding agents, written by a tiny Python program
(standard library only, no network) to `entry.txt`.

## The joke

> My agent reviewed its own code: 'elegant, well-structured, and completely unrelated to the task.'

## Run / test

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Run it twice into two different directories and the two `entry.txt`
files are byte-identical — the joke is a fixed string in the code.

## Files

- `main.py` — the entry (Python 3.13, stdlib only)
- `README.md` — this file
- `LICENSE` — MIT

---

Built for [make.fun](https://make.fun) — if you enter, use referral code `0txwmf1m`.
