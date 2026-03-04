#!/usr/bin/env python3
# 2 files log & csv
# visualize data in csv
import re
import sys
dic1 = {}
dic2 = {}


logFile = sys.argv[1]

with open(logFile, "r") as file:
    lines = file.readlines()
    for line in lines:
        match = re.search(
            r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)
        code, error_msg, user = match.group(1), match.group(2), match.group(3)

        print('code: ',code)
        print('error:', error_msg )
        print('user:', user)
file.close