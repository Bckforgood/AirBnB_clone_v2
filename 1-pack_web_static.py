#!/usr/bin/python3

""" pack_web_static module """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ do_pack function
    Generates a .tgz archive from the contents of the 'web_static'
    folder into the folder 'versions'
    """

    m_date = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_path = "versions/web_static_{}.tgz".format(m_date)
    try:
        local('mkdir -p versions')
        local('tar -cvzf {} web_static'.format(file_path))
        return file_path
    except:
        return none
