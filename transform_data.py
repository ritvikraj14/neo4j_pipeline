import json

# Read protein data from the JSON file
with open('/Users/ritvikraj/airflow/dags/protein.json', 'r') as f:
    protein = json.load(f)

# Transform the protein data
protein_transformed = {
    'accession': protein['accession'],
    'name': protein['recommended_name'],
    'alternative_names': protein['alternative_name'].split('; '),
    'gene': protein['gene_name'],
    'organism': protein['organism']
}

# Write transformed data to a JSON file
with open('/Users/ritvikraj/airflow/dags/protein_transformed.json', 'w') as f:
    json.dump(protein_transformed, f)

