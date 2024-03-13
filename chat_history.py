from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
from datetime import datetime

class chat_history:
    def __init__(self):
        load_dotenv(find_dotenv())

        self.password = os.environ.get("MONGODB_PWD")
        self.connection_string = f"mongodb+srv://wryzxec:{self.password}@vocalbotcluster.qbcuueg.mongodb.net/?retryWrites=true&w=majority&appName=VocalBotCluster"

        self.client = MongoClient(self.connection_string)
        self.printer = pprint.PrettyPrinter()

        self.vocal_bot_db = self.client["Vocal_Bot"]
        self.collections = self.vocal_bot_db.list_collection_names()


    def insert_chat_log(self, chat_content):
        current_datetime = datetime.now()

        collection = self.vocal_bot_db["Chat_History"]
        chat_document = {
            "content": chat_content,
            "time": f"{current_datetime}"
        }
        collection.insert_one(chat_document)

    def get_chat_logs(self):

        columns = {"_id": 0, "content": 1, "time": 1}
        chat_logs = self.vocal_bot_db["Chat_History"].find({}, columns)

        return chat_logs

    def get_chat_log_count(self):
        count = self.vocal_bot_db["Chat_History"].count_documents({})
        
        return count


