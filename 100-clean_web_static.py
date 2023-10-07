#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives
"""

from fabric.api import run, local, env
from os.path import exists
from datetime import datetime

# Update these with your actual server IPs and SSH key file
env.hosts = ['<54.90.54.242>', '<54.227.200.179>']


def do_clean(number=0):
    """
    Deletes unnecessary archives based on the number specified
    Args:
        number: Number of archives to keep (default is 0)

    Returns:
        None
    """
    number = int(number)
    if number < 0:
        number = 0

    try:
        # Delete unnecessary archives in versions folder
        local('ls -1t versions/ | tail -n +{} | xargs -I {{}} rm versions/{{}}'
              .format(number + 1))

        # Delete unnecessary archives in /data/web_static/releases folder
        run('ls -1t /data/web_static/releases/ | tail -n +{} | '
            'xargs -I {{}} rm -rf /data/web_static/releases/{{}}'
            .format(number + 1))

    except Exception as e:
        print("Clean failed:", str(e))


if __name__ == "__main__":
    do_clean()

