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
    "conversation_id": "785b5461-7950-43b0-b9c2-28f2a69842dd",
    "speaker_a": {
        "body_language": "Schaut mit einem fragenden Blick und leicht gehobenen Augenbrauen auf den Fahrkartenkontrolleur",
        "emotion": [
            "neugierig",
            "leicht besorgt"
        ],
        "intent": "Idee zum Projekt teilen und Feedback bekommen",
        "role": "Student",
        "subtext": "Ich hoffe, ich bin nicht zu doof, um so eine Idee jetzt noch vorzuschlagen. Ich hab aber auch keine Lust, mich dafür zu schämen, wenn es jetzt nicht mehr aktuell ist.",
        "text": "Hey, ich hab letztens mein altes Schulprojekt über nachhaltige Energiegewinnung wiedergefunden. Weißt du, damals hatte ich so viel Zeit, mich da richtig reinzuknien. Jetzt fehlt mir leider die Zeit, aber vielleicht könnte man das ja updaten und für eine neue Vorlesung nutzen? Also, nicht das Projekt selbst, sondern die Idee. Könntest du dir vorstellen, dass man so etwas heute noch präsentieren würde? Oder ist das irgendwie out?"
    },
    "speaker_b": {
        "body_language": "Lächelt freundlich, hält den Blickkontakt, hält einen Stempel in der Hand",
        "emotion": [
            "freundlich",
            "leicht gelangweilt"
        ],
        "intent": "Studenten unterstützen und Interesse an der Idee zeigen",
        "role": "Fahrkartenkontrolleur",
        "subtext": "Ich hab so viele dieser Studenten jeden Tag.  Aber irgendwie faszinieren mich ihre Ideen manchmal. Vielleicht kann ich ja später auch nochmal etwas Neues lernen.",
        "text": "Na klar, Energiegewinnung ist doch immer aktuell! Allerdings muss man vielleicht etwas moderner ran gehen. Was wäre denn deine Idee, um das Projekt aufzupeppen?"
    }
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
