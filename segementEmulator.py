from emulatorCharacters import characters

class Display(object):
    
    def __init__(self, title):
        """
        Init
            :param self: 
            :param title: str       debug text shown above the display in console
        """   
        self.title = title
        self.height = 7                                             #No. of rows occupied by display in console
    
    def print(self, text):
        """
        Prints emulated segemnt display to console, only prints characters that are within its dictionary
            :param self: 
            :param text: str    text to be displayed
        """   
        text = str(text)
        print(self.title)
        
        for y in range(self.height):
            
            for x in range(len(text)):
                
                if text[x] in characters:
                    
                    print(characters[text[x]][y], end = " ")
                
            print()
                    
                
        
