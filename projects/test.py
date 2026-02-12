import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# session = requests.Session()

# # 1️⃣ Login first
# login_url = "https://helpdesk.g.group/WOListView.do"   # replace with real login URL
# login_payload = {
#     "username": "ithelpdesk.ho",
#     "password": "oh.12341234"
# }

# login_resp = session.post(login_url, data=login_payload)

# print("Login status:", login_resp.status_code)

# 2️⃣ Now POST to WorkOrder
# wo_url = "https://helpdesk.g.group/WorkOrder.do?woMode=viewWO&woID=146164"

# wo_payload = {
#     "action": "update",
#     "status": "Resolved",
#     "comment": "Resolved via automation script"
# }

# resp = session.post(wo_url, data=wo_payload)

# print("WorkOrder POST status:", resp.status_code)
# print(resp.text)


url = "https://helpdesk.g.group/WOListView.do"

resp = requests.get(url, verify=False)

print(resp.status_code)
print(resp.text)