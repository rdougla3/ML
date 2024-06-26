import subprocess
from time import sleep


while(True):
    api=["./ask_model.sh", "moondream"]
    print("input:")
    response = subprocess.run(api + [(input())])
    print(response)
    sleep(0.25)