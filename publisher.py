import csv
import json
from google.cloud import pubsub_v1

project_name =  'rugged-shuttle-292918'
#'My First Project'
topic_name = 'my-topic'
file_name = 'data.csv'

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_name, topic_name)
print(topic_path)
with open(file_name) as file:
    rd = csv.DictReader(file, delimiter ='|')
    for row in rd:
        data = json.dumps(dict(row))
        publisher.publish(topic_path, data = data.encode('utf-8'))
