import csv
import tarfile

from neo4j import GraphDatabase

# Database Credentials
uri="bolt://localhost:7687"
userName="neo4j"
password="GraphPass"
graph_driver = GraphDatabase.driver(uri, auth=(userName, password))


# open tar files
tarfile_list = tarfile.open(r"data\projectI_hetionet.tar.gz")
file_list = tarfile_list.extractall()


# implement insert query
def execute_query(query):
    try:
        with graph_driver.session() as graphDB_Session:
            graphDB_Session.run(query)
    except Exception as e:
        print(e)


# search query
def execute_search(d_name):
    pass


with open(r'resources\projectI_hetionet\nodes.tsv')as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    tsv_headings = next(tsvreader)
    # print(tsv_headings)

    try:
        for eline in tsvreader:
            # header
            line = next(tsvreader)

            if "Anatomy" in line:
                createAnatomy_node = "CREATE  ( node : Anatomy {{ id : {id},  name : {name} }})".format(id=line[0],
                                                                                                        name=line[1])
                print(createAnatomy_node)
                # execute_query(createAnatomy_node)

            if "Compound" in line:
                createCompound_node = "CREATE  ( node : Compound {{ id : {id},  name : {name} }})".format(id=line[0],
                                                                                                          name=line[1])
                print(createCompound_node)
                # execute_query(createCompound_node)

            if "Disease" in line:
                createDisease_node = "CREATE  ( node : Disease {{ id : {id},  name : {name} }})".format(id=line[0],
                                                                                                        name=line[1])
                print(createDisease_node)
                # execute_query(createDisease_node)

            if"Gene" in line:
                createGene_node = "CREATE  ( node : Gene {{ id : {id},  name : {name} }})".format(id=line[0],
                                                                                                  name=line[1])
                print(createGene_node)
                # execute_query(createGene_node)

    except Exception as e:
        print(e)






# # CQL to query all the universities present in the graph
# cqlNodeQuery1="MATCH (x:university) RETURN x"
#
# # CQL to query the distances from Yale to some of the other Ivy League universities
# cqlEdgeQuery1="MATCH (x:university1 {name:'Yale University1'})-[r]->(y:university1) RETURN y.name,r.miles"
#
#
#
# # Execute the CQL query
# with graph_driver.session() as graphDB_Session:
#     # Create nodes
#     graphDB_Session.run(cqlCreate)

#     # Query the graph
#     nodes = graphDB_Session.run(cqlNodeQuery)

#     print("List of Ivy League universities present in the graph:")
#     for node in nodes:
#         print(node)
#
#     # Query the relationships present in the graph
#     nodes = graphDB_Session.run(cqlEdgeQuer1)
#     print("\nDistance from Yale University to the other Ivy League universities present in the graph:")
#
#     for node in nodes:
#         print(node)
