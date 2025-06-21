# YouTube Transcript Summarizer

A Streamlit application that downloads YouTube video transcripts, converts them to plain text, and generates concise, exam-ready summaries using the OpenRouter API.

## Features
- Downloads YouTube transcripts in VTT format using `yt-dlp`.
- Converts VTT to plain text and saves it.
- Summarizes transcripts into structured markdown summaries.
- Stores outputs (VTT, TXT, summary) in a video-specific folder.
- Displays a progress bar with stages: Start, Download, Process, Finish.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/transcript_summarizer.git
   cd transcript_summarizer
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Enter a YouTube video URL.
2. Select a model (e.g., `deepseek/deepseek-v3-base:free`).
3. Click "Summarize" to generate a markdown summary.
4. Outputs are saved in `transcripts/<video_id>/`.

## Requirements
See `requirements.txt` for dependencies.

## Note
- Requires an OpenRouter API key (hardcoded in `summarizer.py`).
- Ensure the YouTube video has available transcripts.
