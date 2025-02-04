# ✅ Handles SMTP email sending

from app.core.config_core import settings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.schema.email_schema import EmailRequest, EmailResponse
# from app.service.domain_validation_service import domain_validation_service


class EmailService:
    def __init__(self):
        self.server= None
    def setup_smtp(self): # internal authentication
        try:
            self.server = smtplib.SMTP("smtp.gmail.com", 587)
            self.server.starttls()  # establish secure the connection
            self.server.login(settings.MASTER_EMAIL_ID, settings.MASTER_EMAIL_PASSWORD)
            return EmailResponse(success=True, message="SMTP server setup successful.")
        except Exception as error:
            return EmailResponse(success=False, message=str(error))
        
    def close_smtp(self): # close the SMTP server connection.
        if self.server:
            self.server.quit()
            return EmailResponse(success=True, message="SMTP server connection closed.")
        else:
            return EmailResponse(success=False, message="No SMTP connection found.")
    def send_email(self, request: EmailRequest)->EmailResponse:
        if not self.server:
            return EmailResponse(success=False, message="SMTP server not set up.")
        try:                # create the email message
            alias = request.alias_email or "no-reply" # If alias is given, use it. otherwise, use the default email
            msg = MIMEMultipart()
            # msg["From"] = alias 
            msg["From"] = f"{alias} <{settings.MASTER_EMAIL_ALIAS}>"
            msg["To"] = request.receiver_email
            msg["Subject"] = request.subject
            msg.attach(MIMEText(request.body, "plain"))
            if request.reply_email: msg.add_header("Reply-To", request.reply_email)

            self.server.sendmail(settings.MASTER_EMAIL_ALIAS, request.receiver_email, msg.as_string()) # send the email
            return EmailResponse(success=True, message="Email sent successfully.")
        except Exception as error:
            return EmailResponse(success=False, message=str(error))
        

email_service = EmailService()      # creating global instance for email service
