import locale
locale.getpreferredencoding = lambda: "UTF-8"

import openai
import ast
from IPython.display import HTML
import re
import json

#openai.api_key = "OPENAI_API_KEY"  # Replace with my actual API key

def clean_json_response(response_text):
    # Remove triple backticks and "json" if present
    cleaned_text = re.sub(r"```(json)?", "", response_text).strip()
    return json.loads(cleaned_text)  # Convert JSON string to Python dictionary

def extract_entities_openai(text):
    """Extracts scientific entities using OpenAI's API without Promptify."""

    prompt = f"""
    Extract scientific entities from the following text related to solid-state materials science.
    Categorize them into:
    - Inorganic materials
    - Symmetry/phase labels
    - Sample descriptors
    - Material properties
    - Material applications
    - Synthesis methods
    - Characterization methods

    Only include relevant words or short phrases that exactly match the text.

    Text: \"{text}\"

    Respond with a JSON format:
    {{
        "inorganic materials": [],
        "symmetry/phase labels": [],
        "sample descriptors": [],
        "material properties": [],
        "material applications": [],
        "synthesis methods": [],
        "characterization methods": []
    }}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "You are a scientific NLP expert."},
                  {"role": "user", "content": prompt}],
        temperature=0
    )
    response_text = response["choices"][0]["message"]["content"]

    entities = clean_json_response(response_text)
    return entities

def highlight_text(text, entities):
    """Highlights extracted entities in the text with different colors."""

    colors = {
        "inorganic materials": "yellow",
        "characterization methods": "cyan",
        "symmetry/phase labels": "#0a888a",
        "sample descriptors": "magenta",
        "synthesis methods": "lightgreen",
        "material applications": "grey",
        "material properties": "#FFCC00"
    }

    for category, words in entities.items():
        color = colors[category]
        for word in words:
            text = text.replace(word, f"<span style='background-color: {color}'>{word}</span>")

    return HTML(f"<p>{text}</p>")


def exsclaim_ner(text):
    """
    Extracts scientific entities from the text and highlights them with different colors.

    Categories:
    - Inorganic materials
    - Symmetry/phase labels
    - Sample descriptors
    - Material properties
    - Material applications
    - Synthesis methods
    - Characterization methods

    Returns an HTML-highlighted version of the text with extracted entities.
    """

    # OpenAI Prompt
    prompt = f"""
    Extract scientific entities from the following text related to solid-state materials science.
    Categorize them into:
    - Inorganic materials
    - Symmetry/phase labels
    - Sample descriptors
    - Material properties
    - Material applications
    - Synthesis methods
    - Characterization methods

    Only include relevant words or short phrases that exactly match the text.

    Text: \"{text}\"

    Respond with a JSON format:
    {{
        "inorganic materials": [],
        "symmetry/phase labels": [],
        "sample descriptors": [],
        "material properties": [],
        "material applications": [],
        "synthesis methods": [],
        "characterization methods": []
    }}
    """

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "You are a scientific NLP expert."},
                  {"role": "user", "content": prompt}],
        temperature=0
    )

    # Process Response
    response_text = response["choices"][0]["message"]["content"]
    cleaned_text = re.sub(r"```(json)?", "", response_text).strip()
    entities = json.loads(cleaned_text)  # Convert JSON string to Python dictionary

    # Define Highlight Colors
    colors = {
        "inorganic materials": "yellow",
        "characterization methods": "cyan",
        "symmetry/phase labels": "#0a888a",
        "sample descriptors": "magenta",
        "synthesis methods": "lightgreen",
        "material applications": "grey",
        "material properties": "#FFCC00"
    }

    # Highlight Extracted Entities
    for category, words in entities.items():
        color = colors[category]
        for word in words:
            text = text.replace(word, f"<span style='background-color: {color}'>{word}</span>")

    return HTML(f"<p>{text}</p>"), entities  # Returns highlighted HTML and extracted entities

# Example Usage
text = "Graphene is widely used as an electrocatalyst in fuel cells due to its high conductivity and stability."
highlighted_text, extract_entities_openai = exsclaim_ner(text)

print("Extracted Entities:")
print(extract_entities_openai)
print(highlighted_text)  # Display in Jupyter Notebook

import pandas as pd

# # Read JSON file
file_path = "/home/j/jayaverma/exsclaim/output/nature_polymer_protein_complex/exsclaim_protien_csv.csv"
df = pd.read_csv(file_path)

df['new_labels_generated_using_ner'] = df['full_caption'].apply(exsclaim_ner)
print("execution of the file update is completed with a new added column named as new_labels_generated_using_ner")

# Save DataFrame as CSV with the update of new added column named as new_labels_generated_using_ner in the existing df
df.to_csv(file_path, index=False)
print(f"CSV file saved at: {file_path}")