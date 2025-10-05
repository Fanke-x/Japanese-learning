#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import argparse
from pathlib import Path

HIRAGANA_RANGE = (0x3040, 0x309F)
KATAKANA_RANGE = (0x30A0, 0x30FF)


def has_kana(s: str) -> bool:
    for ch in s:
        code = ord(ch)
        if HIRAGANA_RANGE[0] <= code <= HIRAGANA_RANGE[1] or KATAKANA_RANGE[0] <= code <= KATAKANA_RANGE[1]:
            return True
    return False


def classify_on_kun(surface: str, reading: str) -> tuple[str, str]:
    # Simple heuristic:
    # - If surface contains any kana (okurigana) => 訓/混合
    # - Else if all kanji and multi-character: 音（漢語）
    # - Else fallback: 混合
    if has_kana(surface):
        return "訓/混合", "okuriganaあり → 和語/混合の可能性高"
    # Single-kanji nouns often have 音読み語基に派生; keep as 音 by default.
    if len(surface) >= 2:
        return "音", "漢語（多く音読み）と推定"
    return "音", "既定（単漢字・要個別確認）"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--in', dest='inp', required=True, help='Input vocab CSV')
    ap.add_argument('--out', dest='outp', required=True, help='Output annotated CSV')
    args = ap.parse_args()

    inp = Path(args.inp)
    outp = Path(args.outp)

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
    print(f"Wrote {outp}")


if __name__ == '__main__':
    main()
