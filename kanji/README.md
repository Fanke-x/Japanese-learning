# Kanji — Learning Resources and Strategy (for a Chinese native)

Use this folder to focus on readings (音/訓), pitch accent, radicals, and false friends.

## Core resources (free)
- OJAD (Online Japanese Accent Dictionary): https://www.gavo.t.u-tokyo.ac.jp/ojad/
  - Check pitch accent for words; try Prosody Tutor Suzuki-kun for sentence prosody.
- Jisho: https://jisho.org/
  - Kanji details, on/kun, frequency tags, JLPT tags, example sentences.
- Kanjipedia (日本漢字能力検定協会): https://www.kanjipedia.jp/
  - Authoritative kanji meanings, readings, 熟語 examples (JP only).
- KanjiAlive: https://app.kanjialive.com/
  - Stroke order animations, on/kun, mnemonics.
- Kakijun.jp (書き順): https://kakijun.jp/
  - Stroke order for many characters.
- KanjiVG (decomposition data): https://kanjivg.tagaini.net/
  - Component breakdowns (for structure awareness).

## How to study (quick plan)
- Readings first: annotate on/kun in your decks (use tools/annotate_on_kun.py as a guide; override exceptions manually).
- Pitch matters: check OJAD for high–low pattern when you add a new word; say it aloud 3×.
- Components: learn 30–40 common radicals (see radicals_cheatsheet.md) to speed recognition.
- False friends: review pitfalls.csv regularly; produce your own example sentences to disambiguate.

## Repo tie-in
- Vocab CSVs → annotate 音/訓/混合: tools/annotate_on_kun.py
- Quick drills: tools/quiz.py (annotated CSV shows [音]/[訓/混合])
- Export to Anki TSV: tools/export_to_tsv.py

## Pitch-aware minimal pairs (check in OJAD)
- 雨(あめ) vs 飴(あめ)
- 橋(はし) vs 箸(はし) vs 端(はし)
- 紙(かみ) vs 神(かみ)
- 代わる vs 変わる（活用とアクセントに注意）

## Tips for Chinese speakers
- 同形異義警戒：例）手紙(信)／勉強(学习)／娘(女儿)（pitfalls.csv参照）
- 音読み=漢語っぽい語感、訓読み=和語っぽい語感（例外多数）。
- 自他ペア：増える/増やす、決まる/決める… 読みと格助詞のペアで暗記。

## Suggested books (optional, not included)
- 新完全マスター 漢字（N3→N1縦断で語彙も底上げ）
- 日本語アクセント入門（ピッチ意識づけに）
