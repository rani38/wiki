from elasticsearch import Elasticsearch
import warnings
host = 'localhost'
port = 9200
username = 'linux'
password = 'linuxbean5455'
# print(f'http://{username}:{password}@{host}:{port}')
# Create the Elasticsearch client
es = Elasticsearch(
    [f'http://{username}:{password}@{host}:{port}'])
print(es.ping())

# Define the index name
index_name = "wikipedia"

# Define the question
question = "openai"

# # Define the search query
# search_query = {
#     "query": {
#         "match": {
#             "text": question
#         }
#     }
# }

search_query = {
  "query": {
    "match": {
      "field_name": question
    }
  }
}

# Execute the search query
response = es.search(index=index_name, body=search_query)
print(response)

# Reset the warning filter
warnings.resetwarnings()
# Extract the answer from the search response
# answer = response["hits"]["hits"][0]["_source"]["text"]

# Print the answer
# print(answer)