# Tools

- quiz.py — Quick CLI quiz for vocab/grammar from CSV files.
- export_to_tsv.py — Convert a vocab/grammar CSV to Anki-friendly TSV.
- datasets — Uses files from ../vocab and ../grammar

Quiz usage:

- Default: random 10 vocab and 5 grammar using the provided datasets.
- Options:
  - --vocab path/to/csv
  - --grammar path/to/csv
  - --n-vocab 20
  - --n-grammar 10

Export usage:

- Vocab to TSV (front=kanji/pos, back=reading + CN):
  python export_to_tsv.py --type vocab --in ../vocab/core_words_001-150.csv --out vocab_001-150.tsv

- Grammar to TSV (front=pattern, back=CN + notes):
  python export_to_tsv.py --type grammar --in ../grammar/grammar_100.csv --out grammar_100.tsv

- Reading-focused deck (front=reading, back=kanji + CN):
  python export_to_tsv.py --type vocab --in ../vocab/core_words_001-150.csv --out vocab_reading_001-150.tsv --front reading --with-meaning
