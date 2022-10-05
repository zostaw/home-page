"""
Management tool for the home-page deployment.


Usage:
home-page.py make
home-page.py start

Dependencies:
---

"""

from ast import Raise
from genericpath import isfile
import os, sys, subprocess
from psutil import process_iter
from signal import SIGTERM  # or SIGKILL
from subprocess import Popen
import re


class HomePage:
    def __init__(
        self,
        css_dir,
        js_dir,
        images_dir,
        templates_dir,
        blogs_dir,
        app_name="app",
        server_mode="prod",
        port_number=8000,
    ):
        self.css_dir = css_dir
        self.js_dir = js_dir
        self.images_dir = images_dir
        self.templates_dir = templates_dir
        self.blogs_dir = blogs_dir
        self.app_name = app_name
        self.server_mode = server_mode
        self.port_number = port_number

    def make(self):
        pass

    def start(self):
        """
        This method will perform necessary checks and start/restart server: dev or prod, depending on server_mode.
        """
        if self.server_mode not in {"prod", "dev"}:
            raise ValueError(
                f"server_mode is \"{self.server_mode}\", must be either 'prod' for WSGI or 'dev' for testing purposes."
            )
        working_dir = os.path.dirname(os.path.realpath(__file__))

        #cleanup after previous processes

        # read lsof output for server port_number
        with Popen(
            ["lsof", "-i", f":{str(self.port_number)}"], stdout=subprocess.PIPE
        ) as proc:
            lsof_line = proc.stdout.readlines(0)

        try:
            # check if any process listens on the port -> then separate pid from the string
            pid = str(lsof_line[1]).split(" ")[1]
            if pid:
                print("Killing process on pid={pid}")
                os.kill(int(pid), SIGTERM)
        except IndexError:
            print(f"No process listening on port {self.port_number}")

        # start
        if self.server_mode == "dev":
            os.environ["FLASK_APP"] = "app/app"
            subprocess.run(
                [
                    "flask",
                    "run",
                    "--host",
                    "0.0.0.0",
                    "--port",
                    f"{str(self.port_number)}",
                ]
            )
        elif self.server_mode == "prod":
            subprocess.run(
                [
                    "gunicorn",
                    "--bind",
                    f"0.0.0.0:{str(self.port_number)}",
                    "--chdir",
                    f"{working_dir}/app",
                    f"wsgi:{self.app_name}",
                ]
            )


if __name__ == "__main__":
    HomePage = HomePage(
        css_dir=os.path.join(".", "app/static/css"),
        js_dir=os.path.join(".", "app/static/js"),
        images_dir=os.path.join(".", "app/static/images"),
        templates_dir=os.path.join(".", "app/templates"),
        blogs_dir=os.path.join(".", "app/templates/blog"),
        app_name="app",
        server_mode="prod",
        port_number=8000
    )

    cmd = sys.argv[1]

    if cmd not in {"make", "start"}:
        raise ValueError(
            "Must provide option: 'make'/'start'"
        )

    if cmd == "make":
        HomePage.make()
    elif cmd == "start":
        HomePage.start()
