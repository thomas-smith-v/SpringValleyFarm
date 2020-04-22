from src import splunk_api

def post_sensor_metric(name: str, value=None):
    if value:
        fields = {'metric_name':name, name:value}
    else:
        fields = {'metric_name':name}
    
    return splunk_api.post(sourcetype="sensor_info", eventtype="metric", fields=fields)

def post_system_metric(name: str, value=None):
    if value:
        fields = {'metric_name':name, name:value}
    else:
        fields = {'metric_name':name}
    return splunk_api.post(sourcetype="system_info", eventtype="metric", fields=fields)