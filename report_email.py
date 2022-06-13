#!/usr/bin/env python3
import os
import reports
import emails
import datetime
import sys

def process_data(folder_path):
  report_sum = ""
  text_files = []
  # Loop through files in 'directory'
  for text in os.listdir(folder_path):
    text_files.append(folder_path + text)

  # Loop through text files & store in dictionary
  for file in text_files:
    lines = []
    with open(file) as file_open:
      for line in file_open:
        lines.append(line.strip())
   
    report_sum += "<br/>" "name: " + lines[0] + "<br/>" + "weight: " + lines[1] + "<br/>"
  return report_sum
  

def main(argv):
  folder_path = "./foldername/"
  report_summary = process_data(folder_path)
  
  """ Extracting todays date for report """
  x = datetime.datetime.now()
  today = x.strftime("%B %d, %Y")
  title = "Processed Update on "  + today
  reports.generate_report("/tmp/processed.pdf",title,report_summary) 

  # send the PDF report as an email attachment
  sender = "sender@example.com"
  recipient = "recipient@example.com"
  subject ="Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to the mail.
  attachment = "/tmp/processed.pdf"
  message = emails.generate_email(sender,recipient,subject,body,attachment)
  emails.send_email(message)

if __name__ == "__main__":
  main(sys.argv) 
  
