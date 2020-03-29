import json

path="C:\\Users\lenova\Downloads\input.json"

f=open(path,"r")

data=f.read()

f.close()

#print(data)

x=json.loads(data)

print("id's:",x["clients"][0]["id"],",",x["clients"][1]["id"],",",x["clients"][2]["id"])
print("name's:",x["clients"][0]["name"],",",x["clients"][1]["name"],",",x["clients"][2]["name"])

print(type(x))

