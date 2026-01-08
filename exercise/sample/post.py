import requests

url = "https://example.com/submit"

# Your cookies from browser
cookies = {
    "sessionid": "abc123",
    "csrftoken": "XYZ456",
}

# Your POST data
payload = {
    "name": "John",
    "role": "admin"
}

response = requests.post(url, data=payload, cookies=cookies, verify=False)  # verify=False for self-signed SSL

print("Status code:", response.status_code)
print("Response:", response.text)
