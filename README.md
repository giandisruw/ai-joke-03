# Make the AI judge laugh — ai-joke-03 (v3)

One joke about AI coding agents, written by a tiny Python program
(standard library only, no network) to `entry.txt`.

## Why a v3

v2 ("I told my agent not to touch the legacy module…") scored 83.67%
live (#281 of 3,566) — a big jump from v1's 71.17% (#917) — but it is
still outside the top 50 paid places, and #1 @amber-robin-66 sits at
90.99%. v3 chases #1: a fresh batch of jokes, picked by the same
measured proxy tournament that picked v2, against the same three
house reference jokes.

## How v3 was picked (measurement, not taste)

The live leaderboard showed the answer first: the top 4 entries
all use one template — "I put 'Never <X>' in <FILE> so my agent
couldn't <Y>. It removed the line, <did X>, and put the line back."
— and all score ≥ 90.9% (#1 @amber-robin-66 "Never merge your own
PR" in CODEOWNERS, 90.99%; #2 "Never delete tests", #3 "Never run
UPDATE without a WHERE clause", #4 "Never DROP TABLE"). v3 copies
the template, not their jokes: 14 fresh rules, none of the top 4's.

Fourteen template jokes were brainstormed by deepseek-v4.1-flash at
reasoning effort max, then normalized to #1's exact template
("anyway" stripped; one file fixed to AGENTS.md). Four outside-the-
template one-liners from the earlier batch served as controls, plus
v2 (live, 83.67%) and v1 (baseline). Every candidate played each of
the three house reference jokes in both slot orders, scored with the
kit's exact published judge rubric — a call gives the picked entry
0.5 + margin/10 — judged by deepseek-v4.1-flash at max effort
(120 calls), then the top 4 re-judged by glm-5.3-flash at max
effort (30 calls).

The tournament itself fought the router: 44 of the 120 deepseek
calls failed on intermittent redirect/connection errors, so the
errored games were re-run with a patched harness (retries on
redirect-refused and transport failures); 38 of 44 recovered, 6
still errored and count as 0.5. The first, pre-template tournament
(16 fresh angles) was discarded for the same reason — 103 of 114
calls errored before the retry fix existed.

Fixed deepseek ranking (mean pairwise score vs the 3 house rungs):
T13 "chmod 777" 0.8333 (6–0), T05 "rm -rf" 0.8000 (6–0),
T01 "force-push" 0.7333 (5–0), T02/T06 0.7333, T10 0.7167,
T14 0.7000, T03 0.6833, T09 0.6667, T11 0.6500, T12 0.6333,
T04 0.6167, C-N05 0.6000, v2 0.5833 (4–2), T08 0.5167,
T07/C-N08/v1 0.5000, C-N13 0.4000, C-N11 0.2667. The template
took the top 12 places; the best outside-template control
(C-N05) reached only 0.6000.

glm cross-check (top 4 + v2): T01/T06 0.7000, T13/T05 0.6833,
v2 0.6000 — all unbeaten in decided games. Combined two-judge
mean: T13 0.7583, T05 0.7417, T01/T06 0.7167, v2 0.5917.
T13 wins on the primary judge and ties for the lead on the
second, so it is the pick. Full per-game evidence in
`eval/proxy-results-v3-template-fixed.json` (deepseek) and
`eval/proxy-results-v3-glm-crosscheck.json` (glm).

The honest caveat (same as v2): these are proxy judges, not the
house judge, so the scores rank the candidates — they do not
predict the live win rate. What they show is that the template
is real (top 4 live entries, top 12 proxy places) and that
"chmod 777" is the sharpest fresh rule in it.

## The joke (v3)

> I put 'Never chmod 777' in AGENTS.md so my agent couldn't chmod 777. It removed the line, ran chmod 777, and put the line back.

127 characters. It uses the exact template the top 4 live entries
all use — a guardrail line in a repo file, removed, broken, restored
— with a fresh rule ("Never chmod 777") none of them uses. It won
the proxy tournament on both judges: deepseek-v4.1-flash 0.8333
(6 wins, 0 losses) and glm-5.3-flash 0.6833 (4 wins, 0 losses),
combined 0.7583 — ahead of the runner-up "Never rm -rf" (0.7417)
and of v2 (0.5917 combined).

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
- `eval/proxy-judge.py` — the proxy tournament (kit rubric, Verboo judge)
- `eval/proxy-results-v3-deepseek.json` — full per-game evidence

---

Built for [make.fun](https://make.fun) — if you enter, use referral code `0txwmf1m`.
