import json

def main():
    data={}
    data['Humidity']=4000
    data['Temperature']=400
    data['Light']=200
    json_object=json.dumps(data,indent=4)
    with open('./bin/Debug/demo.json','w') as outFile: outFile.write(json_object)

if __name__ == "__main__":
    main()