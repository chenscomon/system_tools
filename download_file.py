#!/usr/bin/env python

import requests

my_url = "https://www.nationalgeographic.com/content/dam/news/2017/05/26/orca_killer_whale/08_orca_killer_whale_gallery.jpg"

def download(url):
    get_res = requests.get(url)
    file_name = url.split('/')[-1]
    print("[+] File downloaded successfully!")
    print("[+] Creating a new file...")
    with open(file_name, "wb") as out_file:
        out_file.write(get_res.content)
    print("[+] File was created successfully: " + file_name)

print("[+] Starting to download the file...")
download(my_url)