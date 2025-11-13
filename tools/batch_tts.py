import os
import sys
import pyttsx3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
READING_DIR = os.path.join(BASE_DIR, 'reading')

FILES = [f'reading_long_{i:02d}.md' for i in range(1, 11)]


def extract_passage(md_text: str) -> str:
    lines = md_text.splitlines()
    out_lines = []
    for line in lines:
        if line.strip().startswith('設問'):
            break
        out_lines.append(line)
    return '\n'.join(out_lines).strip()


def generate_wav(md_path: str, out_wav: str, engine: pyttsx3.Engine):
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()
    passage = extract_passage(md)
    if not passage:
        print('No passage extracted from', md_path)
        return False
    engine.save_to_file(passage, out_wav)
    engine.runAndWait()
    print('Saved', out_wav)
    return True


if __name__ == '__main__':
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    ja_voice = None
    for v in voices:
        if 'japan' in v.name.lower() or 'japanese' in v.name.lower() or 'nihon' in v.name.lower() or 'ja_' in v.id.lower():
            ja_voice = v.id
            break
    if ja_voice:
        engine.setProperty('voice', ja_voice)
        print('Using voice:', ja_voice)
    else:
        print('No explicit Japanese voice found; using default voice.')

    success = []
    for fn in FILES:
        md_path = os.path.join(READING_DIR, fn)
        out_wav = os.path.join(READING_DIR, fn.replace('.md', '.wav'))
        if not os.path.exists(md_path):
            print('Missing file:', md_path)
            success.append(False)
            continue
        res = generate_wav(md_path, out_wav, engine)
        success.append(res)

    ok = all(success)
    if ok:
        print('All files generated successfully')
    else:
        print('Some files failed. See messages above.')
    sys.exit(0 if ok else 1)
