import http.client

conn = http.client.HTTPSConnection("e1dgm3.api.infobip.com")
payload = ''
headers = {
    'Authorization': 'App 6bdfba0e981ac43975ce2e6935d76ff0-3b8c4435-bcea-49b9-b4ea-af30cf2e42d8',
    'Accept': 'application/json'
}
conn.request("GET", "/sms/1/inbox/reports?limit=2&applicationId=default&entityId=default", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))