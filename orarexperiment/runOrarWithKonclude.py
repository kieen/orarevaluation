from runCommandWithTimeout import runCommandWithTimeout

def runOrarWithKonclude(orarJarFile, log4jproperty, koncludePath, port, tbox, aboxList, dl, timeout_in_minutes, outputFile):
    commandString = ""
    commandString += "java -jar -Xmx100G"
    commandString += " -Dlog4j.configuration=file:" + log4jproperty
    commandString += " " + orarJarFile
    commandString += " -reasoner konclude"
    commandString += " -koncludepath " + koncludePath
    commandString += " -port " + port
    commandString += " -tbox " + tbox
    commandString += " -abox " + aboxList
    commandString += " -dl " + dl
    commandString += " -ontinfo "
    commandString += " -absinfo "
    commandString += " -loadtime "
    commandString += " -runtime "
    commandString += " -typeinfo "
    commandString += " > " + outputFile
    timeout_in_second=int(timeout_in_minutes) *60
    return runCommandWithTimeout(commandString, timeout_in_second)
#Test
"""
orarJarFile="/Users/kien/git/ORAR/target/orar.jar"
reasonerName="hermit"
log4jproperty="/Users/kien/git/ORAR/target/log4j.properties"
tbox="/Users/kien/git/ORAR/src/test/resources/testcli/tbox1.owl"
aboxList="/Users/kien/git/ORAR/src/test/resources/testcli/aboxList1.txt"
dl="nonhorn"
timeout_in_minutes="2"
outputFile="testRunOrarWithOWLReasoner.log"
koncludePath="/Users/kien/konclude/newestversion_11_Sept_2015/Konclude"
port="9191"
runOrarWithKonclude(orarJarFile, log4jproperty, koncludePath, port, tbox, aboxList, dl, timeout_in_minutes, outputFile)
"""