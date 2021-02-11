1#!/usr/bin/env python3

import sys
import os
import glob
import random
import codecs
import re

__version__ = 1.0

def dataCollector(file):
    print(os.path.basename(file))
    f = open(file, "r")
    f = f.read()
    #result = re.search(r"\{([A-Za-z0-9_]+)\}", f)
    data = re.findall(r"(?s)= (\{.*?\s\})(?!\S)", f)
    for l in data:
        print(l)
        
def main():
    scriptPath  = os.path.realpath(__file__)
    scriptRoot  = os.path.dirname(scriptPath)
    projectRoot = os.path.dirname(os.path.dirname(scriptPath))

    os.chdir(projectRoot)

    files = glob.glob(os.path.join(projectRoot, "**", "*.txt"), recursive=True)

    for file in files:
        dataCollector(file)
        input

if __name__ == "__main__":
    sys.exit(main())