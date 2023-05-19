from elasticsearch import Elasticsearch

host = 'localhost'
port = 9200
username = 'linux'
password = 'linuxbean5455'
print(f'http://{username}:{password}@{host}:{port}')
# Create the Elasticsearch client
es = Elasticsearch(
    [f'http://{username}:{password}@{host}:{port}'])
print(es.ping())
#create index
# es.indices.create(index="wikipedia")
# Index name and document type
index_name = "wikipedia"  # Replace with the name of your Elasticsearch index
doc_type = "article"  # Replace with the name of your document type

# Question text
question = "What is OpenAI?"

# Elasticsearch search query
query = {
    "query": {
        "match": {
            "content": question
        }
    },
    "highlight": {
        "fields": {
            "content": {}
        }
    }
}

# Execute the search query
result = es.search(index=index_name, doc_type=doc_type, body=query)

# Process the search results
hits = result["hits"]["hits"]
for hit in hits:
    print("Score:", hit["_score"])
    print("Passage:", hit["highlight"]["content"][0])
    print("------")
