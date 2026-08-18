# 🎵 Ohang AI

> AI-powered music generation application built with Stable Audio 3 and Gradio.

Ohang AI is an experimental AI music generation project that allows users to create original music by selecting a genre, mood, language/style, and custom keywords.

The application transforms user selections into an optimized music-generation prompt and uses an AI model to generate stereo audio.

## ✨ Features

- 🎵 AI Music Generation
- 🎼 Genre Selection
- 😊 Mood Selection
- 🌍 Language / Style Selection
- 📝 Custom Keywords
- ⏱️ Adjustable Music Duration
- 🎧 Built-in Audio Player
- 💾 WAV Audio Output
- 🖥️ Interactive Gradio Interface

## 🧠 How It Works

```text
User Input
    │
    ├── Language / Style
    ├── Genre
    ├── Mood
    ├── Keywords
    └── Duration
           │
           ▼
    Prompt Engineering
           │
           ▼
    Stable Audio 3
           │
           ▼
    AI Music Generation
           │
           ▼
      Stereo WAV Audio


🎛️ Example
User Input
Style: Uzbek-inspired
Genre: Pop
Mood: Romantic
Keywords:
traditional dutar melody, gentle doira percussion,
warm piano, romantic melody, cinematic atmosphere
Generated Prompt
Romantic Uzbek-inspired pop music with traditional dutar melody,
gentle doira percussion, warm piano and a cinematic atmosphere.
Professional music production with clean stereo sound.
🛠️ Tech Stack
Python
PyTorch
Stable Audio 3 Small-Music
Gradio
Hugging Face
Torchaudio
Google Colab
🚀 Running the Project
<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/131b3d2c-17e1-4374-81a0-a8da089ae5ac" />


This project is designed to run with GPU acceleration.

1. Clone the repository
git clone https://github.com/YOUR_USERNAME/ohang-ai.git
cd ohang-ai
2. Install dependencies
pip install -r requirements.txt
3. Hugging Face Authentication

The Stable Audio 3 Small-Music model requires access permission and authentication.

Request access to the model and create a Hugging Face access token.

Then login:

from huggingface_hub import login


login()
4. Run the application
python app.py
📁 Project Structure
ohang-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── assets/
    └── demo.png


🔮 Future Improvements
Uzbek music presets
Advanced prompt enhancement
Music generation history
Download management
Uzbek lyrics generation
AI singing voice integration
Uzbek music dataset fine-tuning
Web deployment
⚠️ Note

This is an experimental AI music generation project.

The current version uses a pre-trained Stable Audio 3 Small-Music model. No custom model training or fine-tuning has been performed in the current version.

👨‍💻 Author

Ikromjon Tojiboev

AI / Machine Learning Engineer

⭐ If you like this project, consider giving it a star!
