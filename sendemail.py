import sys
import smtplib

gmail_user = 'adcurtin@gmail.com'
p = open('.password', 'r')
gmail_pwd = p.read().strip()
FROM = gmail_user
TO = gmail_user
SUBJECT = 'Google Music diff script'
TEXT = sys.stdin.read()

# Prepare actual message
message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, TO, SUBJECT, TEXT)
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    # print 'successfully sent the mail'
except:
    print "failed to send mail"
