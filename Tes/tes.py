from pysondb import db 

data = db.getDb("database.json")

d = data.getAll()
print(d[0]["judul"])