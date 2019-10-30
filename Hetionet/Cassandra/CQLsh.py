import json
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


"""
Get credentials from Kubernetes. The credentials were set up as a dictionary. For example:
{
    "username": "USERNAME",
    "password": "PASSWORD"
}
"""
credentials = None
with open('/var/run/secrets/user_credentials/cassandra_credentials') as f:
    credentials = json.load(f)
# Verify the credentials were pulled correctly
if credentials:
    # Setup authentication mechanism
    auth_provider = PlainTextAuthProvider(
        username=credentials.get('username'),
        password=credentials.get('password')
    )

    # Pass parameters to the cluster
    cluster = Cluster(
        auth_provider=auth_provider,
        contact_points=['support-cassandra.dev.anaconda.com']
    )

    # Connect to cluster and set the keyspace
    session = cluster.connect()
    session.set_keyspace('quote')

    # Run query in keyspace and print out the results
    rows = session.execute('SELECT * FROM historical_prices')
    for row in rows:
        print(row)

    # Disconnect from the cluster
    cluster.shutdown()
