# AI_Speech_Coach
🗣️ AI-powered public speaking coach: audio analysis, feedback &amp; tips in real time

An intelligent, interactive Streamlit app that analyzes your speech audio to help you become a more confident and effective speaker. Upload an `.mp3` or `.wav` file of your speech, and receive:

- 📝 Accurate Transcription (via OpenAI Whisper)
- 📊 Quantitative Feedback (pacing, filler words, sentiment)
- 💡 Smart AI Coaching Tips (tailored advice)

---

## ✨ Features

| Feature                  | Description |
|--------------------------|-------------|
| 🔈 **Audio Upload**        | Supports `.mp3` and `.wav` |
| 🔍 **Transcription**       | Uses OpenAI Whisper to convert speech to text |
| ⚙️ **Pacing Analyzer**     | Detects speed/energy of your delivery |
| 🗣️ **Filler Word Counter** | Measures hesitation markers like "um", "uh", "like" |
| 😊 **Sentiment Analysis**  | Detects tone and confidence |
| 💡 **Coaching Tips (AI)**  | AI-generated feedback based on your performance |

---

## 🛠️ Technologies Used

- **Python** 🐍
- **Streamlit** – Web UI framework
- **OpenAI Whisper** – For speech transcription
- **HuggingFace Transformers** – For sentiment analysis
- **PyAudioAnalysis** – For pacing and audio metrics


---

## 📁 Project Structure

```
ai_speech_coach/
│
├── app.py                      # Main Streamlit app
├── requirements.txt            # Dependency list
├── .env.example                # Template for environment variables
│
├── analysis/                   # Modular backend logic
│   ├── transcription.py
│   ├── audio_features.py
│   ├── filler_words.py
│   ├── sentiment_analysis.py
│   └── coaching_tips.py
│
├── audio/                      # Uploaded audio (ignored by git)
└── transcripts/                # (optional) saved transcripts
```

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/demitw/ai-speech-coach.git
cd ai-speech-coach
```

### 2. Create a virtual environment

```bash
python -m venv venv
.env\Scriptsctivate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the app

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser 🎉

---

## 🔐 Note on Privacy

- Uploaded audio is processed locally and never stored or shared.

---

## 📘 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙌 Contributions

Pull requests are welcome! If you have ideas to improve tips, features, or UI, feel free to fork and submit a PR.

---

## 💬 Connect

Created by Demini Waidyanatha.(https://www.linkedin.com/in/demini-waidyanatha-b1b3a9292/) 
Feel free to ⭐ the repo or share your feedback!
