#encoding=utf8

import pandas as pd
import pymongo
from urllib import quote

NEW_USER = "learner"
NEW_PASSWORD = quote("@Mongo!%&Server@")
# NEW_HOST_PORT = "10.47.54.77:27017"
NEW_HOST_PORT = "120.27.162.246:27017"
NEW_DATABASE = "machinelearning"
NEW_MONGO_URL = "mongodb://{0}:{1}@{2}/{3}".format(NEW_USER, NEW_PASSWORD, NEW_HOST_PORT, NEW_DATABASE)
MONGO_URL = NEW_MONGO_URL

with pymongo.MongoClient(host=MONGO_URL) as client:
    db_m = client.get_default_database()
    df_dict = {}
    for name in db_m.collection_names():
        collection = db_m.get_collection(name)
        df_dict[name] = pd.DataFrame(list(collection.find()))

raw_input("Hold -")


