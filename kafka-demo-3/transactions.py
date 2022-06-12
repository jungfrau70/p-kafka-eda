import faust
import json
import subprocess

class Order(faust.Record):
    account_id: str
    command: str

app = faust.App('order', 
                broker=['localhost:9092','localhost:9093','localhost:9094'],
                store='rocksdb://',
)

topic = app.topic("orders", value_type=Order)
output_topic = app.topic('order_results')
# class UserMetadata(Record, serializer='json'):
#     registered_from: str

# class User(Record, serializer='json'):
#     user_id: int
#     email: str
#     metadata: UserMetadata

## Consumer
# @app.agent(topic)
# async def order_agent(orders: faust.Stream):
#     async for order in orders:
#         print(f"Order for {order.account_id}: {order.command}")


# Consumer
@app.agent(topic)
async def order_agent(orders: faust.Stream):
    async for order in orders:
        # print(f"Order for {order.account_id}: {order.command}")
        result = subprocess.check_output(order.command, shell=True)
        # print(type(result))
        await output_topic.send(value=result)

# @app.agent(topic)
# @app.page('send_to_kafka')
# @app.timer(interval=1.0)
# async def order_sender(app):
#     await topic.send(
#         value=Order(account_id='kr', command='ls -al'),
#     )


# Send messages
# @app.timer(interval=1.0)
# async def send_message(message):
#     await topic.send(value='my message')

if __name__ == '__main__':
    """Simple Faust Producer"""

    # Start the Faust App
    app.main()        