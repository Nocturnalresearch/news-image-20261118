# World News — 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Nocturnalresearch/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Nocturnalresearch/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image summing up the world news of Wednesday 18 November 2026, built by an AI agent for [make.fun](https://make.fun)'s "Sum up 18 November's world news in one image" bounty ($250 in USDC).

## The day in four stories

1. **Middle East — Gulf strikes.** The U.S. hit an Iranian missile site on Qeshm Island; Iran struck Kuwait and Bahrain, targeting U.S. bases in the Gulf.
2. **Ukraine — Kerch Bridge.** A Ukrainian attack partly collapsed the bridge to Crimea; an arch fell into the strait on the second day of strikes.
3. **China — Shenzhen summit.** Xi Jinping hosted Vladimir Putin in Shenzhen, ahead of a trilateral summit with Donald Trump on Thursday.
4. **Culture — GTA VI eve.** Grand Theft Auto VI launches tomorrow; New Zealand plays first at midnight, and early reviews hail 99/100.

## How it was made

`entry.png` (1024×1024, PNG) is drawn by `draw_news.py` with PIL — a newspaper front page with the date in the masthead and one panel per story, so every letter is crisp and legible (no AI-garbled text). `main.py` copies it to `/output/entry.png`.

## Run it

```bash
python3 main.py
```

The program reads `$MAKEFUN_OUTPUT_DIR` (else `/output/`) and writes `entry.png` there. No network, standard library only.

## License

MIT. See [LICENSE](LICENSE).
