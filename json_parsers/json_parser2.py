
import json

class JSON: 
    
    def json_read(self,path):
    
        f=open(path,'r')

        data=f.read()

        f.close()

        x=json.loads(data)
    
        return x

if __name__ == "__main__":
    
    j=JSON()
    
    path1 = "D:\\python\\input.json"
    out_put1 = j.json_read(path1)
    print ("id1:",out_put1["data"][0]["_id"])
    print ("id2:",out_put1["data"][1]["_id"])
    
    path2 = "D:\\python\\input2.json"
    out_put2 = j.json_read(path2)
    print (out_put2["mongodb"])
    print(type(out_put2))
