import requests

def post(url, headers, data=None):
  response = None
  if data != None:
    response = requests.post(url, headers=headers, json=data)
  else:
    response = requests.post(url, headers=headers)
  
  return {"statusCode":response.status_code, "body":response.json()}

def get(url, headers):
    response = requests.get(url, headers)
    return {"statusCode":response.status_code, "body":response.json()}
    
