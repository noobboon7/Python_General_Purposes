#!/usr/bin/env python3
import os
import requests

url = "http://{external_ip}/upload/" #replace localhost with provided external ip
img_path = "./supplier-data/images/"
for image in os.listdir(img_path):
  if image.endswith(".jpeg"):
    with open(img_path+image, "rb") as opened:
      r = requests.post(url, files={"file": opened})
      r.raise_for_status()
      