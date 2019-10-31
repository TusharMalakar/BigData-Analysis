from cassandra.cluster import Cluster

def cqlsh(query):
    cluster = Cluster()
    cql = cluster.connect('hetionet')
    cql.execute('use hetionet')
    cql.execute(query)


