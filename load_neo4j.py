from py2neo import Graph, Node, Relationship
import json

# Read transformed protein data from the JSON file
with open('/Users/ritvikraj/airflow/dags/protein_transformed.json', 'r') as f:
    protein_transformed = json.load(f)

# Create Neo4j nodes and edges
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

protein_node = Node('Protein', accession=protein_transformed['accession'],
                    recommended_name=protein_transformed['name'],
                    gene_name=protein_transformed['gene'],
                    organism=protein_transformed['organism'])

gene_node = Node('Gene', name=protein_transformed['gene'])

organism_node = Node('Organism', name=protein_transformed['organism'])

graph.merge(protein_node, 'Protein', 'accession')
graph.merge(gene_node, 'Gene', 'name')
graph.merge(organism_node, 'Organism', 'name')

protein_gene_rel = Relationship(protein_node, 'encodes', gene_node)
protein_organism_rel = Relationship(protein_node, 'isolated_from', organism_node)

graph.merge(protein_gene_rel)
graph.merge(protein_organism_rel)

