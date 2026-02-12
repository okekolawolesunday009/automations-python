#!/bin/bash


for logfile in /var/log/*.log; do
    echo "Processing $logfile..."
    cut -d' ' -f5- "$logfile" | sort | unique -c | sort -nr | head -5 # Extract the message part, count occurrences, sort by frequency, and show top 5
done

# cut -d',' -f1 users.csv 
#👉 Gets the first column (e.g., usernames)

# cut -d':' -f1 /etc/passwd
# 👉 Lists all system usernames

# cut -d',' -f1,3 users.csv
# 👉 Gets column 1 and 3

# cut -d':' -f1-3 /etc/passwd

# awk -F',' '{print $1}' users.csv using f as delimiter, print column 1
# awk '/ERROR/ {print $1, $2, $NF}' app.log (print first, second, and last fields of lines containing "ERROR")

grep 'jane' file get all file that has jane in it (janes get printed out   )
grep ' jane ' file that has only jane as a word