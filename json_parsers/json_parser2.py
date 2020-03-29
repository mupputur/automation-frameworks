
import json

class JsonReader:
    
    def read_file(self,filepath):
        f=open(filepath,'r')
        data=f.read()
        f.close()
        return data

    def load_json_data(self,data):
        json_text=json.loads(data)
        return json_text
    
    def get_ids(self,path,json_text):
        return  [ "id1",json_text["data"][0]["_id"] , "id2",json_text["data"][1]["_id"] ]

    def mongo_db(self,path,json_text):
        return  json_text["mongodb"]

if __name__ == "__main__":

    Json_obj=JsonReader()
    
    path1 = "D:\\Work\\automation-frameworks\\json_parsers\\input.json"
    out_put1 = Json_obj.read_file(path1)
    load_data1=Json_obj.load_json_data(out_put1)
    ids=Json_obj.get_ids(path1,load_data1)
    print(ids)
    

    path2 = "D:\\Work\\automation-frameworks\\json_parsers\\input2.json"
    out_put2 = Json_obj.read_file(path2)
    load_data2=Json_obj.load_json_data(out_put2)
    mongodb_val=Json_obj.mongo_db(path2,load_data2)
    print(mongodb_val)
    
    
    


