import requests
from requests.structures import CaseInsensitiveDict

url = "http://192.168.1.200:8080/job/HiddenPicturesNew_UE4_26_SVN/build"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Basic YWRtaW46MTFiYmUxY2RhOTA4YmM2ZWM2YTczZjhhYzExNDM2YjE4ZQ=="
headers["Content-Type"] = "application/json"
headers["Content-Length"] = "0"


resp = requests.post(url, headers=headers)

print(resp.status_code)