# import pandas as pd

# # # Read JSON file
# json_path = "/home/j/jayaverma/exsclaim/output/nature-nano/exsclaim.json"
# df = pd.read_json(json_path)

# # Define CSV file path (same directory, different extension)
# csv_path = json_path.replace(".json", ".csv")

# # Save DataFrame as CSV
# df.to_csv(csv_path, index=False)

# print(f"CSV file saved at: {csv_path}")



# for polymer Protien
import pandas as pd

# # Read JSON file
json_path = "/home/j/jayaverma/exsclaim/output/nature_polymer_protein_complex/exsclaim.json"
df = pd.read_json(json_path)

# Define CSV file path (same directory, different extension)
csv_path = json_path.replace(".json", ".csv")

# Save DataFrame as CSV
df.to_csv(csv_path, index=False)

print(f"CSV file saved at: {csv_path}")
# print(df)