import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

# Import ObjectId from bson package (part of PyMongo distribution) to enable querying by ObjectId
from bson.objectid import ObjectId

# Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'sample_supplies' database
db = client.sample_supplies

# Get a reference to the 'sales' collection
accounts_collection = db.sales

# TODO: Create a filter document to find all sales with a store location of 'Austin' by replacing the <field> and <value> placeholders
documents_to_find = {"<field>": "<value>"}

# Find documents
cursor = accounts_collection.find(documents_to_find)

# Print documents
for document in cursor:
    pprint.pprint(document)
    print()


client.close()