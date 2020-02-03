from datetime import datetime

class Log(object):

    def __init__(self, type, error):
        """
        Init
            :param type: Bool       if true then instance is error, else its is log
            :param error: Str       the log message
        """   
        
        self.error = error
        self.type = type
        self.time = datetime.now()
        
        if self.type:
            self.writeError()
        else:
            self.writeLog()


    
    def logContent(self):
        
        """
        Formats the given information into a readable forat and returns it
            :param self: 
        """ 
        
        text = str(self.time) + ":       " + str(self.error) + "\n"

        return text
    
    def writeError(self):
        """
        writes error to error log file, then deletes instace
            :param self: 
        """   
        
        errorFile = open("_ErrorLog.txt", "a")
        errorFile.write(self.logContent())
        errorFile.close()
        del self
    
    def writeLog(self):
        """
        writes log to general log file, then deletes instace
            :param self: 
        """   
        
        logFile = open("_Log.txt", "a")
        logFile.write(self.logContent())
        logFile.close()
        del self
