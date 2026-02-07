#!/usr/bin/env python3

import shutil
import psutil
import socket
import time
from emails import generate_email, send_email

# -------------------------------
# Health check helper functions
# -------------------------------

def check_cpu_usage():
    """Return True if CPU usage is over 80%"""
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage > 80

def check_disk_space():
    """Return True if disk space is less than 20%"""
    du = shutil.disk_usage("/")
    free_percent = (du.free / du.total) * 100
    return free_percent < 20

def check_memory():
    """Return True if available memory is less than 100MB"""
    available_memory = psutil.virtual_memory().available / (1024 * 1024)
    return available_memory < 100

def check_localhost():
    """Return True if localhost does NOT resolve to 127.0.0.1"""
    try:
        localhost_ip = socket.gethostbyname("localhost")
        return localhost_ip != "127.0.0.1"
    except:
        return True

# -------------------------------
# Main loop
# -------------------------------

def main():
    while True:
        error_message = None

        if check_cpu_usage():
            error_message = "Error - Rea-bible CPU usage is over 80%"

        elif check_disk_space():
            error_message = "Error - Rea-bible Available disk space is less than 20%"

        elif check_memory():
            error_message = "Error - Rea-bible  Available memory is less than 100MB"

        elif check_localhost():
            error_message = "Error - Rea-bible localhost cannot be resolved to 127.0.0.1"

        if error_message:
            subject = error_message
            body = "Please check your system and resolve the issue as soon as possible."

            # Using the emails.py generate_email() (without attachments)
            message = generate_email(
                sender="automation@example.com",
                recipient="student@example.com",
                subject=subject,
                body=body
            )

            send_email(message)

        time.sleep(60)  # Check again every 60 seconds

if __name__ == "__main__":
    main()

