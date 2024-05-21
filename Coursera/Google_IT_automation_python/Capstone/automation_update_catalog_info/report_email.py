#!/usr/bin/env python3
import reports
import emails
import os
from datetime import date

def generate_report_summary():
  summary = "<br/>"
  path = './supplier-data/descriptions/'
  for fruit_desc in os.listdir(path):
    with open(path+fruit_desc) as file:
      content = file.readlines()
      summary += "name: " + content[0] + "<br/>" + "weight: "+ content[1] + "<br/><br/>" 
  
  return summary

def main():
  pdf_path = "/tmp/processed.pdf"
  title = f"Processed Update on {date.today()}"
  summary = generate_report_summary()
  reports.generate_report(pdf_path, title, summary)
  # send out reports via python email module
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate(sender, receiver, subject, body, pdf_path)
  emails.send(message)

if __name__ == "__main__":
  main()