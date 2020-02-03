#Main.py

from process import SessionData
from log import Log
from download import GetData
from requests import post                                       #External lib "Request" Required
from datetime import datetime,timedelta
from segementEmulator import Display





period = timedelta(seconds = 1, microseconds = 200000)          #Total time between requests
name = "leon blake".lower()                                   #Name of racer to be tracked
raw = GetData().data                                            #object containing raw json in form of a string
startTime = datetime.now()
errDisp = Display("Error:")                                     #Setting up display objects
bTimeDisp = Display("Best Time:")
timeDisp = Display("Last Time:")


while isinstance(raw, int):                                     #check if raw object returned error
    
    if (datetime.now() - startTime) >= period:                  #if raw object returned an error, periodicall try again until it doesnt
        raw = GetData().data
        errDisp.print("444")
        startTime = datetime.now()

session = SessionData(raw)                                      #Session object holds the parameters of the session as well as all the reacers in the session

if session.running:                                             #See if session is running
    racer = session.getRacerByName(name)                        #retrive the racers parameters

    if isinstance(racer, int):                                  #Check if session object returned an error
        
        errDisp.print("404")
        Log(False, "Racer Not In Sesson")
    else:
        lastLap = racer["LapNum"]                               #Store current lap in "lastLap" and display data
        timeDisp.print(racer["LTime"])
        bTimeDisp.print(racer["BestLTime"])
        
        session.dump(racer)                                     #For debuging purpuses
else:
    
    errDisp.print("408")
    Log(False, "No Session Running")

startTime = datetime.now()                                      #Starting point of refresh timer

while True:
    #print (datetime.now() - startTime)
    if (datetime.now() - startTime) >= period:                  #Check if enough time has passed to get session updates
        
        raw = GetData().data                                    #update raw with fresh data
        startTime = datetime.now()                              #reset refresh timer
        
        while isinstance(raw, int):                             #check if raw object returned error
    
            if (datetime.now() - startTime) >= period:          #if raw object returned an error, periodicall try again until it doesnt
                errDisp.print("444")
                raw = GetData().data
                startTime = datetime.now()

        session.update(raw)                                    #Update session object with new data

        
        if not session.running:                                 #Check if session is still running
            
            errDisp.print("403")
            Log(False, "No Session Running")
        else:
            racer = session.getRacerByName(name)
            if racer["LapNum"] != lastLap:                  #Check if a new lap has started, this is to avoid updating the display more than neccesary
                lastLap = racer["LapNum"]
                timeDisp.print(racer["LTime"])              #Display data
                bTimeDisp.print(racer["BestLTime"])
                
                session.dump(racer)                         #For debuging purpuses
