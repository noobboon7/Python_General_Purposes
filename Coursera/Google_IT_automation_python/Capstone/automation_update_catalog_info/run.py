#!/usr/bin/env python3
import os
import requests 

"""json format 
{
  "name": "Watermelon", 
  "weight": 500, 
  "description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.", 
  "image_name": "010.jpeg"}
"""
path = "./supplier-data/descriptions/"
headers = ["name", "weight", "description"]

for file in os.listdir(path):
  fruit_dict = dict()
  with open(path+file) as txt:
    lines = txt.readlines()
    for i in range(len(headers)):
      fruit_dict.update({headers[i]: lines[i].strip('\n')})
      
    fruit_dict.update({"weight": int(fruit_dict["weight"].split()[0])})
    fruit_dict.update({"image_name": file.split(".")[0]+".jpeg"})

  response = requests.post("http://{external_ip}/fruits/", data=fruit_dict)
  response.raise_for_status()