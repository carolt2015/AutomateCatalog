#!/usr/bin/env python3
import emails
import os
import shutil
import psutil
import time


def main(argv):
 subject = ""
 sender = "sender@example.com"
 recipient = "recipient@example.com"
 
 try: 
   while True:
     usage = psutil.cpu_percent(1)
     if usage > 80:
       subject = "Error-CPU usage is over 80%"
       emails.generate_error_report(subject,sender,recipient)
       message =  emails.send_email(message)
    
     disk_usage = shutil.disk_usage('/')
     free = disk_usage.free / disk_usage.total * 100
     if free < 20:
       subject = "Error-Available disk space is less than 20%"
       emails.generate_error_report(subject,sender,recipient)
       message =  emails.send_email(message)

    
    memory_usage = psutil.virtual_memory()
    available_memory = memory_usage.available
    if available_memory < 500000000:
      subject = "Error - Available memory is less than 500MB"
      emails.generate_error_report(subject,sender,recipient)
      message =  emails.send_email(message)
    
    """ gives the list of users who are connected on the system """
    user = psutil.users()
    if user[0].host == "localhost":
      subject = "Error - localhost cannot be resolved to 127.0.0.1"
      emails.generate_error_report(subject,sender,recipient)
      message =  emails.send_email(message)
    
    time.sleep(60)
    
 except Exception as e:
     print(str(e))

if __name__ == "__main__":
  main(sys.argv) 
  
