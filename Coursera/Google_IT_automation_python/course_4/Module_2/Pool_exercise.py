#!/usr/bin/env python3

import subprocess
import os
from multiprocessing import Pool
import multiprocessing 

# src = "/home/student/data/prod/"
# dir = next(os.walk(src))[1]


# def backup(dir):
#   dest = "/home/student/data/prod_backup/"            
#   subprocess.call(["rsync", "-arq", src+'/'+dir, dest])

# p = Pool(len(dir))
# p.map(backup, dir)



home_path = os.path.expanduser('~')

src = home_path + "/data/prod/"
dest = home_path + "/data/prod_backup/"

if __name__ == "__main__":
  pool = Pool(multiprocessing.cpu_count())
  pool.apply(subprocess.call, args=(["rsync", "-arq", src, dest],))
