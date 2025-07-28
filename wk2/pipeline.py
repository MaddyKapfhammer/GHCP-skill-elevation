import csv
import sys
import logging
import time
from typing import Callable, List, Dict, Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class ProcessingError(Exception):
    pass

class Pipeline:
    def __init__(self):
        self.steps: List[Callable[[Dict[str, Any]], Dict[str, Any]]] = []

    def add_step(self, step: Callable[[Dict[str, Any]], Dict[str, Any]]):
        self.steps.append(step)
        logging.info(f"Added step: {step.__name__}")

    def run(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        processed = []
        for row in data:
            try:
                for step in self.steps:
                    row = step(row)
                processed.append(row)
            except Exception as e:
                logging.error(f"Error processing row {row}: {e}")
        return processed

def load_csv(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def save_csv(data: List[Dict[str, Any]], file_path: str):
    if not data:
        logging.warning("No data to save.")
        return
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# Example processing steps
def normalize_names(row: Dict[str, Any]) -> Dict[str, Any]:
    row['name'] = row['name'].strip().title()
    return row

def validate_age(row: Dict[str, Any]) -> Dict[str, Any]:
    age = int(row.get('age', -1))
    if age < 0 or age > 120:
        raise ProcessingError("Invalid age")
    row['age'] = age
    return row

def timestamp(row: Dict[str, Any]) -> Dict[str, Any]:
    row['processed_at'] = time.strftime("%Y-%m-%d %H:%M:%S")
    return row

def main():
    if len(sys.argv) < 3:
        print("Usage: pipeline.py input.csv output.csv")
        return

    input_file, output_file = sys.argv[1], sys.argv[2]

    data = load_csv(input_file)
    logging.info(f"Loaded {len(data)} rows")

    pipeline = Pipeline()
    pipeline.add_step(normalize_names)
    pipeline.add_step(validate_age)
    pipeline.add_step(timestamp)

    processed = pipeline.run(data)
    save_csv(processed, output_file)

    logging.info("Processing complete")

if __name__ == "__main__":
    main()
