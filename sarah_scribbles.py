# -*- coding: utf-8 -*-
import os
import urllib
import urllib2
import re
import smtplib

from time import strftime

# Send attached only
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# The directory you want the downloaded images saved
# e.g.  /home/user/directory
DIRECTORY = "/home/USER/WebComics"

# User credentials
USERNAME = 'example@sender-acct.com'
PASSWORD = 'YOUR_PASSWORD'

FROMADDR = USERNAME

# SMS recipients
SUBS = ['0123456789@example.exchange.net',]


def TimeStamp():
    return strftime('%b %d %Y')


def scribble_get():
    response = urllib2.urlopen('http://sarahcandersen.com/')
    html = response.read()
    findurl = re.findall(r'<img src="http://([0-9]{2}).media.tumblr.com/(.*?)" alt="">',
                         html)
    imgurl = ('%s%s%s%s' % ("http://", findurl[0][0],
                            ".media.tumblr.com/", findurl[0][1]))
    path, fileExtension = os.path.splitext(imgurl)
    filename = path.split('/')[-1]
    imagePath = DIRECTORY + "/sarah_scribbles/" + filename + fileExtension
    if not os.path.isfile(imagePath):
        urllib.urlretrieve(imgurl,
                           DIRECTORY + "/sarah_scribbles/" + filename + fileExtension)
        return imagePath
    else:
        print('Operation aborted, file exists...')
        return "file already exists"


def SendAttached(IMAGE, MESSAGE, TOADDRS):
    img_data = open(IMAGE, 'rb').read()
    msg = MIMEMultipart()

    text = MIMEText(MESSAGE)
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(IMAGE))
    msg.attach(image)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(USERNAME, PASSWORD)
    server.sendmail(FROMADDR, TOADDRS, msg.as_string())
    print('...success!')
    server.quit()


def get_lulz():
    scribble = scribble_get()
    time = TimeStamp()
    message = 'New scribble from: sarah_scribbles@your-server\n' + time
    if scribble != 'file already exists':
        print('sending scribble...')
        for toaddrs in SUBS:
            print('...to ' + toaddrs + '...')
            SendAttached(scribble, message, toaddrs)

""" Make Function Calls """

get_lulz()
