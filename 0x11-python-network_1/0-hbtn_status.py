#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status

import urllib
from urllib import request
resp = request.urlopen("https://alx-intranet.hbtn.io/status")
