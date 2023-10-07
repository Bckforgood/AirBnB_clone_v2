#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers
"""

from fabric.api import local, run, put, env
from datetime import datetime
import os

# Update these with your actual server IPs and SSH key file
env.hosts = ['<54.90.54.242>', '<54.227.200.179>']
env.key_filename = "school.pub"


def do_pack():
    """
    Generates a .tgz archive from web_static folder
    Returns:
        Archive path if successful, None otherwise
    """
    # Current date and time for the archive
    now = datetime.now()
    date_time = now.strftime('%Y%m%d%H%M%S')

    # Archive path
    archive_path = 'versions/web_static_{}.tgz'.format(date_time)

    # Create the archive using tar
    local('mkdir -p versions')
    result = local('tar -cvzf {} web_static'.format(archive_path))

    # Check if the archive was created successfully
    if result.succeeded:
        return archive_path
    else:
        return None


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


def deploy():
    """
    Creates and distributes an archive to web servers
    Returns:
        Result of do_deploy function
    """
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)

