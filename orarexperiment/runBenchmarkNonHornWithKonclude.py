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

#mac
"""orarJarFile = "/Users/kien/git/ORAR/target/orar.jar"
owlRealizerJarFile = "/Users/kien/git/ORAR/target/owlrealizer.jar"
log4jproperty = "/Users/kien/git/ORAR/target/log4j.properties"
koncludePath = "/Users/kien/konclude/newestversion_11_Sept_2015/Konclude"
port = "9191"
"""
#frodo
orarJarFile = "/data/kien/benchmark/software/orar.jar"
owlRealizerJarFile ="/data/kien/benchmark/software/owlrealizer.jar"
log4jproperty = "/data/kien/benchmark/software/log4j.properties"
koncludePath = "/data/kien/benchmark/software/Konclude"
port = "9191"
    


resultFiles = []
# run the benchmark and return all result file of Clipper and Rapid in tuple
def runBenchmark(ontologyList, timeout_in_minutes, backupFolder):
   
    #Create a sub folder in backupFolder
    timeNow = time.strftime("%d_%m_%Y_%H_%M")
    backupDir = sys.argv[3] 
    newFolderInBackupDir = os.path.join(backupDir, "at" + timeNow);
    os.makedirs(newFolderInBackupDir)
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
                runKoncludeBenchmarch(tbox, aboxList, "nonhorn", timeout_in_minutes,newFolderInBackupDir)
            
    return resultFiles
                   
def runKoncludeBenchmarch(tbox, aboxList, dl, timeout_in_minutes, newFolderInBackupDir):
    
    aboxListBaseName = os.path.basename(aboxList);            
   
 
   
            # Run abstraction
    subprocess.call(['killall', '-9', '-u kientran', 'Konclude'])
    subprocess.call(['killall', '-9', '-u kientran', 'java'])
    outputFileAbstraction = tbox + "-" + aboxListBaseName + "-abstraction-with-konclude.result." + dl + ".txt"
    returnString = runOrarWithKonclude(orarJarFile, log4jproperty, koncludePath, port, tbox, aboxList, dl, timeout_in_minutes, outputFileAbstraction)
    if returnString == "timeout" or returnString == "error":
        printStringToFile(returnString, outputFileAbstraction)
            
    print("Backup result is stored in:" + newFolderInBackupDir)
    shutil.copy(outputFileAbstraction, newFolderInBackupDir)
            
    print("return code:")       
    print(returnString)        
    print("\n")
            
            # Run owlrealizer 
    subprocess.call(['killall', '-9', '-u kientran', 'Konclude'])
    subprocess.call(['killall', '-9', '-u kientran', 'java'])
    outputFileOWLReasoner = tbox + "-" + aboxListBaseName + "-konclude.result." + dl + ".txt"
    returnString = runKonclude(owlRealizerJarFile, log4jproperty, koncludePath, port, tbox, aboxList, dl, timeout_in_minutes, outputFileOWLReasoner)
    if returnString == "timeout" or returnString == "error":
        printStringToFile(returnString, outputFileOWLReasoner)
            
    print("Backup result is stored in:" + newFolderInBackupDir)
    shutil.copy(outputFileOWLReasoner, newFolderInBackupDir)   
            
    print("return code:")
    print(returnString)
    print("\n")
                        
    resultFiles.append(outputFileAbstraction)
    resultFiles.append(outputFileOWLReasoner)
   

def printStringToFile(stringToPrint, fileName):
    with open(fileName, mode='a', encoding='utf-8') as aFile:
        aFile.write(stringToPrint+"\n")              
                        
if __name__ == '__main__':
    if len(sys.argv) == 4:
        returnResultFiles = runBenchmark(sys.argv[1], sys.argv[2], sys.argv[3])
        print("#Result files:")
        for file in returnResultFiles:
            print(file)
        
    else:
        print("Please use only 3 arguments: ontologylist,  timeout in minutes,  backup-folder")
# Test
# runBenchmark("ontologyList.txt", "60", "./")
