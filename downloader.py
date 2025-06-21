import yt_dlp
import glob
import os

def download_transcript(url, output_dir):
    """Download the transcript (VTT) for a given YouTube URL."""
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': False,
        'allsubtitles': True,
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get('title', 'video')

    vtt_files = glob.glob(os.path.join(output_dir, f"{title}*.vtt"))
    if vtt_files:
        return vtt_files[0]
    else:
        raise FileNotFoundError("No transcript file found.")