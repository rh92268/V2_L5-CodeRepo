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

directory = 'configs'

exist = os.path.exists(directory)
if not exist:
    os.makedirs(directory)

configlets = client.api.get_configlets(start=0,end=0)

for item in configlets['data']:
    file = open(directory+'/'+item['name']+'.txt','w')
    file.write(item['config'])
    file.close()

