#!/usr/bin/python3

""" pack_web_static module """

from fabric.api import run, put, env, local
from datetime import datetime
import os

env.hosts = ['34.75.228.249', '35.231.205.149']


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
        return None


def do_deploy(archive_path):
    """ do_deploy function
    Distributes an archive to your web servers
    """
    if archive_path is None or os.path.isfile(archive_path) is False:
        return False

    try:
        a_name = archive_path.split('/')[-1]
        put('{}'.format(archive_path), '/tmp/{}'.format(a_name))
        name_target = a_name.split('.')[0]
        full_target = "/data/web_static/releases/{}".format(name_target)
        run('mkdir -p {}'.format(full_target))
        run("tar -xzf /tmp/{} -C {}".format(a_name, full_target))
        run('rm /tmp/{}'.format(a_name))
        run('mv {}/web_static/* {}/'.format(full_target, full_target))
        run('rm -Rf {}/web_static'.format(full_target))
        run('rm -Rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(full_target))
        return True
    except:
        return False


def deploy():
    """ full deploy function
    creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)


def do_clean(number=0):
    """ cleaning function
    deletes out-of-date archives
    """
    if number == 0 or number == 1:
        number = 1
    else:
        number = int(number)

    local("ls -1v versions/web* | head -n -{} | xargs rm -rf".format(number))
    run("ls -1v /data/web_static/releases/web* | head -n -{} | \
    xargs rm -rf".format(number))
