from elasticsearch import Elasticsearch

import os
from dotenv import load_dotenv
load_dotenv()
client = Elasticsearch(os.getenv("ELASTIC_URL"),
                       ca_certs="./http_ca.crt",
                       basic_auth=("elastic", os.getenv("ELASTIC_PASSWORD")),
                       verify_certs=False)

client.indices.delete(index='apple')
