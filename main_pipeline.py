import os
import pandas as pd
from config import validate_config, INPUT_DIR, OUTPUT_FILE
from ai_processor import extract_structured_data
from mock_data_generator import generate_sandbox


def run_pipeline():
    print("=== STARTING ENTERPRISE DATA INTAKE PIPELINE ===")
    
    # 1. Initialize and validate environment
    validate_config()
    
    # Automatically generate dummy data if directory is missing or empty
    if not os.path.exists(INPUT_DIR) or len(os.listdir(INPUT_DIR)) == 0:
        generate_sandbox()

    all_records = []
    files_to_process = os.listdir(INPUT_DIR)
    print(f"[SYSTEM] Found {len(files_to_process)} target files inside intake folder.\n")

    # 2. Iterate through files sequentially
    for filename in files_to_process:
        file_path = os.path.join(INPUT_DIR, filename)
        print(f"Processing File: {filename}")
        
        with open(file_path, "r", encoding="utf-8") as f:
            raw_content = f.read()

        # Execute extraction logic
        structured_record = extract_structured_data(raw_content)
        
        if structured_record:
            # Inject metadata for data lineage tracking
            structured_record["source_file"] = filename
            all_records.append(structured_record)
            print(f"  [SUCCESS] Extracted record for: {structured_record.get('sender_name')}")
        else:
            print(f"  [FAILED] Skipping corrupted or empty record.")
        print("-" * 50)

    # 3. Process records with Pandas and compile database
    if all_records:
        df = pd.DataFrame(all_records)
        
        # Enforce column structure layout
        column_order = ["sender_name", "organization", "contact_channel", "intent", "financial_value", "priority", "source_file"]
        df = df.reindex(columns=column_order)
        
        # Write to final CSV
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"\n[PIPELINE COMPLETE] Generated structured database: '{OUTPUT_FILE}'")
        print(df.to_string())
    else:
        print("\n[ABORTED] No valid records extracted to save.")

if __name__ == "__main__":
    run_pipeline()