# send_email_or_text
Send an e-mail or text message from Python

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
 
