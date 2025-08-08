from murf import Murf
import google.generativeai as genai
from pathlib import Path
import requests
import os
import uuid
import re
from dotenv import load_dotenv

load_dotenv()
murf_api_key = os.getenv("MURF_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)
gemini_model = genai.GenerativeModel("gemini-2.0-flash")

def clean_text_for_tts(text: str) -> str:
    text = re.sub(r'[*_#`>-]+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def transliterate_to_english_letters(text):
    prompt = f"""
Convert the following text into English letters (Roman script).  
Do not translate — only convert phonetically.

Text: {text}
"""
    try:
        response = gemini_model.generate_content(prompt)
        return response.text.strip()
    except Exception:
        return text

def text_to_audio_autoplay(text: str, lang: str = "en", return_path=False):
    try:
        audio_dir = Path("static/audio")
        audio_dir.mkdir(parents=True, exist_ok=True)

        for f in audio_dir.glob("*.mp3"):
            try:
                f.unlink()
            except:
                pass

        cleaned_text = clean_text_for_tts(text)

        if lang.lower() != "en":
            cleaned_text = transliterate_to_english_letters(cleaned_text)

        voice_map = {
            "en": "en-IN-aarav",
            "hi": "hi-IN-kabir",
            "te": "en-IN-aarav",  # closest available
            "bn": "bn-IN-anwesha",
            "fr": "fr-FR-adélie"
        }
        voice_id = voice_map.get(lang.lower(), "en-IN-aarav")

        murf_client = Murf(api_key=murf_api_key)
        res = murf_client.text_to_speech.generate(text=cleaned_text, voice_id=voice_id)
        audio_url = res.audio_file

        if not audio_url:
            return "[Murf Error] No audio file returned."

        filename = f"{uuid.uuid4()}.mp3"
        filepath = audio_dir / filename

        audio_data = requests.get(audio_url).content
        with open(filepath, "wb") as f:
            f.write(audio_data)

        audio_url_tag = f"/static/audio/{filename}"
        if return_path:
            return str(filepath), filename

        return f"""
        <audio autoplay controls>
          <source src="{audio_url_tag}" type="audio/mp3">
          Your browser does not support the audio element.
        </audio>
        """
    except Exception as e:
        return f"[Murf TTS Error] {str(e)}"
