import asyncio
import logging
import websockets
import subprocess
import json
import socket
from subprocess import Popen, CREATE_NEW_CONSOLE, PIPE, STDOUT
import sys
import os

theproc = subprocess.Popen([sys.executable, "PP.py"])
theproc.communicate()


