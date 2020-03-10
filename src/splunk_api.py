#!/home/pi/Documents/student_farm_iot/src/env python3
import json
import socket
import requests
import config

def post(sourcetype: str, eventtype: str, fields: dict):
    try:
        cfg = config.load_config()
        headers = {"Authorization":f"Splunk {cfg['token']}"}
        
        data = {
            "index": cfg['index'],
            "host":socket.gethostname(),
            "sourcetype":sourcetype,
            "event":eventtype,
            "fields":fields
            }
        
        print('URL: ' + cfg['url'] + '\nHeaders: ' + json.dumps(headers) + '\nData: ' + json.dumps(data, indent=4))
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        response = requests.post(cfg['url'], headers=headers, json=data, verify=False)
        return response
        
    except Exception as e:
        print(str(e))
    
def get():
    pass
    

if __name__ == "__main__":
    response = post(sourcetype="httpevent", eventtype="hello world", fields={'metric_name':'test'})
    print(str(response.text))
    print(response)
