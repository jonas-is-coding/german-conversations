# 💬 German Conversations

## Overview

This dataset is designed for training AI chat models and focuses on human-like conversations, including various aspects of communication such as body language, emotions, intentions, and subtext. Each entry captures a dialogue between two speakers, providing rich context for machine learning applications in natural language processing. 💬✨

## Dataset Structure

The dataset consists of multiple entries, each containing the following fields:

- **conversation_id**: A unique identifier for the conversation (string). 🆔
- **speaker_a**: A dictionary containing details about the first speaker, including:
  - **body_language**: Description of the speaker’s body language. 🕺
  - **emotion**: List of emotions exhibited by the speaker. 😐😟
  - **intent**: The primary intention behind the speaker’s message. 🎯
  - **role**: The role or identity of the speaker. 👤
  - **subtext**: Additional thoughts that underline the speaker’s intention. 💭
  - **text**: The actual dialogue spoken by the speaker. 🗣️
- **speaker_b**: A similar dictionary containing details about the second speaker with the same fields as speaker_a.

### Example Entry
```json
{
    "conversation": [
        {
            "role": "Fahrkartenkontrolleur",
            "text": "Guten Morgen! Könnten Sie mir bitte Ihr Ticket zeigen?",
            "intent": "Fahrgast kontrollieren",
            "emotion": [
                "neutral",
                "gestresst"
            ],
            "body_language": "hält seinen Stempelblock in der Hand, schaut den Fahrgast an",
            "subtext": "Hoffentlich ist alles in Ordnung und ich muss keinen Streit anfangen."
        },
        {
            "role": "Kundin",
            "text": "Klar, hier bitte. Ich habe aber im Online-Shop vergessen, die Option für die digitale Fahrkarte auszuwählen.",
            "intent": "sich entschuldigen",
            "emotion": [
                "frustriert",
                "sorglich"
            ],
            "body_language": "hält ihr Handy mit der geöffneten Ticket-App bereit, wirkt leicht verlegen",
            "subtext": "Mist, jetzt habe ich bestimmt wieder einen Fehler gemacht. Hoffentlich ist die Kontrolle nicht allzu streng."
        }
    ]
}
```

## Purpose

This dataset can be utilized for:

- Training and fine-tuning conversational AI models. 🛠️
- Developing chatbots capable of understanding complex dialogues. 🤖
- Analyzing human interactions for research in natural language understanding. 📊

## Data Generation

The data in this dataset was generated based on over 100 unique personas and over 300 distinct situations, ensuring a diverse range of conversations that reflect various contexts and dynamics. 🌍📚

## Usage

To use this dataset, you can load it into your preferred machine learning framework (e.g., TensorFlow, PyTorch) and preprocess it for training. Make sure to handle the JSON structure appropriately and extract the relevant fields for your specific application. 📈

## License

This dataset is available for educational and research purposes. Please refer to the license agreement for more details. 📜

## Contribution

Contributions to this dataset are welcome. If you have suggestions or improvements, feel free to reach out! 🤝✨
