import textwrap
import os
import re

def chunk_text(text, max_chunk_len=8000):
    """Split text into chunks of specified length."""
    return textwrap.wrap(text, width=max_chunk_len, break_long_words=False, replace_whitespace=False)

def get_video_id(url):
    """Extract video ID from YouTube URL."""
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    raise ValueError("Invalid YouTube URL")

def create_video_folder(video_id):
    """Create a folder for video outputs."""
    output_dir = os.path.join("transcripts", video_id)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir