import requests


def test():
    datalogger_ip = "192.168.4.219"
    rsp = requests.get(f"http://{datalogger_ip}/dlx/live")
    print(rsp.text)
    