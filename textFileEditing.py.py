import base64
import os
import glob
from sys import platform

files = glob.glob("files/*", recursive=True)
for file in files:
    fp = open(file, "r+")
    lines = fp.readlines()
    first = lines[:-7]
    last = lines[-7:-2]
    url = lines[-2]
    fp.writelines(first)
    fp.writelines("cv_start-"+url[:-1]+"-cv_stop\n")
    fp.writelines("detail_start--detail_stop\n")
    fp.writelines(last)
    fp.writelines("\n")
    fp.close
