import csv

f = open("csv_file.py")
csv_f = csv.reader(f)

for row in csv_f:
  r_name,  r_age, r_gender = row
  print(f"Name: {r_name}, Age: {r_age}, Gender: {r_gender}")
