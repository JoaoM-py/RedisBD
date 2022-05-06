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

def find():
    Req = conR.get('produto:caneca')
    ReqJson = json.dumps({"Produto": json.loads(Req)})
    return ReqJson



def delete():
    print("\n####DELETE####")
    conR.delete('produto:caneca')
    empty = conR.get('produto:caneca')
    if empty == None:
        empty = "Produto não existe ou foi deletado"
    return empty




#main
print(f"{find()}")
print(f"{delete()}")









