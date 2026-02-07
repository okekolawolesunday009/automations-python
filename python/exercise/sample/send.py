import requests
from requests.auth import HTTPBasicAuth
import urllib3

# Disable SSL warnings for self-signed certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://helpdesk.g.group/WOListView.do"

response = requests.get(
    url,
    auth=HTTPBasicAuth("oke.kolawole", "ho@12341274"),
    verify=False
)

print("Status code:", response.status_code)

# Check if the server returned JSON
content_type = response.headers.get("Content-Type", "")
if "application/json" in content_type.lower():
    print(response.json())
else:
    print("Response is not JSON. Printing raw text:")
    print(response)
