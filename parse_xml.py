import xml.etree.ElementTree as ET
import json

# Parse the XML file
tree = ET.parse('/Users/ritvikraj/Desktop/Personal/Assignment/Q9Y261.xml')
root = tree.getroot()

# Extract protein information
protein = {
    'accession': root.find('.//{http://uniprot.org/uniprot}accession').text,
    'recommended_name': root.find('.//{http://uniprot.org/uniprot}recommendedName/{http://uniprot.org/uniprot}fullName').text,
    'alternative_name': root.find('.//{http://uniprot.org/uniprot}alternativeName/{http://uniprot.org/uniprot}fullName').text,
    'gene_name': root.find('.//{http://uniprot.org/uniprot}gene/{http://uniprot.org/uniprot}name').text,
    'organism': root.find('.//{http://uniprot.org/uniprot}organism/{http://uniprot.org/uniprot}name').text
}

# Write protein data to a JSON file
with open('/Users/ritvikraj/airflow/dags/protein.json', 'w') as f:
    json.dump(protein, f)
