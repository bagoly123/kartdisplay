#Process.py

import json
from requests import post                                       #External lib "Request" Required
from log import Log
class SessionData(object):
    
    def __init__(self, raw, logging):
        """
        Init
            :param self:
            :param raw:     json containing session data
        """
        self.racersByName = {}                                  #All racers in session sorted by name
        self.racersByNum = {}                                   #          -           sorted by kart number
        self.logging = logging
        
        self.update(raw)
        
        self.sessionType = self.getSessionType()
        self.winType = self.getWinType()
        self.running = self.getRunning()
        self.lapsLeft = self.getLapsLeft()
        
        

        
    def update(self, raw):
        """
        Updates self.data with new raw
            :param self: 
            :param raw: raw data json
            :return: None
        """   
        self.data = json.loads(raw)["Messages"].pop()["Args"][0] #Navigates raw json to retrive relevant data, see refrence in documentation
        
        self.sessionType = self.getSessionType()
        self.winType = self.getWinType()
        self.running = self.getRunning()
        self.lapsLeft = self.getLapsLeft()

        self.getRacers()
        if self.logging:
            self.dump(self.racersByName)                            #For debug/loging purpuses
        
    
    
    def getRacers(self):
        """
        Puts all racers in session into two dictionaries, one indexed by kart number the other by racer name
            :param self:
            :return: None
        """
        
        for x in self.data["ScoreboardData"]:
            self.racersByName[x["RacerName"].lower()] = x
            self.racersByNum[x["AutoNo"]] = x
    
    
    def getRacerByName(self, name):
        """
        If given racer in is in racersByName dictionary, returns that racers dictionary. If not then retunrs err code 404
            :param self: 
            :param name:    Name of racer
            :return:        int OR dict
        """   
        
        if name in self.racersByName:
            
            return self.racersByName[name]
        else:
            
            return 404
    
    
    def getRacerByNum(self, num):
        """
        If given kart in is in racersByNum dictionary, returns that racers dictionary. If not then retunrs err code 404
            :param self: 
            :param num:     Kart Number of racer
            :return:        int OR dict
        """ 
        
        if num in self.racersByNum:
            
            return self.racersByNum[num]
        else:
            
            return 404
    
    
    def getRunning(self):
        """
        Check if session is running
            :param self:
            :return: Bool
        """ 
         
        return self.data["RaceRunning"]
    
    
    def getSessionType(self):
        """
        Returns Name of Heat Type 
            :param self:
            :return: str
        """   
        return self.data["HeatTypeName"]
    
    
    def getWinType(self):
        """
        Retuns Race Win Parameter
            :param self:
            :return: str
        """   
        return self.data["Winby"]
    
    def getLapsLeft(self):
        """
        Returns number of laps left or the ammount of time left, depending on the Session Type
            :param self:
            :return: int OR (datetime)?
        """   
        return self.data["LapsLeft"]
    
    @staticmethod
    def getData(n=10):
        """
        Downloads raw data json using POST request
            :param n=10: int       optional parameter to set number of tries before error message
            :return: dict or int   json formated so python can handle it
        """       
        url = "https://rwdevon.clubspeedtiming.com/SP_Center/signalr"                                          #URL for POST request
    
        data = {                                                                                               #Payload for POST request
            "clientId":         "c74bf7d5-4187-4bf1-8c9a-0f396ab32d02",
            "messageId":        "3030",
            "connectionData":   "[{\"name\":\"SP_Center.ScoreBoardHub\",\"methods\":[\"refreshGrid\"]}]",
            "transport":        "longPolling",
            "groups":           "SP_Center.ScoreBoardHub.1"
            }
        
        for i in range(n):
        
            try:
            
                response = post(url = url, data = data)                                              #Post request data stored in response object
            except Exception as e:                                                                            #If request throws conncetion error exceptin, catch and log, return error
                
                if i == n-1:
                    if logging:
                        Log(True, e)
                    return 408
        
            else:
                return response.text
    
    @staticmethod
    def getDebugData():
        """
        Returns archived session data for debug mode
        :return: dict       json formated so python can handle it
        """   
        with open("debugData.txt", "r") as file:
            return file.read()
    
    @staticmethod
    def dump(dict):
        """
        Debug method for dumping dicts or lists into a json file
            :param dict: dict or list       dict or list to be demped
            :return: none
        """
        with open("debugData.json", "a") as file:
            json.dump(dict, file)
            file.write("\n")