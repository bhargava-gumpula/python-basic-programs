import smtplib

GMAIL_USER = "bhargava.gumpula@gmail.com"
GMAIL_PASS = "Rubicks.23_GC"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def send_email(recipient, subject, text):
    smtpserver = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.login(GMAIL_USER, GMAIL_PASS)

    header = 'To:' + recipient + '\n' + 'From: ' + GMAIL_USER
    header += '\n' + 'Subject:' + subject + '\n'
    msg = header + '\n' + text + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, recipient, msg)
    smtpserver.close()

send_email('bhargava_gumpula@gmail.com', 'Hello', '''Hi bhagha bee, 
                                                  are you hear?''')
