from neo4j import GraphDatabase

# Database Credentials
uri="bolt://localhost:7687"
userName="neo4j"
password="GraphPass"
graph_driver = GraphDatabase.driver(uri, auth=(userName, password))


def insert_query(query):
    """
    :param query:
    :return: None
    """
    try:
        with graph_driver.session() as graphDB_Session:
            graphDB_Session.run(query)
            print("successfully inserted")
    except Exception as e:
        print(e)



def find_query(query):
    """
    :param query:
    :return: relation
    """
    try:
        with graph_driver.session() as graphDB_Session:
            relations = graphDB_Session.run(query)
            return relations
    except Exception as e:
        return e

