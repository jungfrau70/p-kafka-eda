import configparser
import faust
import json
import uuid

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8') 

TOPIC=config['kafka']['topic']
SERVER=config['kafka']['server'].split(',')
REGION=config['command']['region']
AZ=config['command']['az']
COMMAND=config['command']['command']

print(SERVER)

class REQUEST(faust.Record):
    region: str
    az: str
    uuid: str
    command: str

app = faust.App(TOPIC, 
                broker=SERVER,
                store='memory://',
)

topic = app.topic(TOPIC, value_type=REQUEST)

# Producer
@app.timer(interval=1.0)
async def requester(app):
    command_request = REQUEST(region=REGION, az=AZ, uuid = uuid.uuid1(), command=COMMAND)

    await topic.send(
        value = command_request,
    )

if __name__ == "__main__":
    app.main()