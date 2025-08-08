import google.generativeai as genai

def translate_text(text: str, target_language: str) -> str:
    if not text.strip():
        return "⚠️ No text to translate."
    try:
        prompt = f"Translate the following into {target_language}:\n\n{text}"
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"[Translation Error] {str(e)}"
