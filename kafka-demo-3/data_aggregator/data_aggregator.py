import csv
import faust
import json
import subprocess

class Result(faust.Record):
    region: str
    az: str
    uuid: str    
    result: str
    
class Record(faust.Record):
    c1: str
    c2: str
    c3: str
    c4: str
    c5: str
    c6: str
    c7: str
    c8: str
    c9: str

app = faust.App('order_results', 
                broker=['10.11.65.187:9092','10.11.65.187:9093','10.11.65.187:9094'],
                store='memory://',
)

topic = app.topic('order_results', value_type=Result)

# Consumer
@app.agent(topic)
async def order_agent(records: faust.Stream):
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