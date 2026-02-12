#!/usr/bin/env python3
# 2 files log & csv
visualize data in csv
import re

dic1 = {}
dic2 = {}

with Open('syslog.log', "r") as file:
    lines = files.readlines()
    for line in lines:
        match = re.search(
            r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)
        code, error_msg, user = match.group(1), match.group(2), match.group(3)