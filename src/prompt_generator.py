import csv
import random
import json

def load_templates(path='prompts/template_prompt.json'):
    with open(path) as f:
        return json.load(f)['templates']

def perturb_template(template):
    return template.replace("help me with", random.choice(["assist", "aid", "guide"]))

def generate_adversarial(n=100, out_path='prompts/adversarial_samples.csv'):
    templates = load_templates()
    rows = []
    for i in range(n):
        t = random.choice(templates)
        pert = perturb_template(t)
        rows.append({"id": i, "prompt": pert})
    with open(out_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "prompt"])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == '__main__':
    generate_adversarial()
