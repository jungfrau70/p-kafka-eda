import csv
import configparser
import faust
import json
import subprocess
import uuid

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8') 

REQUEST_TOPIC=config['kafka']['requestTopic']
RESPONSE_TOPIC=config['kafka']['responseTopic']
SERVER=config['kafka']['server'].split(',')
REGION=config['command']['region']
AZ=config['command']['az']
COMMAND=config['command']['command']

class RESPONSE(faust.Record):
    region: str
    az: str
    uuid: str    
    result: str
    
class RECORD(faust.Record):
    c1: str
    c2: str
    c3: str
    c4: str
    c5: str
    c6: str
    c7: str
    c8: str
    c9: str

app = faust.App('response', 
                broker=SERVER,
                store='memory://',
)

response_topic = app.topic(RESPONSE_TOPIC, value_type=RESPONSE)

# Consumer
@app.agent(response_topic)
async def response(records: faust.Stream):
    async for record in records:
        print(record.region, record.az, record.uuid)
        
        # print(record.result)
        count = 0
        for row in record.result.split('\n'):
            if count <= 2:
                pass
                count += 1
            else:                        
                field = [ col for col in row.split() ]
                if len(field) > 2:
                # row=Record([ col for col in row.split() ])
                    print(f"Record for {field[0]}: {field[2]} {field[8]}")


if __name__ == '__main__':
    
    # Start the Faust App
    app.main()        