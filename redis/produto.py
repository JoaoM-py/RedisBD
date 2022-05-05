import pymongo
from bson.objectid import ObjectId
import redis
import json

client = pymongo.MongoClient("mongodb+srv://JOAO:joao%40123@cluster0.zdev9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

conR = redis.Redis(
    host = 'redis-17239.c261.us-east-1-4.ec2.cloud.redislabs.com',
    port = '17239',
    password = 'joaobd'
)

global mydb
mydb = client.Mercado_Livre


def findSort():
    #Sort
    global mydb
    mycol = mydb.produto
    print("\n####SORT####")
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(x)


def RedisfindSort():
    print(("\n####redis####"))
    pegar = conR.get('produto:{"_id"}')
    print(pegar) 



def findQuery():
    #Query
    global mydb
    mycol = mydb.produto
    print("\n####QUERY####")
    myquery = { "nome": "Caneca"}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

def insert():
    #Insert
    global mydb
    mycol = mydb.produto
    print("\n####INSERT####")
    mylist = {'nome': 'Garrafa gamer', 'Descricao': 'garrafa dia das mães', 'preco': 5.00 }
    dp = json.dumps(mylist)
    conR.set('produto:{"_id}', {dp})
    ld = json.loads(dp)
    x  = mycol.insert_one(ld)
    print(x.inserted_id)

def update():
    global mydb
    print("\n####UPDATE####")
    mycol = mydb.produto
    print("\n####QUERY####")
    myquery = { 'nome': 'Garrafa gamer', 'Descricao': 'garrafa dia das mães', 'preco': 5.00 }
    newvalues = { "$set": { 'nome': 'caderno gamer', 'Descricao': 'caderno dia das mães', 'preco': 25.00 } }
    mycol.update_one(myquery, newvalues)


def delete():
    global mydb
    print("\n####DELETE####")
    mycol = mydb.produto
    print("\n####QUERY####")
    myquery = {'_id': ObjectId('624f0a741352ad412cfa77c0') }
    mycol.delete_one(myquery)





  


#main
""" findSort()
findQuery()
findSort()
insert()
findSort()
update()
findSort()
delete()
findSort() """
insert()
RedisfindSort()

