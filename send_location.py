import requests
import time

url = "http://0.0.0.0:4000/update-location"

data = [[3.4, 5.6], [6.7, -1.5]]


while True:
    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Sent")
    else:
        print("upload failed")
    time.sleep(2)
    


