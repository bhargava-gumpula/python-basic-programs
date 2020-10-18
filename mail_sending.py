import smtplib

# Before running this progam, you must go to the gmail manage account
# and in security section, enable less secure apps to log in to gmail account

GMAIL_USER = "bhargava.gumpula@gmail.com"
GMAIL_PASS = "Rubicks.23_GC"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_email(recipient, subject, text):
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(GMAIL_USER, GMAIL_PASS)

    header = 'To:' + recipient + '\n' + 'From: ' + GMAIL_USER
    header += '\n' + 'Subject:' + subject + '\n'
    msg = header + '\n' + text + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, recipient, msg)
    smtpserver.close()

send_email('gsuryacse7k@gmail.com', 'Hello', '''Hi bhagha bee, 
                                                  are you hear?''')
