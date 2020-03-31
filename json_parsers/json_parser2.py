
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
    
    def get_ids(self,input_path1,json_text):
        return  [ "id1",json_text["data"][0]["_id"] , "id2",json_text["data"][1]["_id"] ]

    def get_mongodb(self,input_path2,json_text):
        return  json_text["mongodb"]

if __name__ == "__main__":

    Json_obj=JsonReader()
    
    input_path1 = "D:\\Work\\automation-frameworks\\json_parsers\\input1.json"
    out_put = Json_obj.read_file(input_path1)
    load_data=Json_obj.load_json_data(out_put)
    ids=Json_obj.get_ids(input_path1,load_data)
    print(ids)
    
    input_path2 = "D:\\Work\\automation-frameworks\\json_parsers\\input2.json"
    out_put = Json_obj.read_file(input_path2)
    load_data=Json_obj.load_json_data(out_put)
    mongodb_val=Json_obj.get_mongodb(input_path2,load_data)
    print(mongodb_val)
    
    
    


