# Gemini & Murf AI Video Summarizer

An advanced web application built with Python and Streamlit that uses Google's Gemini Pro model to analyze video content and Murf AI for high-quality text-to-speech synthesis. Users can upload a video, ask questions, and receive comprehensive summaries that can be translated and spoken aloud in multiple languages.


***

## ## Live Application

**You can access a live deployed demo here:**
[**➡️ Live Video Summarizer App**](https://ai-video-summarizer-murf.onrender.com) ***

## ## Features

* **AI-Powered Video Analysis**: Upload a video file and ask complex questions to get detailed insights powered by Gemini.
* **Comprehensive Summaries**: Generates detailed, essay-style summaries with titles, subjects, and key topics explained.
* **Multi-Language Translation**: Translates the generated summary into various languages, including Telugu, Hindi, Bengali, and French.
* **High-Quality Text-to-Speech**: Uses Murf AI to generate realistic and natural-sounding voiceovers for both original and translated summaries.
* **Interactive User Interface**: A clean and modern UI built with Streamlit for easy file uploads and interaction.

***

## ## Tech Stack & Services

* **Core Language**: Python
* **Web Framework**: Streamlit
* **AI Models**: Google Gemini Pro
* **Text-to-Speech**: Murf AI
* **Key Libraries**:
    * `google-generativeai`
    * `murf-ai`
    * `streamlit`
    * `python-dotenv`
    * `phi-agent`

***

## ## Getting Started

To run this project on your local machine, follow these steps.

### ### Prerequisites

Make sure you have Python 3.8+ and pip installed on your system.

### ### Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/chaitanyananepallicn/AI-Video-Summarizer-Murf.git
    cd gemini-murf-video-summarizer
    ```

2.  **Create and Activate a Virtual Environment**
    * **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Create a `requirements.txt` file**
    * Create a file named `requirements.txt` and add the following lines:
        ```
        streamlit
        google-generativeai
        python-dotenv
        murf-ai
        phi-agent
        requests
        ```

4.  **Install the Required Libraries**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set Up Environment Variables**
    * This project requires two API keys.
    * Get your Google API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
    * Get your Murf API key from your [Murf AI account dashboard](https://murf.ai/).
    * Create a file named `.env` in the root project directory.
    * Add your API keys to the `.env` file:
        ```
        GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
        MURF_API_KEY="YOUR_MURF_API_KEY_HERE"
        ```

6.  **Run the Streamlit Application**
    ```bash
    streamlit run vta2.py
    ```
    * After running the command, open your web browser and navigate to the local URL provided (usually `http://localhost:8501`).

***

## ## Project Structure
