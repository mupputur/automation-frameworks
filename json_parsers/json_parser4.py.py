
import json

    
class Json:

    def json_convert(self,path):
        f=open(input_path.strip("\u202a"),'r')
        data=f.read()
        y=json.loads(data)
        f.close()
        print(y)
        print('#'*50)
        z=y["markers"]
        z[0]["location"]=z[0].pop("position")
        return y
    
    def To_json(self,y):
        self.x=json.dumps(y,indent=4)
        print('#'*50)
        print(self.x)



if __name__=="__main__":
    j=Json()
    input_path="D:\\py\\dependencies\\json\\input1.json"
    out=j.json_convert(input_path)
    print(out)
    put=j.To_json(out)

    
 
#path="D:\\py\\dependencies\\json\\input1.json"
