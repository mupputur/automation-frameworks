import json
class JsonReader:
    def read_json(self,input_path):
        with open(input_path.strip("\u202a"),'r') as f:
            data=f.read()
            return data
    def load_json(self,data):
        load_data=json.loads(data)
        return load_data
    def get_markers(self,load_data):
        try:
            z=load_data["markers"]
            z[0]["location"]=z[0].pop("position")
            return load_data
        except Exception as TypeError:
            print("invalid key {}".format(TypeError))
    def convert_json(self,y):
        result=json.dumps(y,indent=4)
        return result
if __name__=="__main__":
    j=JsonReader()
    input_path="..\\json_parsers\\input1.json"
    json_data=j.read_json(input_path)
    load=j.load_json(json_data)
    get=j.get_markers(load)
    conv_json=j.convert_json(get)
    print(conv_json)
 
