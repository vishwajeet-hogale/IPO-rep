import pymongo
import json
from bson.json_util import dumps
mongo = pymongo.MongoClient("mongodb://vishwajeet:Mjklop@cluster0-shard-00-00.pkcgw.mongodb.net:27017,cluster0-shard-00-01.pkcgw.mongodb.net:27017,cluster0-shard-00-02.pkcgw.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-5kisj2-shard-0&authSource=admin&retryWrites=true&w=majority")

db = mongo["IPO"]

def upload_data(df):
    news_data = pymongo.collection.Collection(db, 'news')
    for i in df.values:
        data_format = dict()
        data_format["id"] = i[1]
        data_format["title"] = i[2]
        data_format["link"] = i[3]
        data_format["publish_date"] = i[4]
        data_format["scraped_date"] = i[5]
        data_format["text"] = i[6]
        data_format["summary"] = i[7]
        news_data.insert_one(data_format)
    return {"Status ": "Success"}

def get_data():
    news_data = pymongo.collection.Collection(db, 'news')
    data = json.loads(dumps(news_data.find()))
    # print(data)
    return data