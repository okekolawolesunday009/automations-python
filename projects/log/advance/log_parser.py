import re
import sys
import csv


#     2026-02-12T10:15:03Z [backend] ERROR: Connection timeout
# nginx[2213]: WARN client closed connection prematurely
# systemd: ALERT Service restarted too frequently
# kubelet[3321]: info Node pressure resolved
# panic: runtime error: invalid memory address
# [cache] FATAL worker crashed unexpectedly


LOG_PATTERN = re.compile(
    r"^(?:"
    r"(?P<date>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s+"
    r"\[(?P<service>[^\]]+)\]\s+" #[^\]]+) match every in the brackect (not) before the \]
    r"(?P<level>[A-Za-z]+):\s+"
    r"(?P<message>.*)"
    r"|"

    r"(?P<process>[A-Za-z]+)\[(?P<pid>\d+)\]:\s+"
    r"(?P<level2>[a-zA-Z]+)\s+"
    r"(?P<message2>.*)"
    r"|"

    r"(?P<process2>[A-Za-z_.+]+):\s+"
    r"(?P<level3>[a-zA-Z]+)\s+"
    r"(?P<message3>.*)"

    r"|"

    
    r"\[(?P<service2>[^\]]+)\]\s+" 
    r"(?P<level4>[A-Za-z]+)\s+"
    r"(?P<message4>.*)"
   
    r")$"           

)

def parse_line(line):
    match = LOG_PATTERN.search(line)
    if not match:
        return None

    d = match.groupdict()

    if d["date"]:
        return [d["date"], d["service"], "",  "", 
        d["level"].upper(),  d["message"]]
    if d["process"]:
        return ["", "", d["process"], d["pid"], 
        d["level2"].upper(), d["message2"]]
                 
    if d["process2"]:
        return ["", "", d["process2"],"",
        d["level3"].upper(),  d["message3"]]

    if d["service2"]:
        return ["", d["service2"], "", "",
         d["level4"].upper(), d["message4"]]

    return None

def export_to_csv():
    if len(sys.argv) < 3:
        print("Usage: python log_parser.py <logfile> <outputfile>")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f, open(sys.argv[2], "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["date", "service", "process", "pid", "level", "message"])
        
        for line in f:
            line = line.strip()
            if not line:
                continue
            parsed = parse_line(line)

            if parsed: 
                writer.writerow(parsed)
            else:
                writer.writerow(["", "", "","", "UNMATCHED", line])
    print(f"✅ Done! Saved to {sys.argv[2]}")
           


if __name__ == '__main__':
    export_to_csv()

    
