from cvprac import cvp_client as cvp_client
import requests
import os


from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp1 = '192.168.0.5'

username = 'arista'
password = 'aristahrqo'

client = cvp_client.CvpClient()

client.connect([cvp1], username, password)

tasks = client.api.get_tasks_by_status('Pending')

for task in tasks:
    taskId = task['workOrderId']
    hostname = task['workOrderDetails']['netElementHostName']
    print(f"{taskId} for {hostname}")
    client.api.execute_task(taskId)