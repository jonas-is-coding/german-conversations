import random
import json
import google.generativeai as genai
import os
import time
from personas import personas
from situations import situations

save_path="./conversations/"
current_index = len(os.listdir(save_path))

# Setze deine API-Schlüssel hier ein
GEMINI_API_KEY = "KEY_1"
GEMINI_API_KEY_2 = "KEY_2"

# Setze den initialen API-Schlüssel
api_key = GEMINI_API_KEY

def generate_conversation(prompt):
    global api_key  # Deklariere api_key als global
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        "gemini-1.5-flash",
        generation_config={"response_mime_type": "application/json"}
    )
    
    while True:  # Schleife zum erneuten Versuchen
        try:
            response = model.generate_content(prompt)
            return json.loads(response.text)  # Direktes Laden als JSON
        except Exception as e:
            print(f"Fehler beim Generieren der Konversation: {e}")
            if "429" in str(e):  # Überprüfe, ob der Fehler 429 ist
                print("Quota erschöpft. Versuche anderen API Schlüssel...")
                # Wechsel den API Schlüssel
                if api_key == GEMINI_API_KEY:
                    api_key = GEMINI_API_KEY_2
                else:
                    print("Beide API Schlüssel sind erschöpft. Warte 10 Sekunden und versuche es erneut...")
                    time.sleep(10)  # Wartezeit, bevor du es erneut versuchst
                genai.configure(api_key=api_key)  # Konfiguriere den neuen Schlüssel
                time.sleep(5)  # Wartezeit vor dem erneuten Versuch
            else:
                return None  # Bei anderen Fehlern beende die Schleife

def save_conversation_to_json(conversation, file_name):
    try:
        with open(file_name, 'w') as json_file:
            json.dump(conversation, json_file, indent=4)  # Speicherung des JSON-Objekts
        print(f"Gespeichert: {file_name}")
    except Exception as e:
        print(f"Fehler beim Speichern der Konversation: {e}")

