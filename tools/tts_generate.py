import io
import os
import sys
import pyttsx3

# Config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH = os.path.join(BASE_DIR, 'reading', 'reading_long_03.md')
OUT_WAV = os.path.join(BASE_DIR, 'reading', 'reading_long_03.wav')


def extract_passage(md_text: str) -> str:
    # Return text from start until the first line that begins with '設問' or '設問（' or '設問\n'
    lines = md_text.splitlines()
    out_lines = []
    for line in lines:
        if line.strip().startswith('設問'):
            break
        out_lines.append(line)
    # Remove markdown title lines and empty lines at start
    # Keep Japanese text as-is
    return '\n'.join(out_lines).strip()


if __name__ == '__main__':
    if not os.path.exists(MD_PATH):
        print('Markdown file not found:', MD_PATH)
        sys.exit(1)

    with open(MD_PATH, 'r', encoding='utf-8') as f:
        md = f.read()

    passage = extract_passage(md)
    if not passage:
        print('No passage extracted (check the format)')
        sys.exit(1)

    # Initialize TTS engine
    engine = pyttsx3.init()

    # List voices to find a Japanese-capable voice
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
        print('No explicit Japanese voice found; using default voice. If the TTS pronunciation is poor, install a Japanese SAPI voice.')

    # Save to file
    engine.save_to_file(passage, OUT_WAV)
    engine.runAndWait()
    print('Saved WAV to', OUT_WAV)
