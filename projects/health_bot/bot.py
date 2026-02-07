#!/usr/bin/env python3

import subprocess
import logging
from pathlib import Path
import argparse

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'

)
logger = logging.getLogger(__name__)


def check_disk_space(threshold=80):
    """comment"""
    result  = subprocess.run(
        ['df', '-h', '/'],
        capture_output=True,
        text=True,
        check=True
        )
    logger.info(f"Disk Usage: {result.stdout}% used")
    lines = result.stdout.strip().split('\n')

def check_service(service_name):
    """comment"""
    try: 
        result = subprocess.run(
            ['systemctl', 'is-active', service_name],
            capture_output=True,
            text=True,
            check=True
        )
        logger.info(f"✅ Service {service_name} is RUNNING")
        return True
    except subprocess.CalledProcessError:
        logger.error(f"❌ Service {service_name} is DOWN")
        return False

def main():
    parser = argparse.ArgumentParser(description="Health Bot for System Monitoring")
    parser.add_argument(
        '--services',
        nargs='+',
        default=['nginx', 'mysql'],
        help='List of services to monitor'
    )
    parser.add_argument(
        '--disk_threshold',
        action='store_true',
        help='Check disk space usage'
    )
    arg = parser.parse_args()

    if arg.disk_threshold:
        check_disk_space()      
    if arg.services:
        for service in arg.services:
            check_service(service)  

if __name__ == "__main__":
    main()