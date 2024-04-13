#!/usr/bin/env python3
import csv
import datetime
import requests
from collections import OrderedDict

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
  """Interactively get the start date to query for."""

  print()
  print('Getting the first start date to query for.')
  print()
  print('The date must be greater than Jan 1st, 2018')
  year =int(input('Enter a value for the year: '))
  month = int(input('Enter a value for the month: '))
  day = int(input('Enter a value for the day: '))
  print()

  return datetime.datetime(year, month, day)

def get_file_lines(url):
  """Returns the lines contained in the file at the given URL"""

  # Download the file over the internet
  response = requests.get(url, stream=True)
  lines = []

  for line in response.iter_lines():
    lines.append(line.decode("UTF-8"))
  return lines


def get_same_or_newer(start_date):
  """Returns the employees that started on the given date, or the closest one."""
  data = get_file_lines(FILE_URL)
  reader = csv.reader(data[1:])
  employee_dict = OrderedDict()
  
  for row in reader:
    row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
    if row_date not in employee_dict:
      employee_dict[row_date] = [f'{row[0]} {row[1]}']
    else:
      employee_dict[row_date].append(f'{row[0]} {row[1]}')
  
  return employee_dict
  # return min_date, min_date_employees

def list_newer(start_date):
  employee_start_dates = get_same_or_newer(start_date)
  for employee_start_date, employees in employee_start_dates.items():
    if employee_start_date >= start_date:
      print("Started on {}: {}".format(employee_start_date.strftime("%b %d, %Y"), employees))

  # while start_date < datetime.datetime.today():
  #   start_date, employees = get_same_or_newer(start_date)
  #   print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))

    # Now move the date to the next one
    # start_date = start_date + datetime.timedelta(days=1)

def main():
  start_date = get_start_date()
  list_newer(start_date)

if __name__ == "__main__":
  main()
