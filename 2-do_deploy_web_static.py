#!/usr/bin/python3
# Fabric script to distribute an archive to your web servers
import os
from fabric.api import env, run, put
from os.path import exists

env.hosts = ["54.198.60.71", "100.26.177.201"]
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        True if successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    filename = os.path.basename(archive_path)
    name = filename.split('.')[0]

    try:
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(filename, name))
        run('rm /tmp/{}'.format(filename))
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(name, name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(name))
        return True
    except Exception as e:
        return False
