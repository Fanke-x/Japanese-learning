#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import random
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_vocab(csv_path: Path):
    items = []
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            label = r.get('reading_type', '')
            label_str = f" [{label}]" if label else ''
            items.append({
                "q": f"{r['kanji']} ({r['pos']}){label_str}",
                "a": f"{r['reading']} — {r['meaning_zh']}",
                "extra": r.get('id', '')
            })
    return items


def load_grammar(csv_path: Path):
    items = []
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            items.append({
                "q": r['pattern'],
                "a": f"{r['meaning_zh']} | {r['notes']}",
                "extra": r.get('id', '')
            })
    return items


def ask(items, n):
    sample = random.sample(items, k=min(n, len(items)))
    correct = 0
    for i, it in enumerate(sample, 1):
        print(f"[{i}/{len(sample)}] {it['q']}")
        input("Enter to show answer…")
        print(f"→ {it['a']}\n")
        yn = input("Did you know it? (y/N): ").strip().lower()
        if yn == 'y':
            correct += 1
        print()
    return correct, len(sample)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--vocab', type=str, default=str(ROOT / 'vocab' / 'core_words_001-150.csv'))
    ap.add_argument('--grammar', type=str, default=str(ROOT / 'grammar' / 'grammar_100.csv'))
    ap.add_argument('--n-vocab', type=int, default=10)
    ap.add_argument('--n-grammar', type=int, default=5)
    args = ap.parse_args()

    print("Vocab drill")
    v_items = load_vocab(Path(args.vocab))
    v_ok, v_total = ask(v_items, args.n_vocab)

    print("Grammar drill")
    g_items = load_grammar(Path(args.grammar))
    g_ok, g_total = ask(g_items, args.n_grammar)

    print("Summary")
    print(f"Vocab: {v_ok}/{v_total} known")
    print(f"Grammar: {g_ok}/{g_total} known")


if __name__ == '__main__':
    main()
