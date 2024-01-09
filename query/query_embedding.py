from elasticsearch import Elasticsearch
import json
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

model = SentenceTransformer('all-mpnet-base-v2')

load_dotenv()
client = Elasticsearch(os.getenv("ELASTIC_URL"),
                       ca_certs="./http_ca.crt",
                       basic_auth=("elastic", os.getenv("ELASTIC_PASSWORD")),
                       verify_certs=False)

embedding = model.encode("my phone is frozen")

resp = client.search(knn={
    "field": "text_vector",
    "query_vector": embedding,
    "k": 10,
    "num_candidates": 100
}, index="apple")

print(json.dumps(dict(resp)))