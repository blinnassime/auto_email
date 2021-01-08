#_*_ coding: utf-8 _*_#
import os

import smtplib
import email, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formataddr
from email import encoders
from email.mime.base import MIMEBase

from datetime import datetime

def sendemail(sender_name, sender_email, sender_passwd, recipient, subject,
messages):    
    message = MIMEMultipart()
    
    message["From"] = formataddr((sender_name, sender_email))
    message["To"] = recipient
    message["Subject"] = subject
    
    # Add body to email
    message.attach(MIMEText(messages, "html"))
    
    #with open("salesreport/daily_sales_report.pdf", "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        #part = MIMEBase("application", "octet-stream")
        #part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    #encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    #part.add_header(
    #    "Content-Disposition",
    #    f"attachment; filename=daily_sales_report.pdf",
    #)
    
    #message.attach(part)
    text = "bravo"#message.as_string()

    # Log in to server using secure context and send email
    server = smtplib.SMTP('192.168.0.8', 25)
    server.starttls()
    server.login(sender_email, sender_passwd)
    server.sendmail(sender_email, recipient , text)
    server.quit()

if __name__ == '__main__':
    now = datetime.now().strftime("%Y-%m-%d")
    
    sender_name = 'Daily Sales Report'
    sender_email = 'reportcentre@testing.com'
    sender_passwd = 'XXXXXXXX'
    recipient = 'blin.nassime@gmx.fr'
    subject = 'Daily Sales Report - ' + str(now)
    
    messages = '<p>Hi Manager</p><p>Attached is the daily sales report.</p>\
    <span>***This is an automatically generated email, please do not reply to this message.***</span></p>'
    
    try:
        sendemail(sender_name, sender_email, sender_passwd, recipient,
subject, messages)
    except:
        print('eMail could not be sent')
