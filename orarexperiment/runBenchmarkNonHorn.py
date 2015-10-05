#!/usr/bin/env python3
import sys
import time
import os
import shutil
import subprocess
from runOrarWithKonclude import runOrarWithKonclude
from runKonclude import runKonclude
from runOrarWithOWLReasoner import runOrarWithOWLReasoner
from runOWLReasoner import runOWLReasoner

#kill all java and python3 and Konclude running by kientran
#subprocess.call(['killall','-9','-u kientran','python3'])
subprocess.call(['killall','-9','-u kientran','Konclude'])
subprocess.call(['killall','-9','-u kientran','java'])

orarJarFile = "/Users/kien/git/ORAR/target/orar.jar"
owlRealizerJarFile = "/Users/kien/git/ORAR/target/owlrealizer.jar"
log4jproperty = "/Users/kien/git/ORAR/target/log4j.properties"
koncludePath = "/Users/kien/konclude/newestversion_11_Sept_2015/Konclude"
port = "9191"
    
reasonerList = ["konclude", "hermit", "fact", "pellet"]
numberOfReasoner = len(reasonerList)
resultFiles = []
# run the benchmark and return all result file of Clipper and Rapid in tuple
def runBenchmark(ontologyList, timeout_in_minutes, backupFolder):
   
    # For each ontology, run reasoner and print out the result
    with open(ontologyList, encoding='utf-8') as ontListFile:
        for aline in ontListFile:
            aline = str(aline.strip())
            if not aline == "" and not aline.startswith("%") and not aline.startswith("#"):
                splitLine = aline.split(',')
                tbox = splitLine[0].strip()
                aboxList = splitLine[1].strip()
                print('tbox:' + tbox)
                print('aboxList:' + aboxList)
                runAll(tbox, aboxList, "nonhorn", timeout_in_minutes)
    return resultFiles
                   
def runAll(tbox, aboxList, dl, timeout_in_minutes):
    
    for reasonerName in reasonerList:
                    # Run in horn 
        if reasonerName == "konclude":
                        
            outputFileAbstraction = tbox + "-" + dl + "-abstraction-with-konclude.result.txt"
            runOrarWithKonclude(orarJarFile, log4jproperty, koncludePath, port, tbox, aboxList, dl, timeout_in_minutes, outputFileAbstraction)
                        
            outputFileOWLReasoner = tbox + "-" + dl + "-konclude.result.txt"
            runKonclude(owlRealizerJarFile, log4jproperty, koncludePath, port, tbox, aboxList, dl, timeout_in_minutes, outputFileOWLReasoner)
                        
            resultFiles.append(outputFileAbstraction)
            resultFiles.append(outputFileOWLReasoner)
        else:
            outputFileAbstraction = tbox + "-" + dl + "-abstraction-with-" + reasonerName + ".result.txt"
            runOrarWithOWLReasoner(orarJarFile, log4jproperty, reasonerName, tbox, aboxList, dl, timeout_in_minutes, outputFileAbstraction)
                        
            outputFileOWLReasoner = tbox + "-" + dl + "-with-" + reasonerName + ".result.txt"
            runOWLReasoner(owlRealizerJarFile, log4jproperty, reasonerName, tbox, aboxList, dl, timeout_in_minutes, outputFileOWLReasoner)
                        
            resultFiles.append(outputFileAbstraction)
            resultFiles.append(outputFileOWLReasoner)

                        
if __name__ == '__main__':
    if len(sys.argv) == 4:
        returnResultFiles = runBenchmark(sys.argv[1], sys.argv[2], sys.argv[3])
        timeNow = time.strftime("%d_%m_%Y_%H_%M")
        backupDir = sys.argv[3] 
        newFolder = os.path.join(backupDir, "at" + timeNow);
        os.makedirs(newFolder)
        
        print("#Result files:")
        for file in returnResultFiles:
            print(file)
            shutil.copy(file, newFolder)

        print("All results have a backup version in the folder:" + newFolder)
    else:
        print("Please use only 3 arguments: ontologylist,  timeout in minutes,  backup-folder")
# Test
# runBenchmark("ontologyList.txt", "60", "./")
