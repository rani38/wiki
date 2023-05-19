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
# Specify the index name
index_name = "wikipedia"

# Define the search query
search_query = {
    "query": {
        "match_all": {}
    }
}

# Perform the search
search_result = es.search(index=index_name, body=search_query)
print(search_result)

# Extract the content from the search result
hits = search_result["hits"]["hits"]
for hit in hits:
    # Access the content of each document
    content = hit["_source"]["content"]
    print(content)