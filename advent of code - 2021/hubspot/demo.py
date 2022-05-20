# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer
from kafka.oauth.abstract import AbstractTokenProvider
from keycloak.realm import KeycloakRealm
import logging

#logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)

# Import sys module
import sys

clientid='Kafka-admin-client'
secret='51ceca35-d92e-4e76-9fe1-a197b821f33f'

# Inherit AbstractTokenProvider Class to retrieve and pass access token to kafka
class testtokenprovider(AbstractTokenProvider):
    def token():
       realm = KeycloakRealm(server_url='https://kube-keycloak.service.intraiad1.devconsul.csnzoo.com', realm_name='Kafka-BDE')
       oidc_client = realm.open_id_connect(client_id=clientid,client_secret=secret)
       access_token=oidc_client.client_credentials()['access_token']
       return(access_token)
    def extensions():
        return {}

# Define server with port
bootstrap_servers = ['kafkac18-iad1-g1-2.c.wf-gcp-us-bigdata-dev.internal:9093']

# Define topic name from where the message will recieve
topicName = 'talent-eng-greenhouse_application_events'

provider = testtokenprovider
# Initialize consumer variable
consumer = KafkaConsumer (topicName,
                          client_id='test-keycloak',
                          group_id ='simplepythonconsumer1',
                          bootstrap_servers =bootstrap_servers,
                          auto_offset_reset='earliest',
                          enable_auto_commit=True,
                          api_version=(2,4,1),
                          security_protocol='SASL_SSL',
                          sasl_mechanism='OAUTHBEARER',
                          sasl_oauth_token_provider=provider)

# Read and print message from consumer
for msg in consumer:
   print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))

# Terminate the script
sys.exit()
