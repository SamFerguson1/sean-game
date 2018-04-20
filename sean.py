from graphics import *
class Sean:

    def __init__(self,height, width):
        self.image = Image(Point(width*.5, height*.3),"sean.gif")
        self.fuckMeter = 0
        self.didRun = 0

    def incrementFuck(self,answer):
        if answer == "y":
            self.fuckMeter +=1
    def incrementDidRun(self):
        self.didRun += 1

    def getSeanFace(self):
        return self.image
    
    def getFuck(self):
        return self.fuckMeter

    def seanResponse(self, choice):
        choice = choice.lower()
        if self.didRun == 1:
            if self.fuckMeter == 1:
                return "hey sam I have to go to work and I won't quit because I'm a bitch, it's been fun playing with you though.............."
            if self.fuckMeter == 0:
                return "That's okay..... It would have been nice to play with you though......."
        elif self.didRun ==2:
            if self.fuckMeter == 2:
                return "alright sam that was very fun, see you tomorrow"
            if self.fuckMeter == 1:
                return "oh oh well that's fine, I'll just play with james good night"
            if self.fuckMeter == 0:
                return "you know what fuck you sam I guess you're just a piece of shit fuck you moron" #game over
        elif self.didRun == 3:
            #if they have 1 for fuck meter still they said no twice
            if self.fuckMeter == 3:
                return "sean abruptly gets off"
            if self.fuckMeter == 2 and choice == "a":
                return "sean abruptly gets off"
            if self.fuckMeter == 2 and choice =="b":
                return "oh well fuck that sucks you're still okay i guess"
            if self.fuckMeter == 1:
                return "you know what fuck you sam I guess you're just a piece of shit fuck you moron" #game over
        elif self.didRun == 4:
            if choice == "a":
                return "sean abruptly gets off"
            else:
                return "you know what fuck you sam I guess you're just a piece of shit fuck you moron" #game over
            
            
