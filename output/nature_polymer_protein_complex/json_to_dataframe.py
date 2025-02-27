from exsclaim.visualize_dataset import *
from itables import init_notebook_mode

init_notebook_mode(all_interactive=True)
df = read_jsons('/home/j/jayaverma/exsclaim/output/nature_polymer_protein_complex/exsclaim.json')

exsclaim_protien_csv = "exsclaim_protien_csv.csv"

print('Json converted and saved to csv')

# Save DataFrame to CSV
df.to_csv(exsclaim_protien_csv, index=False)

# Sample JSON
test_json = {
    "query": {
        "search_field_1": {
            "term": "polymer protein complex",
            "synonyms": [
                "Polypeptide", "Macronutrient", "Biomolecule", "Enzyme", "Macromolecule", 
                "Nutrient", "Amino acid", "Amino acid chain", "Essential nutrient", "Nutriment", 
                "Proteid", "Albumin", "Casein", "Fibrin", "Globulin", "Prolamin", "Biopolymer", 
                "Macromolecule", "Resin", "Chain molecule", "Large molecule", "Plastic", 
                "Polystyrene", "Vinyl", "Polyvinyl chloride (PVC)", "Polypropylene", 
                "Polyethylene", "Synthetic polymer", "Polyamide", "Copolymer", "Thermoplastic"
            ]
        }
    },
}

# Extract search terms and synonyms
search_terms = [test_json["query"]["search_field_1"]["term"]] + test_json["query"]["search_field_1"]["synonyms"]

# Create a regex pattern to match any of the search terms
search_pattern = "|".join(search_terms)  # Creates regex pattern: "term1|term2|term3"

# Filter rows where "full_caption" contains any of the search terms
filtered_df = df[df["full_caption"].str.contains(search_pattern, case=False, na=False, regex=True)]


# Display or Save the new DataFrame
print(filtered_df.head())  # Show first few rows
filtered_df.to_csv("filtered_data.csv", index=False)  # Save to CSV

print('filtered_data.csv is saved')