#Main.py

from process import SessionData
from log import Log
from datetime import datetime,timedelta
from segementEmulator import Display


#Globals
name = "ben fekete"
debugMode = True
logging = False



def updateSession():
    """
    Updates Displays
    :return: None
    """
    if session.running:                                             #See if session is running
        global lastLap
        racer = session.getRacerByName(name)                        #retrive the racers parameters

        if isinstance(racer, int):                                  #Check if session object returned an error
            
            errDisp.print("404")
            lastLap = 0
            if logging:
                Log(False, "Racer Not In Sesson")
        else:
            if racer["LapNum"] != lastLap:                          #Check if a new lap has started, this is to avoid updating the display more than neccesary
                lastLap = racer["LapNum"]                           #Store current lap in "lastLap" and display data
                timeDisp.print(racer["LTime"])
                bTimeDisp.print(racer["BestLTime"]) 
    else:
        
        errDisp.print("408")
        if logging:
            Log(False, "No Session Running")
        
def getRaw(mode):
    """
    Introduces the Raw Data to the document
        :param mode: Bool          Indicates wether the program is in debug mode or not
        :return: String Or Int     Raw Json Data or Err code
    """
    global name
    
    if mode:
        name = "barry fox"                                          #Name of a racer in the Debug Dataset
        return SessionData.getDebugData()
    else:
        name = name.lower()                                         #Format name for easy confirmation later
        return SessionData.getData(logging)
    
def updateRaw():
    """
    Intoduces Raw data to the document, then checks if data has arrived, if yes, returns the raw data
    :return: String     Raw Json Data
    """
    raw = getRaw(debugMode)
    startTime = datetime.now()
    
    while isinstance(raw, int):                                     #check if raw object returned error
    
        if (datetime.now() - startTime) >= period:                  #if raw object returned an error, periodicall try again until it doesnt
            raw = SessionData.getData(logging)
            errDisp.print("444")
            startTime = datetime.now()
    
    return raw






period = timedelta(seconds = 1, microseconds = 200000)              #Total time between requests
errDisp = Display("Error:")                                         #Setting up display objects
bTimeDisp = Display("Best Time:")
timeDisp = Display("Last Time:")
lastLap = 0

session = SessionData(updateRaw(), logging)                         #Session object holds the parameters of the session as well as all the reacers in the session
startTime = datetime.now()                                          #Starting point of refresh timer

while True:
    #print (datetime.now() - startTime)
    if (datetime.now() - startTime) >= period:                      #Check if enough time has passed to get session updates
        
        session.update(updateRaw())                                 #Update session object with new data
        updateSession()