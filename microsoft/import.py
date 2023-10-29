from elasticsearch import Elasticsearch
import jsonlines
from datetime import datetime
import elasticsearch.helpers

import os
from dotenv import load_dotenv
load_dotenv()
client = Elasticsearch(os.getenv("ELASTIC_URL"),
                       ca_certs="./http_ca.crt",
                       basic_auth=("elastic", os.getenv("ELASTIC_PASSWORD")),
                       verify_certs=False,
                       request_timeout=None)

tbeg = datetime.now()

#generator or reading in the JSON data
def get_data():

    with jsonlines.open("./microsoft-3.jsonl") as reader:
        for item in reader:
            yield item

# continues import even if there's an error
elasticsearch.helpers.bulk(client, get_data(), index="microsoft", stats_only=True, raise_on_error=False)

elapsed_time = round((datetime.now()-tbeg).total_seconds(), 2)
print("Completed in {} seconds".format(elapsed_time))
