import pymongo

client = pymongo.MongoClient("mongodb+srv://varun1904:varun1904@bhoomi.fqx6sgs.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d= {
    'name': 'varun',
    'email' : 'varunsharma.b',
    'surname': 'Sharma'
}

db1= client['mongodb0']
coll =db1['test']
coll.insert_one(d)