# Hetionet : Integrating Biology into a Public Neo4j and Cassandra Database

# Extract "projectI_hetionet.tar.tz" file running "Tarfile.py"

![Capture](https://user-images.githubusercontent.com/35859780/67837968-ab8b1c00-fac6-11e9-8aab-db8b4a62a079.PNG)

![Capture](https://user-images.githubusercontent.com/35859780/67838071-e2613200-fac6-11e9-840e-001d598e88ed.PNG)




1. start your Cassandra database:
- cassandra.bat -f
- cqlsh 
2. start your Neo4j database
- neo4j using desktop application
# neo4j node model 
![node](https://user-images.githubusercontent.com/35859780/67996596-5e25c080-fc26-11e9-9586-3ce13f1cab1c.PNG)

# neo4j edges model
![edge](https://user-images.githubusercontent.com/35859780/67996646-9f1dd500-fc26-11e9-9f01-c097e156dc7c.PNG)



# It is python - flask app with Apache Cassandra Database and Neo4j Graph database:
Note:
1. start your Cassandra database:
- cassandra.bat -f
- cqlsh 
2. start your Neo4j database
- neo4j using desktop application


 
Neo4j:
# It is python - flask app with Apache Cassandra Database and Neo4j Graph database:
1. Use: cmd to run the project:
    - python main.py

2. find a relationship by "disease_name" 
    - http://127.0.0.1:5000/disease?name=disese_name
    - Return:
        - alcohol dependence resembles bipolar disorder
        - alcohol dependence localizes blood
        - blood down-regulates SETD7
        - blood express HACD3
        - blood up-regulates CLECL1
        - alcohol dependence up-regulates ARHGAP4
        - alcohol dependence associates DRD2
        - alcohol dependence down-regulates NDUFB7

3. find treats of a disease by disease_id:
# MATCH p= (c:Compound)-[:CtD]->(d:Disease{id:"Disease::DOID:0050741"})-->()-->()-->()->() RETURN p LIMIT 2
- http://127.0.0.1:5000/d_id?id=Disease::DOID:0050741e
- Return: 
    - Disease name is alcohol dependence
    - Acamprosate treats alcohol dependence
    - alcohol dependence localize blood
    - alcohol dependence down-regulates SETD7
    - blood express HACD3
    - blood up-regulates CLECL1
        
4. add a new node:
    - id, name and kind are required to create new node
    - http://127.0.0.1:5000/add_node?id=nodeID&name=nodeName&kind=nodekind
    - Return: Success status
5. add a new edge:
    - source, metaedge and target are required
  - http://127.0.0.1:5000/add_edges?source=nodesource&metaedge=nodemetaedge&target=nodetarget    
       - Return: Success status
   
 7. insert all nodes from node.tsv:
    - http://127.0.0.1:5000/insert_all_nodes
    - Return: Success status

8. insert all edges form edge.tsv:
    - http://127.0.0.1:5000/insert_all_edges
    - Return: Success status

