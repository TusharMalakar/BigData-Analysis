# Hetionet : Integrating Biology into a Public Neo4j Database

# It is python - flask app with Apache Cassandra Database and Neo4j Graph database:
    1. type: cmd run the project:
        - python main.py
        
    2. find a relationship by "disease_name"
        - http://127.0.0.1:5000/disease?name=disese_name
        
    3. add a new node:
        - id, name and kind are required to create new node
        - http://127.0.0.1:5000/add_node?id=nodeID&name=nodeName&kind=nodekind
        
    4. add a new edge:
        - source, metaedge and target are required
        - http://127.0.0.1:5000/add_edges?source=nodesource&metaedge=nodemetaedge&target=nodetarget
        
    
