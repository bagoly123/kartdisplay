#Download.py

from requests import post
from log import Log

class GetData(object):
    
    def __init__(self):
        
        self.url = "https://rwdevon.clubspeedtiming.com/SP_Center/signalr"                                          #URL for POST request
    
        self.data = {                                                                                               #Payload for POST request
            "clientId":         "c74bf7d5-4187-4bf1-8c9a-0f396ab32d02",
            "messageId":        "3030",
            "connectionData":   "[{\"name\":\"SP_Center.ScoreBoardHub\",\"methods\":[\"refreshGrid\"]}]",
            "transport":        "longPolling",
            "groups":           "SP_Center.ScoreBoardHub.1"
            }
        
        self.data = self.getRaw()
    
    def getRaw(self):
        """
        Tries to retrive json data through POST request to URL, tries n times before returning an error
            :param self:
            :return: str OR int
        """   
        n = 10
        
        for i in range(n):
        
            try:
            
                self.response = post(url = self.url, data = self.data)                                              #Post request data stored in response object
            except Exception as e:                                                                            #If request throws conncetion error exceptin, catch and log, return error
                
                if i == n-1:
                    Log(True, e)
                    return 408
        
            else:
                return(self.response.text)
    
        