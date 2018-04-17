from pymongo import MongoClient

connection=MongoClient()
db=connection.test.diniraw7

doc0 = {"ph": int(11),"add":"aaa"}
doc1 = {"ph": int(22),"add":"bbb"}
doc2 = {"ph": int(33),"add":"ccc"}
doc3 = {"ph": int(44),"add":"ddd"}
doc4 = {"ph": int(55),"add":"eee"}

docs = [doc0,doc1,doc2,doc3,doc4]
db.insert_many(docs)


#rec=db.find({"ph":int(22)})
#print rec[1]
