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
from argparse import ArgumentParser
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
        ssl_mode,
        server_mode,
        port_number,
    ):
        """
        ssl_mode: choose between "https" and "http"
        server_mode: dev - flask, prod - wsgi
        port_number: for https port should be 443, but it can be different with port redirect
        """
        self.css_dir = css_dir
        self.js_dir = js_dir
        self.images_dir = images_dir
        self.templates_dir = templates_dir
        self.blogs_dir = blogs_dir
        self.server_mode = server_mode
        self.port_number = port_number
        self.ssl_mode = ssl_mode

        self.SSL_CERT={
            "cert": "cert.pem", 
            "key": "key.pem"
            }

    def stop(self):
        # read lsof output for server port_number
        with Popen(
            ["lsof", "-i", f":{str(self.port_number)}"], stdout=subprocess.PIPE
        ) as proc:
            lsof_line = proc.stdout.readlines(0)

        try:
            # check if any process listens on the port -> then separate pid from the string
            pid = str(lsof_line[1]).split(" ")[1]
            if pid:
                print(f"Killing process on pid={pid}")
                os.kill(int(pid), SIGTERM)
        except IndexError:
            print(f"No process listening on port {self.port_number}")

    def start(self):
        """
        This method will perform necessary checks and start/restart server: dev or prod, depending on server_mode.
        """
        if self.server_mode not in {"prod", "dev"}:
            raise ValueError(
                f"server_mode is \"{self.server_mode}\", must be either 'prod' for WSGI or 'dev' for testing purposes."
            )
        working_dir = os.path.dirname(os.path.realpath(__file__))

        FLASK_CMD = [
            "flask",
            "run",
            "--host",
            "0.0.0.0",
            "--port",
            f"{str(self.port_number)}",
            ]

        WSGI_CMD=[
            "gunicorn",
            "--bind",
            f"0.0.0.0:{str(self.port_number)}",
            "--chdir",
            f"{working_dir}/app",
            f"wsgi:app",
            ]

        if self.ssl_mode == "https":
            FLASK_CMD.append(f"--cert=app/{self.SSL_CERT['cert']}")
            FLASK_CMD.append(f"--key=app/{self.SSL_CERT['key']}")
            WSGI_CMD.append("--certfile")
            WSGI_CMD.append(f"{self.SSL_CERT['cert']}")
            WSGI_CMD.append("--keyfile")
            WSGI_CMD.append(f"{self.SSL_CERT['key']}")

        # cleanup after previous processes
        self.stop()

        # start
        if self.server_mode == "dev":
            os.environ["FLASK_APP"] = "app/app"
            subprocess.run(
                FLASK_CMD
            )
        elif self.server_mode == "prod":
            subprocess.run(
                WSGI_CMD
            )


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('cmd')
    parser.add_argument("--ssl_mode", dest="ssl_mode",
                        help="switch https mode [http/https]", default="https")
    parser.add_argument("--server_mode", dest="server_mode",
                        help="switch between flask (dev) and wsgi (prod) [dev/prod]", default="dev")
    parser.add_argument("--port", dest="port_number",
                        help="set port", default=8080)

    args = parser.parse_args()

    if args.cmd not in {"make", "start", "stop"}:
        raise ValueError("Must provide option: 'make'/'start'/'stop'")

    HomePage = HomePage(
        css_dir=os.path.join(".", "app/static/css"),
        js_dir=os.path.join(".", "app/static/js"),
        images_dir=os.path.join(".", "app/static/images"),
        templates_dir=os.path.join(".", "app/templates"),
        blogs_dir=os.path.join(".", "app/templates/blog"),
        ssl_mode=args.ssl_mode,
        server_mode=args.server_mode,
        port_number=int(args.port_number),
    )



    if args.cmd == "make":
        HomePage.make()
    elif args.cmd == "start":
        HomePage.start()
    elif args.cmd == "stop":
        HomePage.stop()

