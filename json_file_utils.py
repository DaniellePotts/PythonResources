import json 

def read_json_file(json_file):
  with open(json_file) as json_file:
    return json.load(json_file)

def write_json(file, data):
  with open(file, "w") as outfile:
    json.dump(data, outfile)
