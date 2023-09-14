#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Create a compressed archive from the web_static folder.
    Returns:
        (str): Path to the created archive, or None if archiving fails.
    """
    try:
        # Create the versions folder if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Generate archive filename using the current date and time
        now = datetime.now()
        archive_name = "web_static_{}.tgz".format(
            now.strftime("%Y%m%d%H%M%S"))

        # Compress the web_static folder into the archive
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the path to the created archive
        return "versions/{}".format(archive_name)
    except Exception:
        return None
