#!/usr/bin/env python3

from PIL import Image
import os

# Origin folder 
folder_path = "./supplier-data/images/"

# Loop through the  directory for images
for image in os.listdir(folder_path):

# Use try/catch block to catch any images that cannot be converted
  try:
       im = Image.open(folder_path + image)
      # Save corrected img to a new variable and convert to 'RGB' format 
       new_im = im.resize((600,400)).convert('RGB')
       # Save the corrected image to the same origin folder
       img = image.split(".")
       new_im.save(folder_path + img[0] + ".jpeg")
       print("Print" + folder_path + img[0] +".jpeg")
        
  except OSError:
       print("cannot create jpg for",image)
