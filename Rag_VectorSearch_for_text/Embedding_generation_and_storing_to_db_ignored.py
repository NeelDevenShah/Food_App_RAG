# %% [markdown]
# <h1>In this, I have used the server, Which contains the tokenizer from hugging face, Tokenizer used is : sentence-transformers/all-MiniLM-L6-v2</h1>
# While using the api interface of hugging face there is the limit of using, that's why i have made the endpoint named server under Tokenizer_Server directory which can be deployed on the cloud service and the tokenizer service can be utilized, For experimental purpose this server was hosted on azure.

# %%
import pymongo
import os
import json
from bson import ObjectId
import asyncio
import aiohttp

async def process_data():
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb+srv://neel_shah:W5BLOeLu10lXXcWx@cluster0.uxysjwl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client['food_db']
    collection = db['Restraunt_CSV']
    cluster_data = collection.find()

    # Iterate over the data and add the embedding to each document
    for data in cluster_data:
        async with aiohttp.ClientSession() as session:
            url = f"http://20.197.8.42:5000/preprocess"
            headers = {"Content-Type": "application/json"}
            # Convert ObjectId to string
            data["_id"] = str(data["_id"])
            try:
                async with session.post(url, headers=headers, data=json.dumps(data)) as response:
                    json_data = await response.json()
                    collection.update_one({"_id": ObjectId(data["_id"])}, {"$set": {"embedding": json_data["embeddings"]}})
            except aiohttp.ClientConnectionError:
                print("Connection closed. Unable to make API call.")
            print(data["_id"])
            print("Processed")
if __name__ == "__main__":
    asyncio.run(process_data())
