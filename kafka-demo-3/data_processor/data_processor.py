import faust
import json
import subprocess

class Order(faust.Record):
    region: str
    az: str
    uuid: str    
    command: str
    
class Result(faust.Record):
    region: str
    az: str
    uuid: str    
    result: str

app = faust.App('order_processing', 
                broker=['10.11.65.187:9092','10.11.65.187:9093','10.11.65.187:9094'],
                store='memory://',
)

topic = app.topic("orders", value_type=Order)
output_topic = app.topic('order_results')

# Consumer & Producer
@app.agent(topic)
async def order_agent(orders: faust.Stream):
    async for order in orders:
        result = Result(
            region = order.region,
            az = order.az,
            uuid = order.uuid,
            result = subprocess.check_output(order.command, shell=True).decode('utf-8')
        )

        await output_topic.send(
            value = result
        )

if __name__ == '__main__':

    # Start the Faust App
    app.main()        