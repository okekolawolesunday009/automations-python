#!/usr/bin/env bash
set -euo pipefail

INPUT_FILE="users.txt"                  # <-- your file with: user;group1,group2
LOG_FILE="/var/log/user_create.log"     # <-- log output file


echo "user creation $(date)" | tee -a "$LOG_FILE"

logger() {
  local level="$1"; shift
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] [$level] $*" | tee -a "$LOG_FILE"
}

trap 'logger ERROR "Script failed on line $LINENO"' ERR

while IFS=';' read -r username groups; do
  # skip empty lines / comments
  [[ -z "${username// }" ]] && continue
  [[ "$username" =~ ^[[:space:]]*# ]] && continue

  # trim spaces
  username="$(echo "$username" | xargs)"
  groups="${groups:-}"
  groups="$(echo "$groups" | tr -d ' ')"   # remove spaces inside group list

  if id "$username" &>/dev/null; then
    logger INFO "User '$username' already exists"
  else
    # Create user + home directory
    sudo useradd -m -s /bin/bash "$username"
    logger INFO "✅ Created user '$username'"

    # Generate password and set it
    password="$(tr -dc 'A-Za-z0-9!?%=' < /dev/urandom | head -c 12)"
    echo "$username:$password" | sudo chpasswd >/dev/null
    logger INFO "✅ Password set for '$username'"

    # OPTIONAL: force password change on first login
    sudo chage -d 0 "$username" >/dev/null
    logger INFO "✅ Forced password reset on first login for '$username'"
  fi

  # Create groups + add user to them (if provided)
  if [[ -n "$groups" ]]; then
    for grp in $(echo "$groups" | tr ',' ' '); do
      sudo groupadd -f "$grp"
      logger INFO "✅ Ensured group '$grp' exists"
    done

    sudo usermod -aG "$groups" "$username"
    logger INFO "✅ Added '$username' to groups: $groups"
  fi

  # Ensure home ownership is correct (extra safety)
  if [[ -d "/home/$username" ]]; then
    sudo chown -R "$username:$username" "/home/$username"
    logger INFO "✅ Set ownership for /home/$username"
  fi

done < "$INPUT_FILE"

logger INFO "Done."