def generate_prompt():
    persona_a = random.choice(personas)
    persona_b = random.choice(personas)
    conversation_context = random.choice(situations)

    prompt = f"""
    Erzeuge eine lebendige und realistische Konversation im JSON-Format zwischen zwei verschiedenen Personas. Die Konversation soll auf Deutsch verfasst sein. Die Interaktion muss stark an ihrer Rolle, ihrem Alter, ihren Emotionen und ihren spezifischen Eigenschaften ausgerichtet sein und realistische Dialogstrukturen verwenden.
    Dennoch soll die Konversation so realistisch und echt wie nur irgendwie möglich klingen. Verwende Umgangssprache und es ist auch nicht nötig, dass die Personen die ganze Zeit über Ihre Rolle reden. Das Ziel ist es, darzustellen wie bestimmte Rollen auf bestimmte Sätze reagieren würden. Ein Umweltschützer würde die Umwelt z.B. nicht erwähnnen wenn man sagt man besucht einen Sprachkurs. Da musst du also realistisch bleiben.

    **Die gesamte Ausgabe, einschließlich der Rollen, muss auf Deutsch sein**.

    Berücksichtige die folgenden detaillierten Eigenschaften der Personas:
    
    Person A:
    - Alter: {persona_a['age']}
    - Rolle: {persona_a['role']}
    - Hintergrund: {persona_a['background']}
    - Spezifische Eigenschaften: {', '.join(persona_a['specific_traits'])}
    - Emotionale Grundhaltung: {', '.join(persona_a['emotion'])}
    - Sprechstil: {persona_a['speech_style']}
    - Persönlichkeitstyp: {persona_a['personality_type']}
    - Kultureller Hintergrund: {persona_a['cultural_background']}
    - Hobbys: {', '.join(persona_a['hobbies'])}
    - Lebenserfahrungen: {', '.join(persona_a['life_experiences'])}
    - Bildung: {persona_a['education']}
    - Sozioökonomischer Status: {persona_a['socioeconomic_status']}
    - Werte: {', '.join(persona_a['values'])}
    - Kommunikationsstärken: {', '.join(persona_a['communication_strengths'])}
    - Kommunikationsschwächen: {', '.join(persona_a['communication_weaknesses'])}
    - Stressbewältigung: {persona_a['stress_coping']}
    - Beziehungsstatus: {persona_a['relationship_status']}
    - Gesundheit: {persona_a['health']}
    - Technologieaffinität: {persona_a['tech_affinity']}
    - Zukunftsziele: {persona_a['future_goals']}
    - Traumata: {persona_a['traumas']}

    Person B: 
    - Alter: {persona_b['age']}
    - Rolle: {persona_b['role']}
    - Hintergrund: {persona_b['background']}
    - Spezifische Eigenschaften: {', '.join(persona_b['specific_traits'])}
    - Emotionale Grundhaltung: {', '.join(persona_b['emotion'])}
    - Sprechstil: {persona_b['speech_style']}
    - Persönlichkeitstyp: {persona_b['personality_type']}
    - Kultureller Hintergrund: {persona_b['cultural_background']}
    - Hobbys: {', '.join(persona_b['hobbies'])}
    - Lebenserfahrungen: {', '.join(persona_b['life_experiences'])}
    - Bildung: {persona_b['education']}
    - Sozioökonomischer Status: {persona_b['socioeconomic_status']}
    - Werte: {', '.join(persona_b['values'])}
    - Kommunikationsstärken: {', '.join(persona_b['communication_strengths'])}
    - Kommunikationsschwächen: {', '.join(persona_b['communication_weaknesses'])}
    - Stressbewältigung: {persona_b['stress_coping']}
    - Beziehungsstatus: {persona_b['relationship_status']}
    - Gesundheit: {persona_b['health']}
    - Technologieaffinität: {persona_b['tech_affinity']}
    - Zukunftsziele: {persona_b['future_goals']}
    - Traumata: {persona_b['traumas']}

    Verwende diesen Kontext für die Konversation:
    Kontext: {conversation_context}

    WICHTIG:
    - **Alles muss auf Deutsch sein.**
    - **Verwende das Beispiel NICHT als Basis für die Konversation**, sondern nutze es nur als Inspiration. 
    - Jedes Statement muss die politischen, sozialen und emotionalen Ansichten der Persona vollständig widerspiegeln. 
    - Die Antwort muss sich durch die spezifischen Eigenschaften der Persona A und Persona B klar unterscheiden und in sich konsistent sein.
    - Jeder Sprecher soll **genau eine Äußerung** tätigen.

    Jede Äußerung sollte folgende Elemente enthalten:
    - **role**: die Rolle der Person A bzw. Person B (auf Deutsch),
    - **text**: den gesprochenen Text, der zur Rolle, dem Alter und den spezifischen Eigenschaften der Persona passt,
    - **intent**: die Absicht hinter der Äußerung,
    - **emotion**: die Emotion(en), die der Sprecher in diesem Moment empfindet, basierend auf ihrer emotionalen Grundhaltung und den Umständen,
    - **body_language**: nonverbale Kommunikation oder Körpersprache, die die Emotion unterstreicht,
    - **subtext**: implizierte oder unausgesprochene Gedanken oder Gefühle in der Ich-Perspektive.

    Achte darauf, dass:
    1. Die Wortwahl und der Ton der Konversation altersgerecht, rollenspezifisch und kontextsensitiv sind.
    2. Kulturelle Nuancen, Bildungshintergrund und sozioökonomischer Status in der Sprache und den Ansichten reflektiert werden.
    3. Die spezifischen Eigenschaften, Lebenserfahrungen und Werte der Personas in ihren Äußerungen zum Vorschein kommen.
    4. Die Kommunikationsstärken und -schwächen der Personas berücksichtigt werden.
    5. Der Sprechstil jeder Person konsistent und charakteristisch ist.
    6. Die emotionale Grundhaltung der Personas ihre Reaktionen beeinflusst, aber auch situationsbedingte Emotionen auftreten.
    7. Persönliche Anekdoten oder Geschichten eingebracht werden, die mit den Lebenserfahrungen und dem Hintergrund der Personas übereinstimmen.
    8. Offene Fragen gestellt werden, die die spezifischen Interessen und Expertisen der Gesprächspartner berücksichtigen.
    9. Die Stressbewältigung, Gesundheit und Technologieaffinität der Personas in relevanten Situationen zum Ausdruck kommen.

    Die Antwort sollte folgendes JSON-Schema haben:

    {{
        "conversation": [
            {{
                "role": "...",
                "text": "...",
                "intent": "...",
                "emotion": ["...", "..."],
                "body_language": "...",
                "subtext": "..."
            }},
            {{
                "role": "...",
                "text": "...",
                "intent": "...",
                "emotion": ["...", "..."],
                "body_language": "...",
                "subtext": "..."
            }}
        ]
    }}

    Achte darauf, dass die Konversation authentisch und realistisch klingt und die spezifischen Eigenschaften und Emotionen der Sprecher in verschiedenen Situationen deutlich wiedergibt. Verwende ausschließlich die deutsche Sprache.
    
    Vermeide Escape-Zeichen und schreibe im reinen JSON-Format.
    """
    
    return prompt

def generate_and_save_conversations(num_conversations=10000):
    for i in range(current_index, current_index + num_conversations):
        prompt = generate_prompt()
        conversation = generate_conversation(prompt)
        
        # Wenn die Konversation None ist, überspringe das Speichern
        if conversation is None:
            continue
        
        file_name = os.path.join(save_path, f"conversation_{i + 1}.json")  # Erstelle einen Dateinamen
        save_conversation_to_json(conversation, file_name)

print("Generiere Konversationen...")
generate_and_save_conversations()
print("Konversationen wurden generiert und gespeichert.")
