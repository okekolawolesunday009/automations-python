import json
import os

folder= '/data/feedback'
for filename in os.listdir(folder):
        full_path = os.path.join(folder, filename)

        with open(full_path, "r") as f:
                lines = [line.strip() for line in  f]
                data = {
                        "title": lines[0],
                        "name": lines[1],
                        "feedback": lines[2]
                }
            
        new_name = full_path + "_output.json"
      
        with open(new_name, "w") as f:
            json.dump(data, f, indent=2)
        
        response = requests.post("https://35.199.161.168/feedback/", json=data)
        if response.status_code == 200:
            print(f"Sent {filename} successfully")
        else:
            print(f"Failed to send {filename}: {response.status_code}")


# import os 
# import requests

# BASEPATH = '/data/feedback/'

# folder = os.listdir(BASEPATH)

# list = []

# for file in folder:
#     with open(BASEPATH + file, 'r') as f:
#         list.append({"title":f.readline().rstrip("\n"),
#             		"name":f.readline().rstrip("\n"),
#             		"date":f.readline().rstrip("\n"),
#             		"feedback":f.read().rstrip("\n")})

# for item in list:
#     resp = requests.post('http://127.0.0.1:80/feedback/', json=item)
#     if resp.status_code != 201:
#         raise Exception('POST error status={}'.format(resp.status_code))
#     print('Created feedback ID: {}'.format(resp.json()["id"]))

        
