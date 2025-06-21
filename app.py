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
        with st.spinner("Processing transcript..."):
            try:
                video_id = get_video_id(url)
                output_dir = create_video_folder(video_id)
                vtt_path = download_transcript(url, output_dir)
                if vtt_path:
                    text = vtt_to_text(vtt_path, output_dir)
                    if text:
                        summary = summarize_long_transcript(text, model, output_dir)
                        if summary:
                            st.markdown("### Summary")
                            st.markdown(summary)
            except Exception as e:
                st.error(f"Error: {e}")
