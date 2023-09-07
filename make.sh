#!/bin/bash

command -v g++ >/dev/null 2>&1 || { echo >&2 "g++ is not installed.  Aborting."; exit 1; }

command -v python >/dev/null 2>&1 || { echo >&2 "Python is not installed. Aborting."; exit 1; }

mv cptool.py cptool

chmod +x cptool

mv cptool /usr/local/bin/

