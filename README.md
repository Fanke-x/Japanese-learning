# JLPT N1 Prep Repo (Tailored for a Chinese native)

This repo is your structured, self-study toolkit for JLPT N1. It’s optimized for Chinese speakers who already understand a lot of kanji semantics but need to master Japanese readings, grammar nuance, and usage.

## What’s inside

- `vocab/` — Core vocabulary sets (target: 900). CSV format for easy import to Anki/Quiz tools.
- `grammar/` — 100 advanced patterns with CN glosses and brief notes.
- `kanji/` — Kanji readings, pitfalls for Chinese speakers, and false-friend notes.
- `reading/` — Short reading passages with questions and answer keys.
- `tools/` — Minimal Python quiz tool and converters.

## Suggested 12-week roadmap

- Mon–Fri: 60–90 min/day (Vocab 30, Grammar 20, Reading 20+). 10–15 min listening shadowing.
- Sat: 2–3 hrs mock reading/listening, error log review, targeted drills.
- Sun: Light review + reset decks.

Focus areas for Chinese learners:

- Readings over meanings: Don’t rely on meaning recognition via kanji. Drill readings (音読み/訓読み, 重箱読み/湯桶読み) and accent.
- Grammar nuance: 接続, 主観/客観, 書き言葉 vs 話し言葉, 曖昧さ回避。
- Collocations: 動詞＋助詞, 慣用句, 連体修飾の距離。
- Register: 書き言葉（〜に即して／〜に鑑み） vs 口語（〜っぽい）混用注意。

## How to use

1) Start with `vocab/core_words_001-150.csv` (readings + CN meaning). Make cards you miss.
2) Each day pick 1–2 patterns from `grammar/grammar_100.csv`. Rephrase 2 example sentences of your own.
3) Do one `reading/` passage every 1–2 days. Answer questions, then check the key.
4) Run `tools/quiz.py` for quick CLI drills. Export TSV to import into Anki if you prefer.

## File formats

- Vocab CSV: id,kanji,reading,pos,meaning_zh
- Grammar CSV: id,pattern,meaning_zh,notes
- Kanji pitfalls CSV: kanji,jp_meaning_zh,cross_lang_note

## Milestones

- Week 2: 150 words + 20 grammar + 4 readings.
- Week 4: 300 words + 40 grammar + 8 readings.
- Week 8: 600 words + 80 grammar + 16 readings.
- Week 12: 900 words + 100 grammar + 20 readings + 2 full mock papers.

If you want, we can keep adding the remaining vocab files in 100-word batches until you reach 900.
