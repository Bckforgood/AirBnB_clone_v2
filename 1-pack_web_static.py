#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from web_static folder
"""

from fabric.api import local
from datetime import datetime
import os

# Ensure directory for archives exists
if not os.path.exists('versions'):
    os.makedirs('versions')


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
    result = local('tar -cvzf {} web_static'.format(archive_path))

    # Check if the archive was created successfully
    if result.succeeded:
        return archive_path
    else:
        return None
