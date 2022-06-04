# This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import smtplib


class NotificationManager:
    def __init__(self):
        self.twilio_sid = "AC5ed109293f12d6a3fcbab5684c39dcf5"  # Hide it in environment variables
        self.twilio_auth_token = "120909407da5a14a25639525ebc40fe2"  # Hide it in environment variables
        self.client = Client(self.twilio_sid, self.twilio_auth_token)
        self.message = ''
        self.from_email = "smtptrial22@gmail.com"  # Hide it in environment variables
        self.password = "smgmail1995"  # Hide it in environment variables
        self.smtp_server = "smtp.gmail.com"

    def sms(self, sms):
        self.message = self.client.messages \
            .create(
            body=sms,
            from_='+19706717349',
            to='+917989532395'
        )   # Hide "from" number in environment variables
        print(self.message.status)

    def send_mail(self, customer_mails, msg, google_link):
        with smtplib.SMTP(self.smtp_server, 587) as connection:
            connection.starttls()
            connection.login(user=self.from_email, password=self.password)
            for email in customer_mails:
                connection.sendmail(from_addr=self.from_email,
                                    to_addrs=email,
                                    msg=f"Subject:New Low Price Flight!\n\n{msg}\n{google_link}".encode('utf-8'))
