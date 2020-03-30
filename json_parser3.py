import json

class JSON:
    def json_read(self,path):
        f=open(path,'r')
        data=f.read()
        f.close
        x=json.loads(data)
        return x

if __name__ == "__main__":
    
    j=JSON()

    path="C:\\Users\\Admin\\Documents\\json\\json1.txt"
    out_put=j.json_read(path)
    print(out_put.keys())
    
    print(out_put.values())

    print("="*50)

    path="C:\\Users\\Admin\\Documents\\json\\json2.txt"
    out_put2=j.json_read(path)
    print(out_put2.keys())
    
    print(out_put2.values())

    
    

    

    

