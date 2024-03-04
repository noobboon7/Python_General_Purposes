# format as per coursera for csv file is list of lists
hosts = [['workstation.local', "192.168.25.64"], ["webserver.cloud", "10.2.5.6"]]

with  open("host_info.csv", 'w') as f:
  writer = csv.writer(f)
  writer.writerows(hosts)
  
  