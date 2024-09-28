import json
import os
import uuid
from datasets import Dataset, DatasetDict
import numpy as np

# Funktion zum Laden der Daten aus JSON-Dateien
def load_data(conversation_files):
    conversations_dataset_train = []
    conversations_dataset_test = []
    conversations_dataset_val = []

    # Berechne die Längen für Train, Val und Test
    val_length = int(len(conversation_files) * 0.1)
    test_length = int(len(conversation_files) * 0.1)

    # Shuffle der Dateien, um die Auswahl zufällig zu gestalten
    np.random.shuffle(conversation_files)

    # Iteriere über die conversation_files und teile sie in die entsprechenden Datasets auf
    for idx, conversation_file in enumerate(conversation_files):
        with open(conversation_file, 'r') as f:
            conversation = json.load(f)

        speakers = conversation["conversation"]
        
        if len(speakers) < 2:
            continue

        speaker_a = speakers[0]
        speaker_b = speakers[1]

        # Weisen Sie die ersten 10% der Dateien dem Validierungs-Dataset zu
        if len(conversations_dataset_val) < val_length:
            conversations_dataset_val.append({
                "conversation_id": str(uuid.uuid4()),
                "speaker_a": speaker_a,
                "speaker_b": speaker_b,
            })
        # Die nächsten 10% gehen in das Test-Dataset
        elif len(conversations_dataset_test) < test_length:
            conversations_dataset_test.append({
                "conversation_id": str(uuid.uuid4()),
                "speaker_a": speaker_a,
                "speaker_b": speaker_b,
            })
        # Der Rest geht ins Trainings-Dataset
        else:
            conversations_dataset_train.append({
                "conversation_id": str(uuid.uuid4()),
                "speaker_a": speaker_a,
                "speaker_b": speaker_b,
            })

    return conversations_dataset_train, conversations_dataset_val, conversations_dataset_test

# Pfade zu deinen JSON-Dateien
conversation_dir = "./conversations"
conversation_files = [os.path.join(conversation_dir, file) for file in os.listdir(conversation_dir) if file.endswith('.json')]

(conversations_dataset_train, conversations_dataset_val, conversations_dataset_test) = load_data(conversation_files)

# Erstelle die Datasets
conversations_dataset_train = Dataset.from_dict({
    'conversation_id': [entry["conversation_id"] for entry in conversations_dataset_train],
    'speaker_a': [entry["speaker_a"] for entry in conversations_dataset_train],
    'speaker_b': [entry["speaker_b"] for entry in conversations_dataset_train],
})

# Kombiniere die Datasets in einem DatasetDict
hf_dataset = DatasetDict({
    "train": conversations_dataset_train,
    "val": Dataset.from_dict({
        'conversation_id': [entry["conversation_id"] for entry in conversations_dataset_val],
        'speaker_a': [entry["speaker_a"] for entry in conversations_dataset_val],
        'speaker_b': [entry["speaker_b"] for entry in conversations_dataset_val],
    }),
    "test": Dataset.from_dict({
        'conversation_id': [entry["conversation_id"] for entry in conversations_dataset_test],
        'speaker_a': [entry["speaker_a"] for entry in conversations_dataset_test],
        'speaker_b': [entry["speaker_b"] for entry in conversations_dataset_test],
    })
})

# Versuche, das Dataset auf Hugging Face hochzuladen
try:
    hf_dataset.push_to_hub("jonas-is-coding/mira")
    print("Dataset erfolgreich gepusht.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

# Ausgabe der ersten Einträge zur Überprüfung
print(hf_dataset["train"][:5])
print(hf_dataset["val"][:5])
print(hf_dataset["test"][:5])
