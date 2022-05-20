from __future__ import print_function
from kafka import KafkaAdminClient
from pprint import pprint

import os
import subprocess
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
import json

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = ['wf-gcp-us-bigdata-prod']  # TODO: Update placeholder value.

# The name of the zone for this request.
zone = 'us-east4-a'  # TODO: Update placeholder value.

for project in project:
    subprocess.run(["gcloud config set project {}".format(project)], shell=True)
    process=subprocess.run(["gcloud compute instances list --filter \"name ~ kafkac8-pdx1\" --format=\"json\""],check=True, stdout=subprocess.PIPE, universal_newlines=True,shell=True)
    output=process.stdout

data = json.loads(output)
zones={}

for i in range(len(data)):
   name=data[i]["name"]
   brokerid="".join(name.split('g')[1].split('-'))

   zone=data[i]["zone"].split('/')[-1]

   zones[brokerid]=zone

print("\n----------Broker IDs and Respective Zone Information----------")
for keys in zones:
   print(keys,zones[keys])

print('\n')

admin_client = KafkaAdminClient(bootstrap_servers="kafkac8-pdx1-g11-1.c.wf-gcp-us-bigdata-prod.internal:9092", client_id='test')
alltopics=admin_client.list_topics()
topiclist={}

for topic in alltopics:
  metadata=admin_client.describe_topics(topics=[topic])
  output=metadata[0]['partitions']

  for part in range(len(output)):
     topicpart=topic+'-'+str(output[part]['partition'])
     replica=output[part]['replicas'][1:]
     topiclist[topicpart]=[]
     for r in replica:
         topiclist[topicpart].append(zones[str(r)])

print("\n----------Topic Partition Rack Information----------")
rackinfo=False
for key in topiclist:
   if len(topiclist[key]) != len(set(topiclist[key])):
      rackinfo=True
      print(key,topiclist[key])

if not rackinfo:
   print("\n     ******No Topic Partition to Report********")
