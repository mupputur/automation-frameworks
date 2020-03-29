import json

path="D:\\python\\input.json"

f=open(path,'r')

data=f.read()

f.close()

x=json.loads(data)

print("id1:",x["data"][0]["_id"])
print("id2:",x["data"][1]["_id"])


print("*"*60)

import json

path="D:\\python\\input2.json"


f=open(path,'r')

data=f.read()

f.close()

x=json.loads(data)

print(x["mongodb"])

print(type(x))


