from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import glob
import argparse

anaconda_path = "/mnt/d/Anaconda"
parser = argparse.ArgumentParser()
parser.add_argument("--set-global", type=int, choices=[2, 3, -1], default=0)
parser.add_argument("--show", action="store_true")

args = parser.parse_args()

all_pythons = glob.glob("{}/Anaconda*".format(anaconda_path))

if len(all_pythons) < 2:
    raise Exception("Error!")

versions = [os.path.basename(python) for python in all_pythons]
is_2 = any(map(lambda x: "2" in x, versions))
is_3 = any(map(lambda x: "3" in x, versions))
if is_2 and not is_3:
    cur_version = "3"
if is_3 and not is_2:
    cur_version = "2"
if is_2 and is_3:
    cur_version = ""

if args.show:
    if cur_version:
        print("Current version is Anaconda{}".format(cur_version))
    else:
        print("No Anaconda available!")

if args.set_global != 0 and args.set_global != -1:
    if cur_version:
        os.system("mv {}/Anaconda {}/Anaconda{}".format(anaconda_path, anaconda_path, cur_version))
    os.system("mv {}/Anaconda{} {}/Anaconda".format(anaconda_path, args.set_global, anaconda_path))

if args.set_global == -1:
    if cur_version:
        os.system("mv {}/Anaconda {}/Anaconda{}".format(anaconda_path, anaconda_path, cur_version))

