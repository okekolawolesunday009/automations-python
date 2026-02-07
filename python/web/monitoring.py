#!/usr/bin/env python3

import shutil
import psutil
import socket
import subprocess
import time
from emails import generate_email, send_email

# -------------------------------
# Health check helper functions
# -------------------------------

def check_cpu_usage():
    """Return True if CPU usage is over 80%"""
    return psutil.cpu_percent(1) > 80


def check_disk_space():
    """Return True if free disk space is less than 20%"""
    du = shutil.disk_usage("/")
    free_percent = du.free / du.total * 100
    return free_percent < 20


def check_memory():
    """Return True if available memory is less than 100MB"""
    available_mb = psutil.virtual_memory().available / (1024 * 1024)
    return available_mb < 100


def check_localhost():
    """Return True if localhost cannot resolve to 127.0.0.1"""
    try:
        return socket.gethostbyname("localhost") != "127.0.0.1"
    except:
        return True


def check_pm2_app(app_name="my-app"):
    """
    Returns True if the PM2 app is NOT running.
    You can change app_name to match your PM2 application name.
    """
    try:
        result = subprocess.run(
            ["pm2", "status", app_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # PM2 prints "online" if the app is healthy
        if "online" in result.stdout.lower():
            return False  # healthy

        return True  # not online or in error state

    except FileNotFoundError:
        # PM2 is not installed or not in PATH
        return True


# -------------------------------
# Main loop
# -------------------------------
def main():
    while True:
        error_message = None

        if check_cpu_usage():
            error_message = "Error - CPU usage is over 80%"

        elif check_disk_space():
            error_message = "Error - Available disk space is less than 20%"

        elif check_memory():
            error_message = "Error - Available memory is less than 100MB"

        elif check_localhost():
            error_message = "Error - localhost cannot be resolved to 127.0.0.1"

        elif check_pm2_app("my-app"):  # 🔥 change "my-app" to your PM2 process name
            error_message = "Error - PM2 application is not running"

        if error_message:
            subject = error_message
            body = "Please check your system and resolve the issue as soon as possible."

            message = generate_email(
                sender="automation@example.com",
                recipient="student@example.com",
                subject=subject,
                body=body
            )
            send_email(message)

        time.sleep(60)


if __name__ == "__main__":
    main()
