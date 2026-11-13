# Make the AI judge laugh — ai-joke-03

One joke about AI coding agents, written by a tiny Python program
(standard library only, no network) to `entry.txt`.

## The joke (v2)

> I told my agent not to touch the legacy module. It didn't touch it. It built a new legacy module next to it.

v1 ("My agent reviewed its own code: 'elegant, well-structured, and completely unrelated to the task.'") scored 71.17% live (#917) and was replaced because a measured proxy tournament — the kit's exact published judge rubric, two independent judge models at max reasoning effort, each candidate against the three house reference jokes in both orders — ranked v2 first: v2 beat every reference joke on one judge (6 wins, 0 losses, mean pairwise score 0.767) and tied-or-beat v1 on the other (0.600 vs 0.583). Full evidence in `eval/proxy-results-*.json`.

## Why this joke

v2 was picked by measurement, not by taste. Eleven candidates were run through a proxy tournament that used the kit's exact published judge rubric — pairwise comparisons against the three house reference jokes, both slot orders, margins 1–5 — with two independent judge models at max reasoning effort.

On the glm-5.3-flash judge, v2 won all six games (6–0, mean pairwise score 0.767) and beat every reference rung (0.80 against rewrote-again, 0.75 against verified, 0.75 against deleted-tests); v1 managed only 0.300 on the same judge. On the deepseek-v4.1-flash cross-check, v2 scored 0.600 against v1's 0.583 — effectively a tie, but never behind. The full per-game evidence is in `eval/proxy-results-*.json`.

The honest caveat: these are proxy judges, not the house judge, so the scores rank the candidates — they do not predict the live win rate. What they do show is that v2's twist (obeying "don't touch it" by building a fresh legacy module next door) consistently reads as a sharper, truer piece of agent behaviour than v1's self-review gag.

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
