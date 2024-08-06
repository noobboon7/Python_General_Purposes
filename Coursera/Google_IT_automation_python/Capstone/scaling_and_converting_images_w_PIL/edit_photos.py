import os
from PIL import Image #, ImageOps

# img = Image.open("./images/ic_add_location_black_48dp")
# print(img.format, img.size) #downloaded images are TIFF (192, 192)

size = (128,128)
for image in os.listdir("./images"):

  # format file with extension
  file, extension = os.path.splitext(image)
  file = "ic_edit" + file[2:]
  output_file = file + ".jpeg"

  with Image.open(f'./__path__/{image}') as img:
    try:  
      img = img.convert("RGB")
      img = img.rotate(90)
      img.thumbnail(size)
      img.save(f'test_folder/{output_file}')
      # ImageOps.contain(img,size).save(f'test_folder/{output_file}')
    except Exception as e:
      print(f"Error processing {image}: {e}")
  