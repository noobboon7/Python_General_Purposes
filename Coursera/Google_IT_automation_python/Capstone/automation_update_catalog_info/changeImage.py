#!/usr/bin/env python3
import os
from PIL import Image 

size = (600,400)
img_path = "./supplier-data/images/"
for image in os.listdir(img_path):
  try:
    with Image.open(img_path+image) as img:
      if img.mode != "RGB":
        img = img.convert("RGB")
      cropped_image = img.resize(size)
      output_file = os.path.join(img_path, os.path.splitext(image)[0] + ".jpeg")
      cropped_image.save(output_file, "JPEG", optimize=True)
  except Exception as e:
      print(f"Error processing {image}: {e}")
