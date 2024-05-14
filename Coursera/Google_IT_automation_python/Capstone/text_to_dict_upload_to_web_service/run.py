#! /usr/bin/env python3

import os
import requests

path = "./feedback"
headers = ["title", "name", "date", "feedback"]

for feedback in os.listdir(path):
  feedback_dict = dict()
  
  with open(path+"/"+feedback) as file:
    lines = file.readlines()
    for i in range(len(lines)):
      feedback_dict.update({headers[i]:lines[i].strip("\n")})
      
  response = requests.post("http://35.229.96.7/feedback/", json=feedback_dict)
  response.raise_for_status()
  # if not response.ok:
  #   raise Exception("GET failed with status code {}".format(response.status_code))

    

