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

# Directory to store downloaded images
DIRECTORY = "/home/USER/WebComics"

# User credentials
USERNAME = 'example@sender-acct.com'
PASSWORD = 'YOUR_PASSWORD'

FROMADDR = USERNAME

# SMS recipients
SUBS = ['0123456789@example.exchange.net',]


def TimeStamp():
    return strftime('%-I:%M %p - %b %d %Y')


def xkcd_get():
    response = urllib2.urlopen('http://xkcd.com/')
    html = response.read()
    imgurl = re.findall(r'Image URL \(for hotlinking/embedding\): (.*?)\n', html)
    path, fileExtension = os.path.splitext(imgurl[0])
    filename = path.split('/')[-1]
    xkcdPath = DIRECTORY + "/xkcd/" + filename + fileExtension
    if not os.path.isfile(xkcdPath):
        urllib.urlretrieve(imgurl[0],
                           DIRECTORY + "/xkcd/" + filename + fileExtension)
        return xkcdPath
    else:
        print('xkcd aborted, file exists...')
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
    xkcd = xkcd_get()
    time = TimeStamp()
    message = 'Daily comics from: xkcd@webdev-server\n' + time
    if xkcd != 'file already exists':
        print('sending xkcd...')
        for toaddrs in SUBS:
            print('...to ' + toaddrs + '...')
            SendAttached(xkcd, message, toaddrs)

""" Make Function Calls """
get_lulz()
