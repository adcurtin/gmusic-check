import sys
import smtplib
import argparse

parser = argparse.ArgumentParser(description='send an email')
parser.add_argument('grep_retval', type=int,
                    help='return value of grep on the diff')

args = parser.parse_args()

gmail_user = 'adcurtin@gmail.com'
p = open('.password', 'r')
gmail_pwd = p.read().strip()
FROM = gmail_user
TO = gmail_user
SUBJECT = 'Google Music diff script'

if (args.grep_retval == 0):  # found the grep string!
    SUBJECT = 'SONG REMOVED! Google Music diff script'
    TEXT = "A SONG HAS BEEN REMOVED (>) FROM THE LIBRARY\n"
    TEXT += sys.stdin.read()
else:
    TEXT = sys.stdin.read()

# Prepare actual message
message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, TO, SUBJECT, TEXT)
try:
    # print message
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    # print 'successfully sent the mail'
except:
    print "failed to send mail"
