#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers and deploy
"""

from fabric.api import run, put, env
from os.path import exists
import os

# Update these with your actual server IPs and SSH key file
env.hosts = ['<IP web-01>', '<IP web-02>']
env.key_filename = "<path to your SSH key file>"


def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys
    Args:
        archive_path: Path to the archive

    Returns:
        True if successful, False otherwise
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/
        put(archive_path, '/tmp/')

        # Extract archive to the appropriate folder
        archive_file = archive_path.split("/")[-1]
        archive_name = archive_file.split(".")[0]
        run('mkdir -p /data/web_static/releases/{}'.format(archive_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(archive_file, archive_name))

        # Delete the archive from the server
        run('rm /tmp/{}'.format(archive_file))

        # Move contents to appropriate location
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(archive_name, archive_name))

        # Clean up
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_name))

        # Update the symbolic link
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_name))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed:", str(e))
        return False
