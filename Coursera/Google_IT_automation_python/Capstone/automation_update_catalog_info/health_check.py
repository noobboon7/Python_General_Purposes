#!/usr/bin/env python3
import emails
import psutil
import shutil
import socket
import os
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "health checks:"
body = "Please check your system and resolve the issue as soon as possible."

def check_cpu_usage():
  cpu_usage = psutil.cpu_percent(interval=1)
  if cpu_usage > 80:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error(sender, receiver, subject, body)
    emails.send(message)

def check_disk_usage():
  disk_usage = shutil.disk_usage("/")
  percent_used = (disk_usage.used / disk_usage.total) * 100
  if percent_used > 80:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error(sender, receiver, subject, body)
    emails.send(message)
    

def check_memory_usage():
  memory_usage = psutil.virtual_memory()
  available_memory_mb = memory_usage.available / (1024*1024)
  if available_memory_mb < 100:
    subject = "Error - Available memory is less than 100MB"
    message = emails.generate_error(sender, receiver, subject, body)
    emails.send(message)

def check_localhost_resolution():
  try:
    localhost_ip = socket.gethostbyname('localhost')
    if localhost_ip != '127.0.0.1':
      subject = "Error - localhost cannot be resolved to 127.0.0.1"
      emails.send(message)
  except socket.gaierror as e:
      message = emails.generate_error(sender, receiver, subject, f"Failed to resolve localhost: {e}")
      emails.send(message)
    
def main():
  check_cpu_usage()
  check_disk_usage()
  check_memory_usage()
  check_localhost_resolution()

if __name__ == "__main__":
  main()