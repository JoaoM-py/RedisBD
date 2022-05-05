from pyclbr import Function
import redis
import json

conR = redis.Redis(
    host = 'redis-17239.c261.us-east-1-4.ec2.cloud.redislabs.com',
    port = '17239',
    password = 'joaobd'
)



""" conR.set('user:name', 'branquinho')

print(conR.get('user:name')) """
conR.set('ticket:braquinho', '{"nome": "branquinhodobololo", "desconto":50}')

def findAll():
    ticket = conR.get('ticket:braquinho')
    js = json.dumps({"response": json.loads(ticket)})
    print(js)










#main
findAll()
