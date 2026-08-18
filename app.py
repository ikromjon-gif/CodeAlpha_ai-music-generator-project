import os
import uuid

import gradio as gr
import torch
import torchaudio
from huggingface_hub import login
from stable_audio_3 import StableAudioModel


# =========================
# CONFIG
# =========================

SAMPLE_RATE = 44100
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


# =========================
# HUGGING FACE AUTH
# =========================

# For local/Colab usage:
# Run `huggingface-cli login`
# or set HF_TOKEN as an environment variable.

HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN:
    login(token=HF_TOKEN)


# =========================
# LOAD MODEL
# =========================

print(f"Using device: {DEVICE}")
print("Loading Stable Audio 3 Small-Music...")

model = StableAudioModel.from_pretrained("small-music")

print("Model loaded successfully!")


# =========================
# MUSIC GENERATION
# =========================

def generate_music(language, genre, mood, keywords, duration):

    if not keywords or len(keywords.strip()) < 3:
        raise gr.Error("Please enter some keywords for your music.")

    # Prompt engineering
    prompt = f"""
    {genre} music,
    {mood} mood,
    {language} musical style,
    {keywords},

    high quality professional music production,
    clean stereo sound,
    professional studio recording,
    detailed instruments,
    balanced composition.
    """

    if language == "Instrumental":
        prompt += """
        Instrumental music only.
        No speech, no talking, no vocals.
        """

    print("\n" + "=" * 50)
    print("GENERATED PROMPT:")
    print(prompt)
    print("=" * 50 + "\n")

    # Generate music
    with torch.inference_mode():
        audio = model.generate(
            prompt=prompt,
            duration=int(duration)
        )

    # Remove batch dimension
    waveform = audio.squeeze(0).cpu()

    # Create output directory
    os.makedirs("outputs", exist_ok=True)

    # Unique filename
    filename = f"outputs/ohang_{uuid.uuid4().hex[:8]}.wav"

    # Save audio
    torchaudio.save(
        filename,
        waveform,
        SAMPLE_RATE
    )

    return filename


# =========================
# GRADIO UI
# =========================

with gr.Blocks(
    title="Ohang AI"
) as demo:

    gr.Markdown("""
    # 🎵 OHANG AI

    ### AI-Powered Music Generator

    Select a style, genre and mood.
    Add keywords and let AI create your music.
    """)

    with gr.Row():

        # LEFT SIDE
        with gr.Column():

            language = gr.Dropdown(
                choices=[
                    "English",
                    "French",
                    "Uzbek-inspired",
                    "Korean",
                    "Instrumental"
                ],
                value="Instrumental",
                label="Language / Style"
            )

            genre = gr.Dropdown(
                choices=[
                    "Pop",
                    "Rap",
                    "Hip Hop",
                    "Electronic",
                    "Rock",
                    "Classical",
                    "Lo-fi",
                    "Traditional",
                    "Jazz",
                    "Cinematic"
                ],
                value="Pop",
                label="Genre"
            )

            mood = gr.Dropdown(
                choices=[
                    "Happy",
                    "Sad",
                    "Romantic",
                    "Emotional",
                    "Energetic",
                    "Relaxing",
                    "Epic",
                    "Dark"
                ],
                value="Romantic",
                label="Mood"
            )

            keywords = gr.Textbox(
                label="Keywords",
                placeholder=(
                    "Example: traditional dutar melody, "
                    "gentle doira percussion, warm piano..."
                ),
                lines=4
            )

            duration = gr.Slider(
                minimum=10,
                maximum=59,
                value=30,
                step=1,
                label="Duration (seconds)"
            )

            generate_btn = gr.Button(
                "✨ Generate Music",
                variant="primary"
            )

        # RIGHT SIDE
        with gr.Column():

            output_audio = gr.Audio(
                label="🎧 Generated Music",
                type="filepath"
            )

            gr.Markdown("""
            ### 💡 Example

            **Style:** Uzbek-inspired  
            **Genre:** Pop  
            **Mood:** Romantic  

            **Keywords:**

            `traditional dutar melody, gentle doira percussion,
            warm piano, emotional melody, cinematic atmosphere,
            slow beginning, powerful ending, 95 BPM`
            """)

    # Button action
    generate_btn.click(
        fn=generate_music,
        inputs=[
            language,
            genre,
            mood,
            keywords,
            duration
        ],
        outputs=output_audio
    )


# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    demo.launch()
