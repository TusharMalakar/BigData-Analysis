# Hetionet : Integrating Biology into a Public Neo4j and Cassandra Database

![Capture](https://user-images.githubusercontent.com/35859780/67837968-ab8b1c00-fac6-11e9-8aab-db8b4a62a079.PNG)

![Capture](https://user-images.githubusercontent.com/35859780/67838071-e2613200-fac6-11e9-840e-001d598e88ed.PNG)




1. start your Cassandra database:
- cassandra.bat -f
- cqlsh 
2. start your Neo4j database
- neo4j using desktop application 

# It is python - flask app with Apache Cassandra Database and Neo4j Graph database:
    1. Use: cmd to run the project:
        - python main.py
        
    2. find a relationship by "disease_name" 
        - http://127.0.0.1:5000/disease?name=disese_name
     
    3. find treats of a disease by disease_id:
        - http://127.0.0.1:5000/d_id?id=Disease::DOID:0050741e
        
    4. add a new node:
        - id, name and kind are required to create new node
        - http://127.0.0.1:5000/add_node?id=nodeID&name=nodeName&kind=nodekind
        
    5. add a new edge:
        - source, metaedge and target are required
        - http://127.0.0.1:5000/add_edges?source=nodesource&metaedge=nodemetaedge&target=nodetarget
    
    7. insert all nodes from node.tsv:
        - http://127.0.0.1:5000/insert_all_nodes
    
    8. insert all edges form edge.tsv:
        - http://127.0.0.1:5000/insert_all_edges
    
        
    
