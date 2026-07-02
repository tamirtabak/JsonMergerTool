import json
import os
import glob

# ==================== CONFIGURATION ====================
# Simply change this variable to whatever key your JSON files are using
MASTER_FIELD = "products"
BATCHES_FOLDER = "batches"
OUTPUT_FILE = "master_products.json"
# =======================================================

# Initialize the master dictionary structure using your variable
master_data = {MASTER_FIELD: []}

# Create the search pattern to find files inside the batches folder
search_pattern = os.path.join(BATCHES_FOLDER, "batch*.json")
batch_files = sorted(glob.glob(search_pattern))

if not batch_files:
    print(f"Error: No JSON files starting with 'batch' found in the '{BATCHES_FOLDER}' folder!")
else:
    print(f"Found {len(batch_files)} batch files to merge using key '{MASTER_FIELD}'...")

    # Loop through and extract the items from the specified field
    for file_path in batch_files:
        print(f"Processing: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            file_data = json.load(f)

            # Pull the list from your configured MASTER_FIELD and append it
            if MASTER_FIELD in file_data:
                master_data[MASTER_FIELD].extend(file_data[MASTER_FIELD])
            else:
                print(f"Warning: Key '{MASTER_FIELD}' not found in {file_path}")

    # Save the final merged file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(master_data, f, indent=2)

    print("\nSuccess! 🚀")
    print(f"Your combined file has been saved to: {os.path.abspath(OUTPUT_FILE)}")
