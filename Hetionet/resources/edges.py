import csv
from Cassandra.CQLsh import cqlsh
from Neo4j.query import insert_query


"""Creating dummy relationship: "KNOWS"  to check DB connection"""
dummy_edge = """MATCH  (dummy1: dummy), (dummy2: dummy) where dummy1.name="dummy" and dummy2.name="dummy"
                CREATE (dummy1) - [KNOWS : KNOWS ] -> (dummy2)
                RETURN dummy1, dummy2"""
# insert_query(dummy_edge)


def insert_all_edges():
    with open(r'projectI_hetionet\edges.tsv')as tsvfile:
        """
        reading and appending all types of edges in list
        """
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        tsv_headings = next(tsvreader)
        # appending all types of edges to list
        #['GiG', 'CrC', 'DdG', 'DlA', 'CtD', 'CbG', 'CuG', 'DrD', 'DaG', 'CpD', 'AdG', 'AuG', 'GcG', 'Gr>G', 'CdG', 'DuG', 'AeG']

        for line in tsvreader:
            list = []
            if line[1] not in list:
                list.append(line[1])


# gline = 0
# """
#     reading and inserting all the edges line by line
# """
# with open(r'projectI_hetionet\edges.tsv')as tsvfile:
#     tsvreader = csv.reader(tsvfile, delimiter="\t")
#     tsv_headings = next(tsvreader)
#
#     for line in tsvreader:
#
#         gline = gline + 1  # line counter
#
#         # if "CrC" in line:  # 6486
#         #     # print("Compound resembles Compound")
#         #     CrC_realation = f"""MATCH (a:Compound), (b:Compound)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     crc = f"""insert into hetionet.relation_crc(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     cqlsh(crc)
#         #     # insert_query(CrC_realation)
#         # if "CtD" in line:                    # 755
#         #     # print("Compound treat Disease")
#         #     CtD_realation = f"""MATCH (a:Compound), (b:Disease)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     ctd = f"""insert into hetionet.relation_ctd(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     print(ctd)
#         #     cqlsh(ctd)
#         #     # insert_query(CtD_realation)
#         # if "CpD" in line:                      # 390
#         #     # print("Compound palliates Disease")
#         #     CpD_realation = f"""MATCH (a:Compound), (b:Disease)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     cpd = f"""insert into hetionet.relation_cpd(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     print(cpd)
#         #     cqlsh(cpd)
#         #     # insert_query(CpD_realation)
#         # if "CuG" in line:                       # 18756
#         #     # print("Compound upregulates Gene")
#         #     CuG_realation = f"""MATCH (a:Compound), (b:Gene)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     cug = f"""insert into hetionet.relation_cug(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     print(cug)
#         #     cqlsh(cug)
#         #     # insert_query(CuG_realation)
#         # if "CbG" in line:                      # 11571
#         #     # print("Compound binds Gene")
#         #     CbG_realation = f"""MATCH (a:Compound), (b:Gene)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     cbg = f"""insert into hetionet.relation_cbg(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     print(cbg)
#         #     cqlsh(cbg)
#         #     # insert_query(CbG_realation)
#         # if "CdG" in line:                      # 21102
#         #     # print("Compound downregulates Gene")
#         #     CdG_realation = f"""MATCH (a:Compound), (b:Gene)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     cdg = f"""insert into hetionet.relation_cdg(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     print(cdg)
#         #     cqlsh(cdg)
#         #     # insert_query(CdG_realation)
#         #
#         #
#         #
#         # if "DrD" in line:                       # 543
#         #     # print("Disease resembles Disease")
#         #     DrD_realation = f"""MATCH (a:Disease), (b:Disease)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     drd = f"""insert into hetionet.relation_drd(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     cqlsh(drd)
#         #     # insert_query(DrD_realation)
#         # if "DuG" in line:                         # 7731
#         #     # print("Disease upregulates Gene")
#         #     DuG_realation = f"""MATCH (a:Disease), (b:Gene)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     dug = f"""insert into hetionet.relation_dug(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     cqlsh(dug)
#         #     # insert_query(DuG_realation)
#         # if "DaG" in line:                         # 12623
#         #     # print("Disease associates Gene")
#         #     DaG_realation = f"""MATCH (a:Disease), (b:Gene)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     dag = f"""insert into hetionet.relation_dag(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     cqlsh(dag)
#         #     # insert_query(DaG_realation)
#         # if "DdG" in line:                        # 7623
#         #     # print("Disease downregulates Gene")
#         #     DdG_realation = f"""MATCH (a:Disease), (b:Gene)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     ddg = f"""insert into hetionet.relation_ddg(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     cqlsh(ddg)
#         #     # insert_query(DdG_realation)
#         # if "DlA" in line:                       # 3602
#         #     # print("disease localizes Anatomy")
#         #     DlA_realation = f"""MATCH (a:Disease), (b:Anatomy)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     dla = f"""insert into hetionet.relation_dla(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     cqlsh(dla)
#         #     # insert_query(DlA_realation)
#         #
#         #
#         # if "AuG" in line:                  # 97848
#         #     # print("Anatomy upregulates Gene")
#         #     AuG_realation = f"""MATCH (a:Anatomy), (b:Gene)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     aug = f"""insert into hetionet.relation_aug(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     cqlsh(aug)
#         #     # insert_query(AuG_realation)
#         # if "AeG" in line:                   # 526407
#         #     # print("Anatomy express Gene")
#         #     AeG_realation = f"""MATCH (a:Anatomy), (b:Gene)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     aeg = f"""insert into hetionet.relation_aeg(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     cqlsh(aeg)
#         #     # insert_query(AeG_realation)
#         # if "AdG" in line:                     # 102240
#         #     # print("Anatomy downregulates Gene")
#         #     AdG_realation = f"""MATCH (a:Anatomy), (b:Gene)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     adg = f"""insert into hetionet.relation_adg(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     cqlsh(adg)
#         #     # insert_query(AdG_realation)
#         #
#         #
#         #
#         # if "GiG" in line:                 # 147164
#         #     # print("Gene interacts Gene")
#         #     GiG_realation = f"""MATCH (a:Gene), (b:Gene)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     gig = f"""insert into hetionet.relation_gig(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     cqlsh(gig)
#         #     # insert_query(GiG_realation)
#         # if "GcG" in line:                 # 61690
#         #     # print("Gene covaries Gene")
#         #     GcG_realation = f"""MATCH (a:Gene), (b:Gene)where a.id="{line[0]}" and b.id="{line[2]}"
#         #                     CREATE (a)-[r: {line[1]}]-> (b)
#         #                     RETURN a, b"""
#         #     gcg = f"""insert into hetionet.relation_gcg(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#         #     cqlsh(gcg)
#         #     # insert_query(GcG_realation)
#         if "Gr>G" in line:                     # 265672
#             # print("Gene regulates Gene")
#             Gr_G_realation = f"""MATCH (a:Gene), (b:Gene)where a.id="{line[0]}" and b.id="{line[2]}"
#                             CREATE (a)-[r: Gr_G]-> (b)
#                             RETURN a, b"""
#             grg = f"""insert into hetionet.relation_grg(source, metaedge, target) values( '{line[0]}' , '{line[1]}' , '{line[2]}');"""
#             cqlsh(grg)
#             # insert_query(Gr_G_realation)
#
#     print("Numbers of edges => ", gline, "\nEdges inserted Successfully ")
