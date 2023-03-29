# neo4j_pipeline

1. Download and install Neo4j from the official website https://neo4j.com/download/
2. Setup airflow by following the instructions here: https://airflow.apache.org/docs/apache-airflow/stable/start.html
3. Dowload the xml file Q9Y261.xml from the repo https://github.com/weavebio/data-engineering-coding-challenge/tree/main/data
4. Dowload the repo https://github.com/ritvikraj14/neo4j_pipeline/ and keep all the files in the directory /Users/<username>/airflow/dags/
        parse_xml.py
        transform_data.py
        load_neo4j.py
        neo4j_pipeline.py


5. Update the absolute path in the above files

neo4j_pipeline.py:
        line 26: /Users/<username>/airflow/dags/parse_xml.py
        line 33: /Users/<username>/airflow/dags/transform_data.py
        line 40: /Users/<username>/airflow/dags/load_neo4j.py

parse_xml.py:
        line 5: /Users/<username>/Desktop/Personal/Assignment/Q9Y261.xml
        line 18: /Users/<username>/airflow/dags/protein.json

transform_data.py:
        line 4: /Users/<username>/airflow/dags/protein.json
        line 17: /Users/<username>/airflow/dags/protein_transformed.json

load_neo4j.py:
        line 5: /Users/<username>/airflow/dags/protein_transformed.json
        line 9: change the password as given while setting up the neo4j db


6. start airflow using the following command:
        airflow standalone
