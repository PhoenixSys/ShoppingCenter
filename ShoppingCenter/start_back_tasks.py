import time
from datetime import datetime

import requests

while True:
    resp = requests.post("http://127.0.0.1:8000/fa/tasks/start/", data={"token": "HiAdmin"})
    print(datetime.now(), " | ", resp.json())
    time.sleep(10)
