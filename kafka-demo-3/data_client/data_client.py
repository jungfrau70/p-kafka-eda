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

# Consumer
@app.agent(topic)
async def order_agent(records: faust.Stream):
    async for record in records:
        print(record.region, record.az, record.uuid, record.command)


if __name__ == '__main__':
    
    # Start the Faust App
    app.main()        