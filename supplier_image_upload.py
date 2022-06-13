#! /usr/bin/env python3
import os
import requests

folder_path = "./foldername/"
img_files = []
url = "http://localhost/name/"

# Loop through files in 'directory'
for img in os.listdir(folder_path):
     if img == img[:-4] + "jpeg":
       path = folder_path + img
       with open(path,'rb') as opened:
         r = requests.post(url, files={'file':opened})
         print(r.status_code)
