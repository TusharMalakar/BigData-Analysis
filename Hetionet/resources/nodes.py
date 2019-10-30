import csv
from Neo4j.query import insert_query

"""Dummy insertion to check DB connection"""
dummy_node = """CREATE (dummy_node: dummy{name: "dummy"})"""
insert_query(dummy_node)


"""
    reading and inserting all the nodes line by line
"""
aline = 0   # line counter

with open(r'projectI_hetionet\nodes.tsv')as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    tsv_headings = next(tsvreader)
    for line in tsvreader:
        aline = aline + 1
        # if "Anatomy" in line:
        #     createAnatomy_node = f"""CREATE   ( Anatomy : Anatomy {{ id : "{line[0]}",  name : "{line[1]}", kind : "{line[2]}" }})"""
        #     insert_query(createAnatomy_node)
        #
        # if "Compound" in line:
        #     createCompound_node = f"""CREATE  ( Compound : Compound {{ id : "{line[0]}",  name : "{line[1]}", kind : "{line[2]}"  }})"""
        #     insert_query(createCompound_node)
        #
        # if "Disease" in line:
        #     createDisease_node = f"""CREATE  ( Disease : Disease {{ id : "{line[0]}",  name : "{line[1]}", kind : "{line[2]}"  }})"""
        #     insert_query(createDisease_node)
        #
        # if"Gene" in line:
        #     createGene_node = f"""CREATE  ( Gene : Gene {{ id : "{line[0]}",  name : "{line[1]}", kind : "{line[2]}"  }})"""
        #     insert_query(createGene_node)

    print("Numbers of nodes => ", aline, "\nNodes inserted successfully!")
