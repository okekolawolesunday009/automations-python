
import re
import sys

LOG_PATTERN = re.compile(
    r"^(?:"
    r"(?:(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+)?"
    r"(?:\[(.*?)\]\s+)?"
    r"([a-zA-Z]+)\s+"
    r"(.*)"
    r")$"

)

def intermediate():
    with open(sys.argv[1], 'r') as f:
        
        for line in f:
            line = line.strip()
            match = LOG_PATTERN.search(line)
            if not match:
                print("No match:", line)
                continue
            date, time, service, level, message = match.groups()
            print("date:   ", date)
            print("time:   ", time)
            print("service:", service)
            print("level:  ", level)
            print("message:", message)
            print("-" * 40)



if __name__ == '__main__':
    intermediate()

    
