1#!/usr/bin/env python3

import sys
import os
import glob
import random
import codecs

__version__ = 1.0

def cleanCaptialString(line=''):
    line = line.replace("ï»¿", "")
    line = line.strip()
    return line


def main():
    scriptPath  = os.path.realpath(__file__)
    scriptRoot  = os.path.dirname(scriptPath)
    countryDir  = os.path.join("C:\\","Programs", "SteamApps", "Hearts of Iron IV","history", "countries")
    
    #os.chdir(countryDir)
    os.chdir(scriptRoot)

    #Get Textures
    for (path, dirs, files) in os.walk(countryDir):
        for country in files:
            if not ".txt" in country:
                continue
            contryTag = country[:3]
            try:
                fileContry = open(os.path.join(countryDir, country), 'r')
                contryFile = fileContry.readlines()
                print("Reading file: {}".format(country, os.path.join(countryDir, country)))
                for line in contryFile:
                    if "capital =" in line:
                        capital = cleanCaptialString(line)
                    continue
            except:
                try:
                    fileContry = open(os.path.join(countryDir, country), "rt", encoding="utf-8")
                    contryFile = fileContry.readlines()
                    print("Reading file: {} (File have been re-encoded)".format(country, os.path.join(countryDir, country)))
                    for line in contryFile:
                        if "capital =" in line:
                            capital = cleanCaptialString(line)
                        continue
                except:
                    print("\033[91mERROR reading: {} {}\033[0m".format(country, fileContry))
                    continue
            # Build nation
            ruling_party = random.choice([
                "democratic","democratic","democratic","democratic","democratic","democratic","democratic","democratic",
                "neutrality","neutrality","neutrality","neutrality","neutrality",
                "communism","communism","communism",
                "fascism","fascism"
            ])

            if ruling_party in ["democratic","neutrality", "communism"]:
                if "democratic" in ruling_party:
                    elections_allowed = random.choice([
                        "yes","yes","yes","yes","yes",
                        "no",
                    ])
                if "neutrality" in ruling_party:
                    elections_allowed = random.choice([
                        "yes","yes","yes","yes","yes",
                        "no","no","no"
                    ])
                if "communism" in ruling_party:
                    elections_allowed = random.choice([
                        "yes",
                        "no","no","no","no"
                    ])
            else:
                elections_allowed = "no"

            if "no" in elections_allowed:
                last_election = [random.randint(1995,2008),random.randint(1,11),random.randint(1,28)]
            else:
                last_election = [random.randint(2005,2009),random.randint(1,11),random.randint(1,28)]

            set_stability = round(random.uniform(0.2, 1.0), 2)

            
            #set_popularities = [0,0,0,0]
            a = random.randint(1,100)
            b = random.randint(1,100)
            c = random.randint(1,100)
            d = random.randint(1,100)

            if ruling_party == "democratic":
                a = a+25
            elif ruling_party == "communism":
                b = b+25
            elif ruling_party == "fascism":
                c = c+25
            elif ruling_party == "neutrality":
                d = d+25

            set_popularities_total = a+b+c+d
            a = round(a/(set_popularities_total), 2)
            b = round(b/(set_popularities_total), 2)
            c = round(c/(set_popularities_total), 2)
            d = round(d/(set_popularities_total), 2)
            set_popularities_total_dec = a+b+c+d
            set_popularities_total_dec = round(set_popularities_total_dec, 2)
            while set_popularities_total_dec != 1.0:
                removeFrom = random.randint(1,4)
                if set_popularities_total_dec >= 1.0:
                    if removeFrom == 1:
                        a = a-0.01
                    elif removeFrom == 2:
                        b = b-0.01
                    elif removeFrom == 3:
                        c = c-0.01
                    elif removeFrom == 4:
                        d = d-0.01
                    else:
                        pass
                    set_popularities_total_dec = set_popularities_total_dec - 0.01
                elif set_popularities_total_dec <= 1.0:
                    if removeFrom == 1:
                        a = a+0.01
                    elif removeFrom == 2:
                        b = b+0.01
                    elif removeFrom == 3:
                        c = c+0.01
                    elif removeFrom == 4:
                        d = d+0.01
                    else:
                        pass
                    set_popularities_total_dec = set_popularities_total_dec + 0.01
                else:
                    pass

            a = float(a)
            a = a * 100
            b = float(b)
            b = b * 100
            c = float(c)
            c = c * 100
            d = float(d)
            d = d * 100
            set_popularities = [round(a),round(b),round(c),round(d)]

            newNation = ["# {} {} ({}) {}".format(contryTag, ruling_party, elections_allowed, set_popularities),
            capital,
            "",
            "# oob = \"\"",
            "",
            "set_research_slots = 2",
            "set_stability = {}".format(set_stability),
            "set_war_support = 0",
            "",
            "set_convoys = 500",
            "",
            "set_politics = {",
            "\truling_party = {}".format(ruling_party), 
            "\tlast_election = \"{}.{}.{}\"".format(last_election[0],last_election[1],last_election[2]),
            "\telection_frequency = 48",
            "\telections_allowed = yes".format(elections_allowed),
            "}",
            "set_popularities = {} # Total: 100% = {} ({})".format("{", set_popularities_total, round(set_popularities_total_dec, 2)),
            "\tdemocratic = {}".format(set_popularities[0]),
            "\tcommunism = {}".format(set_popularities[1]),
            "\tfascism = {}".format(set_popularities[2]),
            "\tneutrality = {}".format(set_popularities[3]),
            "}",
            "",
            "set_party_name = {",
            "\tideology = democratic",
            "\tlong_name = \"Democratic Party\"",
            "\tname = \"Democratic Party\"",
            "}",
            "set_party_name = {",
            "\tideology = communism",
            "\tlong_name = \"Communist Party\"",
            "\tname = \"Communist Party\"",
            "}",
            "set_party_name = {",
            "\tideology = fascism",
            "\tlong_name = \"Faschist Party\"",
            "\tname = \"Faschist Party\"",
            "}",
            "set_party_name = {",
            "\tideology = neutrality",
            "\tlong_name = \"Free Party\"",
            "\tname = \"Free Party\"",
            "}"]
            print("{} ({}), {} (Elections: {}) {} (sum: {})".format(country, contryTag, ruling_party, elections_allowed, set_popularities, set_popularities[0]+set_popularities[1]+set_popularities[2]+set_popularities[3]))
            output = os.path.join(scriptRoot, "output")
            try:
                os.stat(output)
            except:
                os.mkdir(output)
            outputFile = os.path.join(output, country)
            fileContry = open(outputFile, "w+", encoding='utf-8-sig')
            for i in newNation:
                fileContry.write(i)
                fileContry.write("\n")

            fileContry.close
        break

    
if __name__ == "__main__":
    sys.exit(main())