import json

if __name__ =="__main__":
    with open("./protocol/my_protocol.json") as json_file:
        my_p = json.load(json_file)
    print(type(my_p))
