import smtplib

GMAIL_USER = 'bhargava.gumpula@gmail.com'
GMAIL_PASS = 'Rubicks.23_GC'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def send_email(recipient, subject, text):
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(GMAIL_USER, GMAIL_PASS)

    header = 'To:' + recipent + '\n' + 'From: ' + GMAIL_USER
 
