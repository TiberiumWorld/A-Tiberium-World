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
    projectStateDir  = os.path.join(projectRoot, "history", "states")
    stateDir  = os.path.join("C:\\","Programs", "SteamApps", "Hearts of Iron IV", "history", "states")

    os.chdir(projectRoot)

    gameStates = []
    files = glob.glob(os.path.join(stateDir, "**", "*.txt"), recursive=True)
    for file in files:
        s = file.split('-')[0]
        s = s.replace(str(stateDir), "")
        s = s.replace("\\", "")
        gameStates.append(s)

    doneStates = []
    files = glob.glob(os.path.join(projectStateDir, "**","*.txt"), recursive=True)
    for file in files:
        s = file.split('-')[0]
        s = s.replace(str(projectStateDir), "")
        s = s.replace("\\", "")
        doneStates.append(s)

    print("Total States: ", len(gameStates))
    print("Done States:  ", len(doneStates))
    print("States left:  ", len(gameStates)-len(doneStates))

if __name__ == "__main__":
    sys.exit(main())