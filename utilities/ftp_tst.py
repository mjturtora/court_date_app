from ftplib import FTP
import email
import csv

import os

def read_auth():
    """
    Inputs authorization info from external file.
    :return:
    """
    with open('priv\\paramikossh.txt') as auth:
        auth_reader = csv.DictReader(auth)
        for row in auth_reader:
            if row['Variable'] == 'url':
                url = row['Value']
            elif row['Variable'] == 'account_id':
                account_id = row['Value']
            else:
                passwd = row['Value']
    return url, account_id, passwd

url, account_id, passwd = read_auth()
print 'url, account_id, passwd  =', url, account_id, passwd

ftp = FTP(url)   # connect to host, default port
ftp.login(account_id, passwd)   # user anonymous, passwd anonymous@
ftp.cwd("mail/whenismycourtdate.com/data/cur/")

"""
try:
    os.remove('priv\\test.txt')
except OSError:
    pass

try:
    os.remove('priv\\attachment.txt')
except OSError:
    pass
"""

with open('priv\\test.txt', 'w') as f:
    print 'opened test.txt'

    def write_to_file(line):
        f.write('%s\n' % line)
        #f.write(line)

    #ftp.dir()
    #ftp.retrlines('LIST')     # list directory contents

    ftp.retrlines('RETR 1469701987.H711106P24423.box1182.bluehost.com,S=12725499:2,Sab',
                      write_to_file)

#print len(email)
ftp.quit()

msg = email.message_from_file(open('priv\\test.txt'))
#print "msg = ", msg
print "len = ", len(msg.get_payload())
attachment = msg.get_payload()[2]
print attachment.get_content_type()
open('priv\\attachment.txt', 'w').write(attachment.get_payload(decode=True))

