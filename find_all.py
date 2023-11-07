import pymongo

# Replace the connection string with your own.
connection_string = "mongodb://localhost:27017/"

# authentication username and password for mongodb
username = "root"
password = "mongopass"


# Create a MongoClient object.
client = pymongo.MongoClient(
    connection_string, username=username, password=password)

# Access the database.
db = client["studentSummary"]

# Access the collection.
collection = db["summaries"]

# Get all documents from the collection.
documents = collection.find()

# Print each document.
for document in documents:
    print(document)
