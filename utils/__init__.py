# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '1.0.0'

import frappe

from .responder import *
from .exceptions import *
from .validator import *

def system_command(cmd):
	import subprocess
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	return process.communicate()