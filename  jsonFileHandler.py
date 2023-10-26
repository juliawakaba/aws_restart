import json

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
            print("data:",data)
    except IOError:
        print("Could not read file")
    return data