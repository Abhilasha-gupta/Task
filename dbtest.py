import pymongo
#database connection

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydb"]
mycol = mydb["emp"]

#fetch data from database

for x in mycol.find({},{"ename":1}):
  print(x)
