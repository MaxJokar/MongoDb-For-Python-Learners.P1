from pymongo import MongoClient
import pymongo
from pprint import pprint ,PrettyPrinter
 # pprint:It Displays like JSON format
#PrettyPrinter:is a like template, we can give a format

"""
in cmd we can see follwing mongoDB connected :
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
mongodb://127.0.0.1=>(local host ) IP address which mongo is on it  ,  :27017==> its port
"""


client=MongoClient(host='localhost' , port =27017) #1.connect to client
#MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)
print(client)
print()

db_test=client['test'] #2.inside the clinet made a DataBase
#Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'test')
print(db_test)
print()


#To have collection in our db:
people=db_test['People']#3.inside the db created a  collection named People
#Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'test'), 'People')
print(people)

#Our collection is still empty so we wont see it yet!
# people.insert_one({'name':'Max','family':'Jokar','age':42}) #one record inserted in our  dB
print('-'*100)
#inside the client we get database :
for db in  client.list_database_names():
    print(db)

#------------------------------
# admin
# config
# local
# test
#inside the database we get collection:
for collection in db_test.list_collection_names():
    print(collection )


#Terminal:
# config
# local
# test
# firstDb
# People<== assigned

print('#'*100)
for doc in people.find():
    print(doc)


##############    TERMINAL  #########################################
# {'_id': ObjectId('62f15dd861b8c019e2b741cc'), 'name': 'Max', 'family': 'Jokar', 'age': 42}


# people.insert_one([
#     {'name':'Max','family':'Jokar','age':42},
#     {'name':'Rose','family':'Jokar','age':7}
#     ])


# for doc in people.find({'name':'Max'}):
#     print(doc)

# for doc in people.find({'name':'Max'}):
#     pprint(doc)


# 'family': 'Jokar',
#  'name': 'Max'}
# {'_id': ObjectId('62f161ebce5981a42a2780dd'),
#  'age': 42,
#  'family': 'Jokar',
#  'name': 'Max'}



for doc in people.find({'name':'Max'}):
    PrettyPrinter(indent=4, sort_dicts=False) #sort_dicts:arrangement in list based on words ,etc
    pprint(doc)


# print(people.find().count())#!!!!!!!!!!!!


for doc in people.find().limit(2):
    print(doc)
#Terminal
# {'_id': ObjectId('62f15dd861b8c019e2b741cc'), 'name': 'Max', 'family': 'Jokar', 'age': 42}
# {'_id': ObjectId('62f161ebce5981a42a2780dd'), 'name': 'Max', 'family': 'Jokar', 'age': 42}


print('%'*35)
#UPDATEL
people.update_one({'family':'Jokar'}, {'$set':{'name':'Phil','family':'Bolton','age':12}})
for doc in people.find():
    pprint(doc)
#Terminal:
#{'_id': ObjectId('62f15dd861b8c019e2b741cc'),
#  'age': 12,
#  'family': 'Bolton',
#  'name': 'Phil'}
# {'_id': ObjectId('62f161ebce5981a42a2780dd'),
#  'age': 12,
#  'family': 'Bolton',
#  'name': 'Phil'}
# {'_id': ObjectId('62f161ebce5981a42a2780de'),
#  'age': 12,
#  'family': 'Bolton',
#  'name': 'Phil'}

print('REMOVE '*30)
#REMOVE:
people.remove({'name':'Rose'})
for doc in people.find():
    pprint(doc)

#Terminate with DataBase
client.close()












