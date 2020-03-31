import json

class JsonReader():
    def read_file(self,filepath):
        f=open(filepath,"r")
        data=f.read()
        f.close()
        return data

    def load_json_data(self,data):
        json_text=json.loads(data)
        return json_text

    def get_ids(self,path,json_text):
        return  "id's:", json_text["clients"][0]["id"],",",json_text["clients"][1]["id"],",",json_text["clients"][2]["id"]

    def get_names(self,path,json_text):
        return "name's:",json_text["clients"][0]["name"],",",json_text["clients"][1]["name"],",",json_text["clients"][2]["name"]

if __name__=="__main__":

    Json_obj=JsonReader()

    path1="C:\\Users\\lenova\\Desktop\\json\\automation-frameworks\\json_praser3\\json_file.json"
    out_put1 = Json_obj.read_file(path1)
    load_data1=Json_obj.load_json_data(out_put1)
    ids=Json_obj.get_ids(path1,load_data1)
    names=Json_obj.get_names(path1,load_data1)
    print(ids)
    print (names)


    
    

        
        
        
        


