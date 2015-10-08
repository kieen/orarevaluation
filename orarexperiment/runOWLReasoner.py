from runCommandWithTimeout import runCommandWithTimeout

def runOWLReasoner(owlRealizerJarFile, log4jproperty, reasonerName, tbox, aboxList, dl, timeout_in_minutes, outputFile):
    commandString = ""
    commandString += "java -jar -Xms50G -Xmx100G"
    commandString += " -Dlog4j.configuration=file:" + log4jproperty
    commandString += " " + owlRealizerJarFile
    commandString += " -reasoner "+ reasonerName
    commandString += " -tbox " + tbox
    commandString += " -abox " + aboxList
    commandString += " -dl " + dl
    commandString += " -ontinfo "
    commandString += " -loadtime "
    commandString += " -runtime "
    commandString += " > " + outputFile
    timeout_in_second=int(timeout_in_minutes) *60
    return runCommandWithTimeout(commandString, timeout_in_second)
#Test
"""
owlRealizerJarFile="/Users/kien/git/ORAR/target/owlrealizer.jar"
log4jproperty="/Users/kien/git/ORAR/target/log4j.properties"
tbox="/Users/kien/git/ORAR/src/test/resources/testcli/tbox1.owl"
aboxList="/Users/kien/git/ORAR/src/test/resources/testcli/aboxList1.txt"
dl="nonhorn"
timeout_in_minutes="2"
outputFile="test.log"
reasonerName="hermit"
runOWLReasoner(owlRealizerJarFile, log4jproperty,reasonerName , tbox, aboxList, dl, timeout_in_minutes, outputFile)
"""