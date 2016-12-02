"""
Use this function to send an e-mail or text from Python.

You must fill in:
 -a list of recipients (EMAIL_LIST)
 -EMAIL_SENDER - address of email sending message from
 -EMAIL_PASSWORD - the password for the sender address
 -SMTP_SERVER - currently configured for gmail, check your email address provider
 
To send a text message simply enter a string as a recipient with
the phone number followed by @provider.com where provider.com is 
from the list below based on the cell service provider of the recipient.

AT&T: number@txt.att.net
T-Mobile: number@tmomail.net
Verizon: number@vtext.com
Sprint: number@messaging.sprintpcs.com or number@pm.sprint.com
Virgin Mobile: number@vmobl.com

For example to send a text to someone with the number 123-456-7890 who uses Verizon,
enter the address as "1234567890@vtext.com".
 
"""

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys

EMAIL_LIST = [""] #ENTER EMAIL ADDRESS(S) AS STRINGS, ie. test@test.com
EMAIL_SENDER = "" #ENTER SENDER EMAIL ADDRESS 
EMAIL_PASSWORD = "" #ENTER SENDER EMAIL PASSWORD
SMTP_SERVER = "smtp.gmail.com:587" #Configured for GMail Sender



def send_message(subject, sender_name, message):
    '''(string, string, string) -> None
    
    Takes strings, sends e-mail.
    '''
    recipients = EMAIL_LIST
    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender_name
     
    part = MIMEText(message)
    msg.attach(part)  
    
    server = smtplib.SMTP(SMTP_SERVER)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
     
    server.sendmail(msg['From'], emaillist , msg.as_string())

send_message("Test Subject", "From Sender", "My Message!")
print "Success"
