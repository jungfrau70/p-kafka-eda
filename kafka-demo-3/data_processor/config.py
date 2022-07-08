import asyncio

# env Variable
KAFKA_TOPIC_REQUEST="request"
KAFKA_TOPIC_RESPONSE="response"
KAFKA_CONSUMER_GROUP="group-id"
KAFKA_BOOTSTRAP_SERVERS="192.168.171.132:9092,192.168.171.132:9093,192.168.171.132:9094" # Office
# KAFKA_BOOTSTRAP_SERVERS="192.168.54.139:9092,192.168.54.139:9093,192.168.54.139:9094" # Home

REGION="kr"
AZ="1"
TENNANT="prod"
COMMAND="openstack server list"

# loop = asyncio.get_event_loop()