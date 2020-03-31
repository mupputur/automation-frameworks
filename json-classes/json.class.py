import json

class JsonReader():
    def read_file(self,filepath):
        f=open(filepath,'r')
        data=f.read()
        f.close()
        return data
    def load_json_data(self,data):
        json.text=json.loads(data)
        x=json.text[0]
        return x
    def get_urls(self,x):
        y=x["entities"]["urls"]
        d={}
        for keys,values in y[0].items():
            if keys  in "indices":
                break
            d[keys]=values
        return d

    def get_urls2(self,x):
        z=x["user"]
        h={}
        for keys,values in z.items():
            if keys in "url":
                h[keys]=values
        return h
    def get_urls3(self,x):
        z=x["user"]
        q=z["entities"]["url"]["urls"]
        c={}
        for keys,values in q[0].items():
            if keys in "indices":
                break
            c[keys]=values
        return c
    def get_urls4(self,x):
        z=x["user"]
        w=z["entities"]["description"]
        return w

if __name__=="__main__":

    Json_obj=JsonReader()

    path1="C:\\Users\\srihari\\Documents\\json\\input2.json"
    out_put1 = Json_obj.read_file(path1)
    load_data1=Json_obj.load_json_data(out_put1)
    get_urls=Json_obj.get_urls(load_data1)
    get_urls2=Json_obj.get_urls2(load_data1)
    get_urls3=Json_obj.get_urls3(load_data1)
    get_urls4=Json_obj.get_urls4(load_data1)
    print(get_urls)
    print(get_urls2)
    print(get_urls3)
    print(get_urls4)
