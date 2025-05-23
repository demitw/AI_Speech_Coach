import streamlit as st
from analysis.transcription import transcribe_audio
from analysis.audio_features import get_pacing
from analysis.filler_words import count_filler_words
from analysis.sentiment_analysis import get_sentiment
from analysis.coaching_tips import generate_tips
from dotenv import load_dotenv
import os
import re

load_dotenv()

# --- Header Section ---
st.set_page_config(page_title="AI Coach for Public Speaking", page_icon="🗣️")

st.markdown("<h1 style='color:#2c3e50;'>🎙️ AI Coach for Public Speaking</h1>", unsafe_allow_html=True)
st.markdown("##### 👋 Upload a speech to get real-time AI feedback on your delivery, clarity, and tone.")

st.markdown("---")

# --- File Upload Section ---
uploaded_file = st.file_uploader("📤 Upload your speech (MP3 or WAV)", type=["mp3", "wav"])

if uploaded_file:
    file_path = os.path.join("audio", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.audio(file_path)

    st.markdown("---")

    # --- Analysis ---
    with st.spinner("🔍 Analyzing your speech..."):
        transcript = transcribe_audio(file_path)
        pacing = get_pacing(file_path)
        filler_count = count_filler_words(transcript)
        sentiment, confidence = get_sentiment(transcript)

    # --- Transcript Display ---
    st.markdown("### 📝 Transcript")
    st.markdown(f"<div style='background-color:#f8f9fa; padding: 12px; border-radius: 8px;'>{transcript}</div>", unsafe_allow_html=True)

    st.markdown("---")

    # --- Metrics Section ---
    st.markdown("### 📊 Feedback Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Pacing", f"{pacing:.2f}", "🕒")
    col2.metric("Filler Words", f"{filler_count}", "💬")
    col3.metric("Sentiment", sentiment, f"{confidence:.2f}")

    if filler_count > 10:
        st.warning("⚠️ Too many filler words! Try to slow down and think clearly.")
    if sentiment == "NEGATIVE":
        st.warning("😕 Your tone sounds negative or unconfident. Consider using more positive phrasing.")

    st.markdown("---")

    # --- AI Coaching Tips ---
    tips = generate_tips(transcript, sentiment, pacing, filler_count)

    st.markdown("### 💡 AI Coaching Tips")

    if not tips or len(tips.strip()) < 10:
        st.success("✅ Great job! No major issues found. Keep practicing to maintain your strengths.")
    else:
        split_tips = re.split(r"\s*\d+\.\s*", tips.strip())
        split_tips = [tip for tip in split_tips if len(tip.strip()) > 5]
        for tip in split_tips:
            st.markdown(f"<div style='background-color:#eaf4fc; padding:10px; border-left: 4px solid #3498db; margin-bottom: 10px;'>{tip.strip().capitalize()}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("📌 Tip: Record speeches in different tones and compare how your delivery changes over time.")
