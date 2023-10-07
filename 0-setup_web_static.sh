#!/usr/bin/env bash
# This script sets up the web servers for the deployment of web_static

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories and symbolic link
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "<html> <head> </head> <body> Holberton School </body> </html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config="\nlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n"
sudo sed -i "/^\tserver_name/ a $config" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
exit 0
