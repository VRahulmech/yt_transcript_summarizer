import streamlit as st
from downloader import download_transcript
from processor import vtt_to_text
from summarizer import summarize_long_transcript
from utils import create_video_folder, get_video_id

st.title("YouTube Transcript Summarizer")
st.markdown("Enter a YouTube video URL to generate a concise, exam-ready summary of its transcript.")

# Input fields
url = st.text_input("YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")
model = st.selectbox("Select Model", [
    "deepseek/deepseek-v3-base:free",
    "meta-llama/llama-3.3-8b-instruct:free"
])

# Summarize button
if st.button("Summarize"):
    if not url:
        st.error("Please enter a valid YouTube URL.")
    else:
        try:
            # Initialize progress bar and stage label
            stage_label = st.empty()
            stage_label.text("Stage: Start")
            progress_bar = st.progress(0.0, text="Progress: Start (0%)")

            # Create video folder
            video_id = get_video_id(url)
            output_dir = create_video_folder(video_id)
            progress = 0.0

            # Stage 1: Download
            vtt_path = download_transcript(url, output_dir)
            progress = 0.33
            stage_label.text("Stage: Download")
            progress_bar.progress(progress, text="Progress: Download (33%)")

            if vtt_path:
                # Stage 2: Process
                text = vtt_to_text(vtt_path, output_dir)
                progress = 0.66
                stage_label.text("Stage: Process")
                progress_bar.progress(progress, text="Progress: Process (66%)")

                if text:
                    # Stage 3: Summarize (leads to Finish)
                    summary = summarize_long_transcript(text, model, output_dir)
                    progress = 1.0
                    stage_label.text("Stage: Finish")
                    progress_bar.progress(progress, text="Progress: Finish (100%)")

                    if summary:
                        st.markdown("### Summary")
                        st.markdown(summary)
        except Exception as e:
            st.error(f"Error: {e}")
            progress_bar.empty()
            stage_label.empty()