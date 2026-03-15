from fastapi import FastAPI, Request
from app.logger import log_message
from app.task import send_email
import re
app = FastAPI(title="Messaging App")

@app.get("/")
async def root(request: Request):
    query_params = request.query_params

    if "talktome" in query_params:
        message = "Someone accessed the talktome enpoint"
        log_message(message)

        return {
            "status": "success",
            "action": "logged",
            "message": message
        }
    sendmail = query_params.get("sendmail")
    pattern = r"^[a-zA-Z._%+]+([a-z0-9.]+)?@[a-zA-Z0-9]+\.[a-z]{2,}$"
    #?sendmail=mailto:test@example.com"
    email = sendmail.split("mailto:")[-1] if sendmail else None

    if sendmail and re.match(pattern, email):
        email_message = f"Email sent with message: {sendmail}"
        send_email(sendmail)    

        return {
            "status": "success",
            "action": "logged",
            "message": "task queued"
        }
    return {
        "status": "error",
        "message": "Use ?talktome or ?sendmail=mailto:test@example.com"
    }