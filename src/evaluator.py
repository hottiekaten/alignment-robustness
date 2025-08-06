import csv
import os
import anthropic

client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))
MODEL = os.getenv("CLAUDE_MODEL", "claude-4-opus")

def evaluate(input_csv='prompts/adversarial_samples.csv', output_csv='results/responses.csv'):
    os.makedirs('results', exist_ok=True)
    with open(input_csv) as fin, open(output_csv, 'w', newline='') as fout:
        reader = csv.DictReader(fin)
        writer = csv.DictWriter(fout, fieldnames=["id", "prompt", "response"])
        writer.writeheader()
        for row in reader:
            resp = client.completions.create(model=MODEL, prompt=row["prompt"], max_tokens=200)
            writer.writerow({"id": row["id"], "prompt": row["prompt"], "response": resp.completion})
