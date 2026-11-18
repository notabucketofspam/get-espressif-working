#!/usr/bin/env python
from __future__ import print_function, division
import sys
import subprocess
import os.path
import site

# Ensure UCRT64 site-packages (pyserial, click, etc.) are always found when invoked from VS
os.environ["PYTHONPATH"] = os.pathsep.join(site.getsitepackages())

paths = {}


def check_path(path):
    try:
        return paths[path]
    except KeyError:
        pass
    paths[path] = path
    try:
        winpath = subprocess.check_output(["cygpath", "-w", path]).strip().decode()
    except subprocess.CalledProcessError:
        return path
    if not os.path.exists(winpath):
        return path
    winpath = winpath.replace("\\", "/")
    paths[path] = winpath
    return winpath


def should_sync_intellisense(args):
    if "clean" in args or not os.path.exists("sdkconfig"):
        return False
    if not os.path.exists("esp8266_intellisense.props"):
        return True
    return os.path.getmtime("sdkconfig") > os.path.getmtime("esp8266_intellisense.props")


def main():
    print("Running make in '%s'" % check_path(os.getcwd()))
    make = subprocess.Popen(["make"] + sys.argv[1:] + ["BATCH_BUILD=1"])
    rc = make.wait()

    if rc == 0 and should_sync_intellisense(sys.argv[1:]):
        sync_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sync_intellisense.py")
        if os.path.exists(sync_script):
            subprocess.run([sys.executable, sync_script], check=False)

    sys.exit(rc)


if __name__ == "__main__":
    main()