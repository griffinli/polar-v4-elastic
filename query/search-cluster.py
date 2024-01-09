from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

model = SentenceTransformer('all-mpnet-base-v2')

load_dotenv()
client = Elasticsearch(os.getenv("ELASTIC_URL"),
                       ca_certs="./http_ca.crt",
                       basic_auth=("elastic", os.getenv("ELASTIC_PASSWORD")),
                       verify_certs=False)

question = "my iphone broke"

query = {
    "field": "cluster_vector",
    "query_vector": model.encode(question),
    "k": 1,
    "num_candidates": 100
}

res = client.search(index="apple-cluster", knn=query)

print(res)
