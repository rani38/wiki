import requests
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch
# Wikipedia page URL
url = "https://en.wikipedia.org/wiki/OpenAI"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the main content area of the page
content_div = soup.find(id="mw-content-text")

# Extract the text from the content area
text = content_div.get_text()

# Print the extracted text
print(len(text))

host = 'localhost'
port = 9200
username = 'linux'
password = 'linuxbean5455'
print(f'http://{username}:{password}@{host}:{port}')
# Create the Elasticsearch client
es = Elasticsearch(
    [f'http://{username}:{password}@{host}:{port}'])
print(es.ping())

# Define the index name
index_name = "wikipedia"

# Define the document to be indexed
document = {
    "text": text
}

# Index the document into Elasticsearch
es.index(index=index_name, body=document)

