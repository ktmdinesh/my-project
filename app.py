from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
import openai

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello, world!"

@app.route("/watsapp", methods=['POST'])
def sms_reply():
    # Get the incoming WhatsApp message
    msg = request.form.get('Body')
    
    # Prepare Twilio response
    resp = MessagingResponse()

    # Check if OpenAI key is set
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    if openai.api_key:
        # Generate AI response
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":msg}]
        )
        answer = completion.choices[0].message.content
        resp.message(answer)
    else:
        # If no OpenAI key, just echo the message
        resp.message(f"You said: {msg}")
    
    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
