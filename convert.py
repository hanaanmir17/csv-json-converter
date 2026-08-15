"""Convert a file between CSV and JSON, auto-detecting direction from the file extensions."""
import csv
import json
import sys


def csv_to_json(input_path, output_path):
    with open(input_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2)
    print(f"Converted {len(rows)} rows: {input_path} -> {output_path}")


def json_to_csv(input_path, output_path):
    with open(input_path, encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list) or not data:
        print("Input JSON must be a non-empty list of objects.")
        return
    fieldnames = list(data[0].keys())
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Converted {len(data)} rows: {input_path} -> {output_path}")


def main():
    if len(sys.argv) < 3:
        print("Usage: python convert.py <input.csv|input.json> <output.json|output.csv>")
        return

    input_path, output_path = sys.argv[1], sys.argv[2]
    if input_path.endswith(".csv") and output_path.endswith(".json"):
        csv_to_json(input_path, output_path)
    elif input_path.endswith(".json") and output_path.endswith(".csv"):
        json_to_csv(input_path, output_path)
    else:
        print("Could not detect direction. Use a .csv -> .json pair or .json -> .csv pair.")


if __name__ == "__main__":
    main()
