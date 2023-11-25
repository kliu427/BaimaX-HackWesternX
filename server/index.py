import http.client
import json
from flask import Flask

conn = http.client.HTTPSConnection("e1dgm3.api.infobip.com")
payload = json.dumps({
    "messages": [
        {
            "destinations": [
                {
                    "to": "14168227911"
                }
            ],
            "from": "InfoSMS",
            "text": "This is a sample message"
        }
    ]
})
headers = {
    'Authorization': 'App 6bdfba0e981ac43975ce2e6935d76ff0-3b8c4435-bcea-49b9-b4ea-af30cf2e42d8',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
conn.request("POST", "/sms/2/text/advanced", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

@app.route("/api/incoming-sms", methods=["POST"])
def incoming_sms():
    message_results = SmsInboundMessageResult(
        message_count=request.json["message_count"],
        pending_message_count=request.json["pending_message_count"],
        results=request.json["results"]
    )
    
    for result in message_results.results:
        print("message text: {0}".format(result.clean_text))
    