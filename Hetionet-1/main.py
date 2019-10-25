import csv
from neo4j import GraphDatabase

# Database Credentials
uri="bolt://localhost:7687"
userName="neo4j"
password="GraphPass"
num_nodes, num_edges = 0, 0

graph_driver = GraphDatabase.driver(uri, auth=(userName, password))


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


# with open(r'resources\projectI_hetionet\nodes.tsv')as tsvfile:
#     tsvreader = csv.reader(tsvfile, delimiter="\t")
#     tsv_headings = next(tsvreader)
#     # print(tsv_headings)
#
#     try:
#         for eline in tsvreader:
#             # header
#             line = next(tsvreader)
#             num_nodes = num_nodes + 1
#             print("Inserting node number =>", num_nodes)
#             """
#             1. creating queries as f_stream.
#             2. inserting queries in noo4j graph DB
#             """
#             if "Anatomy" in line:
#                 createAnatomy_node = f"""CREATE   ( Anatomy : Anatomy {{ id : "{line[0]}",  name : "{line[1]}", kind : "{line[2]}" }})"""
#                 # print(createAnatomy_node)
#                 execute_query(createAnatomy_node)
#
#             if "Compound" in line:
#                 createCompound_node = f"""CREATE  ( Compound : Compound {{ id : "{line[0]}",  name : "{line[1]}", kind : "{line[2]}"  }})"""
#                 # print(createCompound_node)
#                 execute_query(createCompound_node)
#
#             if "Disease" in line:
#                 createDisease_node = f"""CREATE  ( Disease : Disease {{ id : "{line[0]}",  name : "{line[1]}", kind : "{line[2]}"  }})"""
#                 # print(createDisease_node)
#                 execute_query(createDisease_node)
#
#             if"Gene" in line:
#                 createGene_node = f"""CREATE  ( Gene : Gene {{ id : "{line[0]}",  name : "{line[1]}", kind : "{line[2]}"  }})"""
#                 # print(createGene_node)
#                 execute_query(createGene_node)
#
#     except Exception as e:
#         print(e)


with open(r'resources\projectI_hetionet\edges.tsv')as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    tsv_headings = next(tsvreader)

    # # appending all types of edges to list
    # #['GiG', 'CrC', 'DdG', 'DlA', 'CtD', 'CbG', 'CuG', 'DrD', 'DaG', 'CpD', 'AdG', 'AuG', 'GcG', 'Gr>G', 'CdG', 'DuG', 'AeG']
    # list = []
    #     if eline[1] not in list:
    #         list.append(eline[1])
    # print(list)
    # print(len(list))

    for line in tsvreader:
        if "CrC" in line:
            print("Compound resembles Compound")
        if "CtD" in line:
            print("Compound treat Disease")
        if "CpD" in line:
            print("Compound palliates")
        if "CuG" in line:
            print("Compound upregulates Gene")
        if "CbG" in line:
            print("Compound binds Gene")
        if "CdG" in line:
            print("Compound downregulates Gene")

        if "DrD" in line:
            print("Disease resembles Disease")
        if "DuG" in line:
            print("Disease upregulates Disease")
        if "DaG" in line:
            print("Disease associates Disease")
        if "DdG" in line:
            print("Disease downregulates Disease")
        if "DlA" in line:
            print("disease localizes Anatomy")


        if "AuG" in line:
            print("Anatomy upregulates Gene")
            # relation_AuG = f"""CREATE   ( Anatomy : Anatomy {{ id : "{line[0]}",  name : "{line[1]}", kind : "{line[2]}" }})"""
            # execute_query(relation_AuG)
        if "AeG" in line:
            print("Anatomy express Gene")
            # relation_AeG = f"""CREATE   ( Anatomy : Anatomy {{ id : "{line[0]}",  name : "{line[1]}", kind : "{line[2]}" }})"""
            # execute_query(relation_AeG)
        if "AdG" in line:
            print("Anatomy downregulates Gene")
            # relation_AdG = f"""CREATE   ( Anatomy : Anatomy {{ id : "{line[0]}",  name : "{line[1]}", kind : "{line[2]}" }})"""
            # execute_query(relation_AdG)


        if "GiG" in line:
            print("Gene interacts Gene")
            # relation_GiG = f"""CREATE   ( Anatomy : Anatomy {{ id : "{line[0]}",  name : "{line[1]}", kind : "{line[2]}" }})"""
            # execute_query(relation_GiG)
        if "GcG" in line:
            print("Gene covaries Gene")
            # relation_GcG = f"""CREATE   ( Anatomy : Anatomy {{ id : "{line[0]}",  name : "{line[1]}", kind : "{line[2]}" }})"""
            # execute_query(relation_GcG)
        if "Gr>G" in line:
            print("Gene regulates Gene")
            # relation_Gr>G = f"""CREATE   ( Anatomy : Anatomy {{ id : "{line[0]}",  name : "{line[1]}", kind : "{line[2]}" }})"""
            # execute_query(relation_Gr>G)



        # (harvard)-[:connects_in {miles: 327}]->(cornell)
