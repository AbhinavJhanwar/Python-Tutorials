'''
Created on Jan 30, 2018

@author: abhinav.jhanwar
'''

'''
Start MongoDB:
"C:\Program Files\MongoDB\Server\4.0\bin\mongod.exe" --dbpath="c:\data\db"

Connect to MongoDB:
"C:\Program Files\MongoDB\Server\4.0\bin\mongo.exe"

Install robo mongo - UI for check mongoDB database
'''

from pymongo import MongoClient
import pymongo
import pprint
import datetime
from bson.objectid import ObjectId

# making a connection with mongo client
# client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))
client = MongoClient('localhost', 27017)

# getting a database
db = client['test-database']

# getting a collection
collection = db['test-collection']

# inserting one document
post = {"author": "Chris",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "data": datetime.datetime.utcnow()
        }
posts = db['posts']
post_id = posts.insert_one(post).inserted_id
#print(post_id)

# printing collection names
#print(db.collection_names(include_system_collections=False))
# inserting mulitple documents
new_posts = [{"author": "Chris",
               "text": "Another post!",
               "tags": ["bulk", "insert"],
               "date": datetime.datetime(2009, 11, 12, 11, 14)},
              {"author": "Eliot",
               "title": "MongoDB is fun",
               "text": "and pretty easy too!",
               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
posts_ids = posts.insert_many(new_posts).inserted_ids
#print(posts_ids)

# getting a document
#pprint.pprint(posts.find_one())
#pprint.pprint(posts.find_one({"_id": post_id}))

# updating a document
# update text where author is Eliot
#posts.update_one({"author": "Eliot"}, {'$set':{"text": "easily changed"}})
# querying for more than one document
#for post in posts.find():
#    pprint.pprint(post)

# number of documents
#print(posts.count())
#print(posts.find({"author": "Chrish"}).count())

# deleting documents
#result = db.posts.delete_many({})
#result = db.posts.delete_many({"author": "Chris"})

# dropping a collection
#db.profiles.drop()

# dropping multiple collections
#for collection_name in db.collection_names():
#    db.drop_collection(collection_name)

# creating index - unique value for profiles
#result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],
#                                  unique = True, name = 'myIndex')
#print(sorted(list(db.profiles.index_information())))

# dropping index
#profiles.drop_index('myIndex')

# setting up user profiles
#user_profiles = [
#    {'user_id': 211, "name": "Luke"},
#    {'user_id': 212, "name": "Ziltoid"}]
#profiles = db.profiles
#result = profiles.insert_many(user_profiles)

# trying to add duplicate profile
#duplicate_profile = {'user_id': 211, "name": "Tom"}
#result = db.profiles.insert_one(duplicate_profile)