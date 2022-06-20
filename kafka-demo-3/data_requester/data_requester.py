import faust
import json
import uuid

class Order(faust.Record):
    region: str
    az: str
    uuid: str
    command: str

app = faust.App('order', 
                broker=['10.11.65.187:9092','10.11.65.187:9093','10.11.65.187:9094'],
                store='memory://',
)

topic = app.topic("orders", value_type=Order)

# Producer
@app.timer(interval=1.0)
async def order_sender(app):
    order = Order(region='kr', az='kr1', uuid = uuid.uuid1(), command='ls -al')

    await topic.send(
        value = order,
    )

if __name__ == "__main__":
    app.main()