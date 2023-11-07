import pandas as pd
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

# insert csv file into mongodb

# Read the csv file.
df = pd.read_csv("summaries_train.csv")

# Convert the dataframe to a dictionary.
data = df.to_dict("records")

# Access the collection.
collection = db["summaries"]

# Insert the data into the collection.
collection.insert_many(data)
