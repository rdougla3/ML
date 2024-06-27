import json
import subprocess
from time import sleep

model = "llama2"
api=["./pull_model.sh", model]
response = subprocess.run(api)

api=["./ask_model.sh", model]
while(True):
    print("\ninput:")
    response = subprocess.run(api + [(input())],  capture_output = True, text = True)
    response = json.loads(response.stdout)
    response = response['response']
    print(response)
    sleep(0.25)