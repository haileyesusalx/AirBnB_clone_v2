#!/usr/bin/python3
# Fabric script to delete out-of-date archives
from fabric.api import env, run, local, lcd
import os

env.hosts = ["54.198.60.71", "100.26.177.201"]  # Replace with your server IPs
env.user = 'ubuntu'  # Replace with your SSH username


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep. Defaults to 0.
    """
    try:
        number = int(number)
    except ValueError:
        return

    if number < 0:
        return

    with lcd('versions'):
        local('ls -1t | tail -n +{} | xargs -I {{}} rm {{}}'.format(number + 1))

    with cd('/data/web_static/releases'):
        run('ls -1t | tail -n +{} | xargs -I {{}} rm -rf {{}}'.format(number + 1))
