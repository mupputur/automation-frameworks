import json

path="C:\\Users\\srihari\\Documents\\json\\input2.json"
f=open(path,"r")
data=f.read()
f.close()
data2=json.loads(data)
x=data2[0]
y=x["entities"]["urls"]

for keys,values in y[0].items():
    if keys  in "indices":
        break
    print(keys,"-",values)
z=x["user"]
for keys,values in z.items():
    if keys in "url":
            print(keys,"_",values)
q=z["entities"]["url"]["urls"]
for keys,values in q[0].items():
    if keys in "indices":
        break
    print(keys,"-",values)
w=z["entities"]["description"]
print(w)

    
        
          
