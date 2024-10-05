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
            "body_language": "Legt den Kopf leicht schräg und beobachtet die Reaktion des Gegenübers",
            "emotion": [
                "neugierig",
                "leicht besorgt"
            ],
            "intent": "Informationen über das Festival einholen",
            "role": "Polizist",
            "subtext": "Ich bin gespannt, wie der junge Mann auf die Frage reagiert und ob er ähnliche Erfahrungen mit dem Festival gemacht hat. Ob es tatsächlich so wild war, wie mein Kollege berichtet hat, bezweifle ich.",
            "text": "Ich hab' gehört, dass am Wochenende ein Festival in der Stadt war. Ich war selbst nicht da, aber ein Kollege erzählte mir, dass es ganz schön wild zuging. Hattest du auch was mitbekommen?"
        },
        {
            "body_language": "Lebhafte Gestik, strahlende Augen, schnelle Bewegungen",
            "emotion": [
                "euphorisch",
                "begeistert",
                "leicht ängstlich"
            ],
            "intent": "Seine Begeisterung für das Festival teilen",
            "role": "Zirkusartist",
            "subtext": "Das war so eine coole Erfahrung, ich hatte so viel Spaß! Jetzt hab ich noch mehr Lust, meine eigene Zirkus-Produktion zu starten. Vielleicht sogar auf einem Festival wie dem! Das wäre echt der Wahnsinn!  Aber ich muss auch auf meine Gesundheit achten, ich will mir ja nicht nochmal den Arm brechen.",
            "text": "Ach, du meinst das Summer Blast? Ja klar, da war ich! Es war echt der Hammer, die Stimmung war so euphorisch, die Musik hat durchgedröhnt und die Leute haben getanzt wie verrückt! Das Energielevel war unglaublich!  Ich musste natürlich auch mal kurz auf die Bühne, hab ein paar Jonglage-Tricks gezeigt. Die Leute waren begeistert! Die Musik war so inspirierend, ich hatte richtig Bock, noch mehr zu zeigen! Aber ich musste ja auch aufpassen, dass ich nicht zu sehr aus dem Häuschen gerate und mir nichts breche.  Hab aber trotzdem ein paar coole Fotos für Social Media gemacht, die Leute müssen ja wissen, dass wir da waren!"
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
