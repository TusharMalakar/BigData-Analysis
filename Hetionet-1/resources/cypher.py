import csv
import tarfile
from neo4j import GraphDatabase


# open tar files
tarfile_list = tarfile.open(r"data\projectI_hetionet.tar.gz")
file_list = tarfile_list.extractall()
num_nodes, num_edges = 0, 0

# number of edges
with open(r'projectI_hetionet\edges.tsv')as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for eline in tsvreader:
         num_edges = num_edges + 1
    print("number of edges=>", num_edges)

# number of nodes
with open(r'projectI_hetionet\nodes.tsv')as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for nline in tsvreader:
        num_nodes = num_nodes + 1
    print("number of nodes=>", num_nodes)




# # Database Credentials
# uri="bolt://localhost:7687"
# userName="neo4j"
# password="GraphPass"
#
# graph_driver = GraphDatabase.driver(uri, auth=(userName, password))
#
#
#
# # CQL to query all the universities present in the graph
# cqlNodeQuery="MATCH (x:university) RETURN x"
#
# # CQL to query the distances from Yale to some of the other Ivy League universities
# cqlEdgeQuery="MATCH (x:university {name:'Yale University'})-[r]->(y:university) RETURN y.name,r.miles"
#
# # CQL to create a graph containing some of the Ivy League universities
# cqlCreate = """CREATE   (cornell:university { name: "Cornell University"}),
#                         (yale:university { name: "Yale University"}),
#                         (princeton:university { name: "Princeton University"}),
#                         (harvard:university { name: "Harvard University"}),
#
#                         (cornell)-[:connects_in {miles: 259}]->(yale),
#                         (cornell)-[:connects_in {miles: 210}]->(princeton),
#                         (cornell)-[:connects_in {miles: 327}]->(harvard),
#
#                         (yale)-[:connects_in {miles: 259}]->(cornell),
#                         (yale)-[:connects_in {miles: 133}]->(princeton),
#                         (yale)-[:connects_in {miles: 133}]->(harvard),
#
#                         (harvard)-[:connects_in {miles: 327}]->(cornell),
#                         (harvard)-[:connects_in {miles: 133}]->(yale),
#                         (harvard)-[:connects_in {miles: 260}]->(princeton),
#                         (princeton)-[:connects_in {miles: 210}]->(cornell),
#                         (princeton)-[:connects_in {miles: 133}]->(yale),
#                         (princeton)-[:connects_in {miles: 260}]->(harvard)"""
#
#
# # Execute the CQL query
# with graph_driver.session() as graphDB_Session:
#     # Create nodes
#     graphDB_Session.run(cqlCreate)
#     # Query the graph
#     nodes = graphDB_Session.run(cqlNodeQuery)
#     print("List of Ivy League universities present in the graph:")
#
#     for node in nodes:
#         print(node)
#
#     # Query the relationships present in the graph
#     nodes = graphDB_Session.run(cqlEdgeQuery)
#     print("\nDistance from Yale University to the other Ivy League universities present in the graph:")
#
#     for node in nodes:
#         print(node)
