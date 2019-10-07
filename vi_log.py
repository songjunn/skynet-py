#!/usr/bin/env python
# coding: utf-8

import os,sys
import time 
import glob
import signal

log_path = "./log/"

def int_func(signo, sigstack):
    sys.exit()

signal.signal(signal.SIGINT, int_func)

files = glob.glob(log_path+"game-*")

log_file = sorted(files, key=lambda x:os.stat(x).st_mtime ,reverse= True)[0]
os.system("vi " + log_file)
