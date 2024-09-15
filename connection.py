#%%
import pandas as pd
import pymongo
#%%
try:
    # Create a connection to the MongoDB server
    client = pymongo.MongoClient('mongodb+srv://emilianogardav:emigymdav6122@mongoaop.zszccwx.mongodb.net/')
    db = client['Dreams']
    coollection  = db['Dreamore']
    documents = coollection.find()
    for doc in documents:
        print(doc)
except Exception as e:
    print(e)
finally:
    client.close()
    print('Connection closed')
# %%
