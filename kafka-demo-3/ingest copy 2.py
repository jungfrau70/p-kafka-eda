import csv
import faust
import json
import subprocess

class Output(faust.Record):
    row: str

app = faust.App('order_ingest', 
                broker=['localhost:9092','localhost:9093','localhost:9094'],
                store='rocksdb://',
)

#topic = app.topic("orders", value_type=OrderOutput)
topic = app.topic('order_results')
order_results = app.Table('order_results', default=str,
                        help='Keep count of words (int to str).')
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
# header = [re.sub(' +',' ',i[0][:-1].replace('\n', ' ')) for i in optionsTable[0]]


@app.agent(topic)
async def get_results(outputs: faust.Stream):
    keys = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9')
    async for output in outputs:
        count = 0
        result = []
        for row in output.split('\n'):
            if count <= 2:
                pass
                count += 1
            else:
                values = [ col for col in row.split() ]
                out = dict(zip(keys, values))
                if len(json.dumps(out).encode('utf-8')) > 10:
                    result.append(json.dumps(out).encode('utf-8')) 
        return(result)

@app.page('/results/')
async def get_order_results(self, request):
#     # update the counter
#     # count[0] += 1
#     # and return it.
#     get_results()
    # result = get_results()
    # print(result)
    return self.json({
        get_results(),
    })


# keys = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9')
# values = ('Monty', 42, 'spam')
# out = dict(zip(keys, values))

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