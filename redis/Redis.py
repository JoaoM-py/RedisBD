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
conR.set('produto:caneca', '{"nome": "Caneca maneira", "preco":50.00}')

def findAll():
    ticket = conR.get('produto:caneca')
    js = json.dumps({"response": json.loads(ticket)})
    print(js)

def delete():
    print("\n####DELETE####")
    conR.delete('produto:caneca')
    dl = conR.get('produto:caneca')
    print(dl)












#main
findAll()
delete()

