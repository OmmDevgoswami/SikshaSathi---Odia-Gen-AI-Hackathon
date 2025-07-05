#Educhain
user_logs = []

def log_doubt(query, answer, videos):
    user_logs.append({
        "question": query,
        "answer": answer,
        "videos": videos
    })

def get_all_logs():
    return user_logs
#gemini_llm
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-1.5-pro")
def get_ai_response(query):
    try:
        response = model.generate_content(f"Answer this student's doubt: {query}")
        return response.text
    except Exception as e:
        return f"Error: {e}"
#Youtube_search
def get_youtube_links(query, max_results=2):
    prompt = (
        f"Suggest {max_results} highly relevant YouTube video links for the following "
        f"NEET/JEE/UPSC/Class XII doubt:\n\n{query}\n\n"
        f"Only return direct YouTube URLs, each on a new line."
    )
    response = get_ai_response(prompt)
    links = [line.strip() for line in response.split("\n") if "youtube.com/watch" in line]
    return links[:max_results]
#main.py
import streamlit as st
from googletrans import Translator
import speech_recognition as sr
from pydub import AudioSegment

st.set_page_config(page_title="SikshaSathi", page_icon="📘", layout="wide")


with st.sidebar:
   # st.image("assets/banner.png", use_container_width=True)  # ✅ FIXED
    st.title("📘 SikshaSathi")
    st.markdown("*Welcome to SikshaSathi - ଶିକ୍ଷାସାଥୀ!*")
    st.markdown("Doubt Assistant-ସ‌ହ‌ଯୋଗୀ ଶିକ୍ଷା")
    st.markdown("---")
    # st.markdown("🧭 Pages:")
    # st.markdown("- Main (You’re here!)")
    # st.markdown("- Roadmap Generator")
    # st.markdown("- Doubt Solver")
    # st.markdown("- Mock Test")


st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-family: Space Grotesk, sans-serif;'>SikshaSathi - ଶିକ୍ଷାସାଥୀ</h1>
         <h2 style='font-family: Space Grotesk, sans-serif;'>Doubt Assistant-ସ‌ହ‌ଯୋଗୀ ଶିକ୍ଷା</h2>
          <h3 style='font-family: Space Grotesk, sans-serif;'>"Confused? Let SikshaSathi clear the air - one doubt at a time!"</h3>
       
    </div>
    """,
    unsafe_allow_html=True
)


st.subheader("📚 Ask Your Doubt")

exam_type = st.selectbox("Choose Exam:", ["NEET", "JEE", "UPSC", "Class XII"])
language = st.selectbox("Preferred Language:", ["English", "Hindi", "Odia"])


st.markdown("### 🎙 Or Upload an Audio Doubt")
uploaded_audio = st.file_uploader("Upload audio (WAV or MP3)", type=["wav", "mp3"])
transcribed_text = ""

if uploaded_audio is not None:
    st.audio(uploaded_audio, format='audio/wav')

   
    if uploaded_audio.type == "audio/mpeg":
        audio = AudioSegment.from_mp3(uploaded_audio)
    else:
        audio = AudioSegment.from_wav(uploaded_audio)

    audio.export("temp.wav", format="wav")
    recognizer = sr.Recognizer()

    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)
        try:
            transcribed_text = recognizer.recognize_google(audio_data)
            st.success(f"✅ Transcribed Text: {transcribed_text}")
        except sr.UnknownValueError:
            st.error("❌ Could not understand audio.")
        except sr.RequestError as e:
            st.error(f"❌ API error: {e}")


query = st.text_area("✍ Enter your doubt below:", value=transcribed_text)

if st.button("🧠 Clear My Doubt"):
    if not query.strip():
        st.warning("⚠ Please enter a valid doubt.")
    else:
        full_query = f"{exam_type} Doubt: {query}"
        answer = get_ai_response(full_query)
        videos = get_youtube_links(query)
        log_doubt(full_query, answer, videos)

        st.markdown("### ✅ AI Answer:")
        st.write(answer)

        if language != "English":
            try:
                translator = Translator()
                lang_code = {"Hindi": "hi", "Odia": "or"}[language]
                translated = translator.translate(answer, dest=lang_code).text
                st.markdown(f"### 🌐 Translated Answer ({language}):")
                st.write(translated)
            except Exception:
                st.warning("⚠ Translation unavailable right now.")

        st.markdown("### 📺 Recommended Videos:")
        for link in videos:
            st.markdown(f"[Watch here]({link})")

        st.success("✅ Doubt saved with EduChain!")