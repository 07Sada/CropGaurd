from pymongo import MongoClient
from dotenv import load_dotenv
import gridfs
import pickle
import os

# Load environment variables from .env file
load_dotenv()

def load_model_and_encoders(model_path, transformer_path, target_encoder_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    with open(transformer_path, 'rb') as f:
        pipeline_encoder = pickle.load(f)

    with open(target_encoder_path, 'rb') as f:
        label_encoder = pickle.load(f)
    
    return model, pipeline_encoder, label_encoder


def retrieve_image_by_name_from_mongodb(file_name, database_name, collection_name):
    # Establish a connection to MongoDB
    client = MongoClient(os.getenv("MONGO_URL"))

    # Access the specified database
    db = client[database_name]

    # Create a new GridFS object (a specification for storing and retrieving large binary objects)
    fs = gridfs.GridFS(db, collection=collection_name)

    # Find the image data using the filename in the metadata
    image_data = fs.find_one({"filename": file_name})

    try:
        if image_data is None:
            raise ValueError("image_data is None")
        
        return image_data.read()
    except Exception as e:
        print(f"An error occurred: {e}")
        raise  # Re-raise the caught exception


def retrieve_data(database_name, collection_name, search_query):
    # Connect to MongoDB
    client = MongoClient(os.getenv("MONGO_URL"))
    database = client[database_name]
    collection = database[collection_name]

    # Search for the document based on the provided query
    result = collection.find_one(search_query)

    client.close()
    return result['data_info']
