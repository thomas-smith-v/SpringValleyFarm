import json
import socket
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os
import time

from src import config

def post(sourcetype: str, eventtype: str, fields: dict):
    try:
        cfg = config.load_config()
        headers = {"Authorization":f"Splunk {cfg['token']}"}
        
        data = {
            "index": cfg['index'],
            "host":str(socket.gethostname()),
            "sourcetype":sourcetype,
            "event":eventtype,
            "fields":fields
            }
        
        # print('URL: ' + cfg['url'] + '\nHeaders: ' + json.dumps(headers) + '\nData: ' + json.dumps(data, indent=4))
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        response = requests.post(cfg['url'], headers=headers, json=data, verify=False)
        print(f"[{int(str(time.time()).split('.')[0])}] Uploaded {data['fields']['metric_name']} -> Response: {response.status_code}")
        return response
        
    except Exception as e:
        print(str(e))
    
def get():
    pass
    
