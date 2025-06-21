import webvtt
import os


def vtt_to_text(vtt_path, output_dir):
    """Convert VTT file to plain text and save it."""
    if not os.path.exists(vtt_path):
        raise FileNotFoundError(f"Transcript file not found: {vtt_path}")

    text = ""
    for caption in webvtt.read(vtt_path):
        text += caption.text + " "

    text = text.strip()
    text_path = os.path.join(output_dir, "transcript.txt")
    with open(text_path, 'w', encoding='utf-8') as f:
        f.write(text)

    return text