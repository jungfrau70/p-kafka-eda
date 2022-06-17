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
                broker=['localhost:9092','localhost:9093','localhost:9094'],
                store='memory://',
)

topic = app.topic('order_results', value_type=Result)
# order_results = app.Table('order_results', default=str)
                   
# class UserMetadata(Record, serializer='json'):
#     registered_from: str

# class User(Record, serializer='json'):
#     user_id: int
#     email: str
#     metadata: UserMetadata

# Consumer
# header = [re.sub(' +',' ',i[0][:-1].replace('\n', ' ')) for i in optionsTable[0]]

# @app.agent(topic)
# async def get_results(events: faust.Stream):
#     async for event in events:    
#         count = 0
#         for index, row in enumerate(event.split('\n')):
#             if count <= 2:
#                 pass
#                 count += 1
#             else:
#                 values = [ col for col in row.split() ]
#                 if len(values) > 10:
#                     await order_results.send(key=index, value=Record(row=[json.dumps(values).encode('utf-8')]))

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

# @app.page('/{region}/{az}/{uuid}/')
# @app.table_route(table=order_results, match_info='uuid')
# async def get_count(web, request, uuid):
#     return web.json({
#         word: order_results,
#     })

# @app.page('/results/')
# @app.table_route(table=order_results, query_param='index')
# async def get_count(web, request):
#     word = request.query['index']
#     return web.json({
#         word: order_results[index],
#     })


# @app.page('/results/')
# @app.table_route(table=order_results, match_info='partition')
# async def get_order_results(web, request, partition):
#     return web.json({
#         partition: order_results[str(partition)],
#     })

# async def get_order_results(self, request):
#     # update the counter
#     # count[0] += 1
#     # and return it.
#     get_results()
    # result = get_results()
    # print(result)
    # return self.json({
    #     get_results(),
    # })


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