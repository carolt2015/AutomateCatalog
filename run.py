#! /usr/bin/env python3
import os
import requests

text_files =[]
folder_path = "./foldername/"

# Loop through files in 'directory'
for text in os.listdir(folder_path):
    text_files.append(folder_path + text)

# Loop through files & store in dictionary
for file in text_files:
   lines = []
   with open(file) as file_open:
      for line in file_open:
         lines.append(line.strip())
   img_name = file.split("/")
   im_name = img_name[3][:3] + ".jpeg"
   wt=(lines[1].split(" ")) 
   fruits = {"name":lines[0],"weight":wt[0],"description":lines[2],"image_name":im_name}

   url = http://[linux-instance-external-IP]/fruits/
   response = requests.post(url,json=fruits)

   if not response.ok:
      raise Exception("POST failed with status code {}".format(response.status_code)) 
