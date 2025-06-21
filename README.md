# YouTube Transcript Summarizer
A Streamlit application that downloads YouTube video transcripts, converts them to plain text, and generates concise, exam-ready summaries using the OpenRouter API.
Features

- Downloads YouTube transcripts in VTT format using yt-dlp.
- Converts VTT to plain text and saves it.
- Summarizes transcripts into structured markdown summaries.
- Stores outputs (VTT, TXT, summary) in a video-specific folder.
- Displays a progress bar with stages: Start, Download, Process, Finish.

## Installation

Clone the repository:git clone https://github.com/your-username/transcript_summarizer.git
cd transcript_summarizer


Create and activate a virtual environment:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install -r requirements.txt


Run the app:streamlit run app.py



## Usage

Enter a YouTube video URL.
Select a model (e.g., deepseek/deepseek-v3-base:free).
Click "Summarize" to generate a markdown summary.
Outputs are saved in transcripts/<video_id>/.

## Requirements
See requirements.txt for dependencies.
Note

Requires an OpenRouter API key (hardcoded in summarizer.py).
Ensure the YouTube video has available transcripts.

