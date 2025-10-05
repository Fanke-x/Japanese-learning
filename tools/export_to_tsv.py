#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import argparse
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--type', choices=['vocab', 'grammar'], required=True)
    ap.add_argument('--in', dest='inp', required=True)
    ap.add_argument('--out', dest='outp', required=True)
    # New options for vocab decks
    ap.add_argument('--front', choices=['kanji', 'reading'], default='kanji', help='Front side for vocab cards')
    ap.add_argument('--with-meaning', action='store_true', help='Include CN meaning on the back (vocab)')
    args = ap.parse_args()

    inp = Path(args.inp)
    outp = Path(args.outp)

    with open(inp, encoding='utf-8') as f, open(outp, 'w', encoding='utf-8', newline='') as g:
        reader = csv.DictReader(f)
        if args.type == 'vocab':
            for r in reader:
                kanji = f"{r['kanji']} ({r['pos']})"
                reading = r['reading']
                meaning = r.get('meaning_zh', '')
                if args.front == 'kanji':
                    front = kanji
                    back = reading if not args.with_meaning else f"{reading} — {meaning}"
                else:  # front is reading
                    front = reading
                    back = kanji if not args.with_meaning else f"{kanji} — {meaning}"
                g.write(front + "\t" + back + "\n")
        else:
            # front: pattern | back: meaning_zh | notes
            for r in reader:
                front = r['pattern']
                back = f"{r['meaning_zh']} | {r['notes']}"
                g.write(front + "\t" + back + "\n")

    print(f"Wrote {outp}")


if __name__ == '__main__':
    main()
