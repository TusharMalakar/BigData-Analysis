import csv
from Cassandra.CQLsh import cqlsh
from Neo4j.query import insert_query

"""Dummy insertion to check DB connection"""
dummy_node = """CREATE (dummy_node: dummy{name: "dummy"})"""
insert_query(dummy_node)


aline = 0  # line counter


def insert_all_nodes():
    """
    reading and inserting all the nodes line by line
    """
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



aline = 0
cline = 0
dline = 0
gline = 0
with open(r'projectI_hetionet\nodes.tsv')as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        tsv_headings = next(tsvreader)
        for line in tsvreader:

            if "Anatomy" in line and aline < 10:
               a_query = f"""insert into hetionet.anatomy1(id, kind, name) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
               print(a_query)
               cqlsh(a_query)
               aline = aline + 1


            if "Compound" in line and cline < 10:
                c_query = f"""insert into hetionet.compound1(id, kind, name) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
                cqlsh(c_query)
                cline = cline + 1


            if "Disease" in line and dline < 10:
                d_query = f"""insert into hetionet.disease1(id, kind, name) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
                print(d_query)
                cqlsh(d_query)
                dline = dline + 1


            if"Gene" in line and gline < 10:
                q_query = f"""insert into hetionet.gene1(id, kind, name) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
                cqlsh(q_query)
                gline = gline + 1

        print("Numbers of nodes => ", aline, "\nNodes inserted successfully!")
