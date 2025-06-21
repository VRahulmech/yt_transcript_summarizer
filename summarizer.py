import requests
import json
import os
import streamlit as st
from utils import chunk_text


def summarize_with_openrouter(text, model="meta-llama/llama-3.3-8b-instruct:free"):
    """Summarize text using OpenRouter API."""
    api_key = st.secrets.get("OPENROUTER_API_KEY", os.getenv("OPENROUTER_API_KEY"))
    if not api_key:
        raise ValueError("OpenRouter API key not found. Set it in Streamlit secrets or environment variables.")

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are an expert assistant that summarizes long lecture transcripts into very short, exam-ready summaries. Be as concise as possible while preserving key insights."
            },
            {
                "role": "user",
                "content": f"Summarize the following lecture transcript in a very short and structured format:\n\n{text}\n\n"
                           "Instructions:\n"
                           "- Organize the summary using clear section headers (e.g., 'Introduction', 'Key Concepts', 'Formulas', 'Conclusion')\n"
                           "- Under each section, list 2–4 concise bullet points\n"
                           "- Use plain language suitable for quick review\n"
                           "- Include definitions and formulas only if critical to understanding\n"
                           "- Do not include examples unless absolutely necessary\n"
                           "- Avoid repetition and focus only on the essential ideas\n\n"
                           "Format the output in markdown style for readability. Keep the entire summary short and to the point — ideal for last-minute revision."
            }
        ],
        "temperature": 0.3,
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    try:
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        raise ValueError(f"JSON decode failed: {e}")


def summarize_long_transcript(full_text, model, output_dir):
    """Summarize a long transcript by chunking and combining summaries."""
    chunks = chunk_text(full_text)
    all_summaries = []

    for i, chunk in enumerate(chunks):
        summary = summarize_with_openrouter(chunk, model=model)
        all_summaries.append(summary)

    final_summary = summarize_with_openrouter("\n\n".join(all_summaries), model=model)

    summary_path = os.path.join(output_dir, "summary.txt")
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(final_summary)

    return final_summary