from elasticsearch import Elasticsearch

# Connect to Elasticsearch
host = 'localhost'
port = 9200
username = 'linux'
password = 'linuxbean5455'
print(f'http://{username}:{password}@{host}:{port}')

es = Elasticsearch(
    [f'http://{username}:{password}@{host}:{port}'])
print(es.ping())

# Define the index name
index_name = "wikipedia"

# Define the document to be inserted
document = {
    "title": "Example Article",
    "content": "This is the content of the article."
}

# Insert the document into Elasticsearch
response = es.index(index=index_name, body=document)

# Check the response
if response["result"] == "created":
    print("Document inserted successfully.")
else:
    print("Failed to insert document.")