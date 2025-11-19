from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello, world!"

@app.route("/watsapp", methods=['POST'])
def sms_reply():
    """"Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # create reply
    resp = MessagingResponse()
    resp.message("good moring")

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

