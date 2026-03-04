#!/bin/bash

echo "Updating system..."
sudo apt update

echo "Installing Git..."
sudo apt install -y git

echo "Configuring Git..."
git config --global user.name "okekolawolesunday009"
git config --global user.email "okekolawolesunday@gmail.com"
git config --global init.defaultBranch main

echo "Generating SSH key..."

if [ ! -f ~/.ssh/id_rsa ]; then
    ssh-keygen -t rsa -b 4096 -C "okekolawolesunday@gmail.com" -f ~/.ssh/id_rsa -N ""
    echo "SSH key generated."
else
    echo "SSH key already exists."
fi

echo "Starting SSH agent..."
eval "$(ssh-agent -s)"

echo "Adding SSH key to agent..."
ssh-add ~/.ssh/id_rsa

echo "Your public SSH key (copy this to GitHub/GitLab):"
cat ~/.ssh/id_rsa.pub

echo "Setup complete."