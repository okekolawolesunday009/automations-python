#!/usr/bin/env bash
set -euo pipefail  #for strict failing
IFS=$'\n\t'

LOG_FILE="bootstrap.log"

echo "Bootstrap started at $(date)" > "$LOG_FILE" #creates a log file with the current date and time

logger() {
    local level="$1"; shift #removes the first arguments and leavs the rest in $*
    echo "[$(date "+%Y-%m-%d %H:%M:%S")] [$level] $*" | tee -a "$LOG_FILE"
}


trap 'log ERROR "Script failed on line $LINENO"' ERR #logs out this error to output

is_installed() {
    command -v "$1" &>/dev/null
}

install_docker() {
    if is_installed docker; then 
        logger INFO "Docker already installed"
    # ADD docker installation setup here
    else
        logger ERROR "Docker is not installed. Please install Docker and try again."
        exit 1
    fi
}


main() {
    logger INFO "Starting bootstarp....🎯🎯"
    install_docker
    logger INFO "Devops-new bee Docker (check file for docker error)"
    logger INFO "Bootstrap completed successfully! 🚀🚀"
}

main "$@"