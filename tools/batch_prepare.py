#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOCAB_DIR = ROOT / 'vocab'
TOOLS_DIR = ROOT / 'tools'

HIRAGANA_RANGE = (0x3040, 0x309F)
KATAKANA_RANGE = (0x30A0, 0x30FF)


def has_kana(s: str) -> bool:
    for ch in s:
        code = ord(ch)
        if HIRAGANA_RANGE[0] <= code <= HIRAGANA_RANGE[1] or KATAKANA_RANGE[0] <= code <= KATAKANA_RANGE[1]:
            return True
    return False


def classify_on_kun(surface: str, reading: str):
    if has_kana(surface):
        return "訓/混合", "okuriganaあり → 和語/混合の可能性高"
    if len(surface) >= 2:
        return "音", "漢語（多く音読み）と推定"
    return "音", "既定（単漢字・要個別確認）"


def annotate_csv(inp: Path, outp: Path):
    with open(inp, encoding='utf-8') as f, open(outp, 'w', encoding='utf-8', newline='') as g:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['reading_type', 'reading_type_note'] if reader.fieldnames else None
        writer = csv.DictWriter(g, fieldnames=fieldnames)
        writer.writeheader()
        for r in reader:
            typ, note = classify_on_kun(r['kanji'], r['reading'])
            r['reading_type'] = typ
            r['reading_type_note'] = note
            writer.writerow(r)


def export_reading_tsv(inp: Path, outp: Path):
    with open(inp, encoding='utf-8') as f, open(outp, 'w', encoding='utf-8', newline='') as g:
        reader = csv.DictReader(f)
        for r in reader:
            reading = r['reading']
            kanji = f"{r['kanji']} ({r['pos']})"
            meaning = r.get('meaning_zh', '')
            back = f"{kanji} — {meaning}"
            g.write(reading + "\t" + back + "\n")


def main():
    csvs = sorted([p for p in VOCAB_DIR.glob('core_words_*.csv') if not p.name.endswith('_annotated.csv')])
    if not csvs:
        print('No vocab CSVs found.')
        return
    TOOLS_DIR.mkdir(parents=True, exist_ok=True)
    for src in csvs:
        stem = src.stem  # e.g., core_words_001-150
        annotated = src.with_name(stem + '_annotated.csv')
        tsv = TOOLS_DIR / (f'vocab_reading_{stem}.tsv')
        annotate_csv(src, annotated)
        export_reading_tsv(src, tsv)
        print(f"Annotated: {annotated}")
        print(f"Exported:  {tsv}")


if __name__ == '__main__':
    main()
