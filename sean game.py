from graphics import *
from sean import Sean
import time
def getClickArea(obj,win):
#purpose create the clickable range for a given rectangle object
#input: rectangle, windowobject
#output:the x and y values of an object in a tuple
    objp1 = obj.getP1()
    objp2 = obj.getP2()
    objp1x = objp1.getX()
    objp2x = objp2.getX()
    objp1y = objp1.getY()
    objp2y = objp2.getY()
    yRange = objp1y,objp2y
    xRange = objp1x,objp2x
    return (xRange,yRange)



    
    

def playGame():
    playAgain = True
    height  =600
    width = 800
    win = GraphWin("Sean Dating Sim",  width, height)
    sean = Sean(height, width)
    welcome = Text(Point(width//2, height//2) ,"Sean Dating Sim 1! Quest For Toes")
    welcome.setSize(36)
    welcome.setStyle("bold italic")
    welcome.setTextColor("red")
    click = Text(Point(width*.5,height*.95), "Click anywhere to continue")
    messages = open("messages.txt", "r")
    messages = messages.readlines()
    yesBox = Rectangle(Point(width*.3,height*.8),Point(width*.45,height*.9))
    noBox = Rectangle(Point(width*.55,height*.8),Point(width*.7,height*.9))
    yesText = Text(Point(width*.37,height*.85), "Yes")
    noText = Text(Point(width*.62,height*.85), "No")
    yesClick = getClickArea(yesBox,win)
    noClick = getClickArea(noBox,win)
    msgs = open("scenario.txt","r")
    msgs = msgs.readlines()
    for i in range(len(msgs)-1):
        msgs[i] = msgs[i][:-1]
    msgs1 = msgs[0]
    msgs2 = msgs[1]
    msgs3 = msgs[2]
    msgs4 = msgs[3]
    msgs5 = msgs[4]
    msgs6 = msgs[5]
    msgs7 = msgs[6]
    msgs8 = msgs[7]
    msgs9 = msgs[8]

    for i in range(len(messages)-1):
        messages[i] = messages[i][:-1]
    while playAgain == True:
        welcome.draw(win)
        click.draw(win)
        win.getMouse()
        welcome.undraw()
        click.undraw()
        time.sleep(.5)
        message1 = messages[0]
       
        for i in range(len(message1)):
            display = message1[:i]
            texty = Text(Point(width*.5, height*.5), display)
            texty.draw(win)
            time.sleep(.05)
            texty.undraw()
        texty.draw(win)
        time.sleep(.5)
#that is
        message2 = messages[1]
        for i in range(len(message2)):
            display = message2[:i+1]
            texty2 = Text(Point(width*.5, height*.55), display)
            texty2.draw(win)
            time.sleep(.05)
            texty2.undraw()
        texty2.draw(win)
        time.sleep(.5)
        texty.undraw()
        texty2.undraw()
# more on his

        message3 = messages[2]
        for i in range(len(message3)):
            display = message3[:i]
            texty = Text(Point(width*.5, height*.5), display)
            texty.draw(win)
            time.sleep(.05)
            texty.undraw()
        texty.draw(win)
        time.sleep(.4)
#his toes
        message4 = messages[3]
        for i in range(len(message4)):
            display = message4[:i+1]
            texty2 = Text(Point(width*.5, height*.55), display)
            texty2.draw(win)
            time.sleep(.05)
            texty2.undraw()
        texty2.draw(win)
        time.sleep(.5)
        texty.undraw()
        texty2.undraw()
#anyway
        message5 = messages[4]
        for i in range(len(message5)):
            display = message5[:i]
            texty = Text(Point(width*.5, height*.5), display)
            texty.draw(win)
            time.sleep(.05)
            texty.undraw()
        texty.draw(win)

#is toes
        message6 = messages[5]
        for i in range(len(message6)):
            display = message6[:i+1]
            texty2 = Text(Point(width*.5, height*.55), display)
            texty2.draw(win)
            time.sleep(.05)
            texty2.undraw()
        texty2.draw(win)
        time.sleep(.5)
        texty.undraw()
        texty2.undraw()
        
        texty = Text(Point(width*.5,height*.5), "oh FUCK here he comes now")
        texty.setSize(36)
        texty.setStyle("bold italic")
        texty.draw(win)
        for i in range(15):
            texty.undraw()
            shift = i%2     
            if shift == 0:
                texty = Text(Point(width*.53,height*.5), "oh FUCK here he comes now")
                texty.setSize(36)
                texty.setStyle("bold italic")
                texty.draw(win)
            if shift == 1:
                texty = Text(Point(width*.47,height*.5), "oh FUCK here he comes now")
                texty.setSize(36)
                texty.setStyle("bold italic")
                texty.draw(win)
            time.sleep(.1)
        click.draw(win)
        win.getMouse()
        click.undraw()
        texty.undraw()
        seanFace = sean.getSeanFace()
        seanFace.draw(win)
        message7 = messages[6]
        for i in range(len(message7)):
            display = message7[:i+1]
            texty = Text(Point(width*.5, height*.7), display)
            texty.draw(win)
            time.sleep(.05)
            texty.undraw()
        texty.draw(win)
        time.sleep(.2)
        yesBox.draw(win)
        noBox.draw(win)
        yesText.draw(win)
        noText.draw(win)
        answer= "fuck"
        validClick = False
        while validClick == False:
            click1 = win.getMouse()
            if (click1.getX() >= yesClick[0][0] and click1.getX() <=yesClick[0][1]) and (click1.getY() >= yesClick[1][0] and click1.getY() <=yesClick[1][1]):
                answer = "y"
                validClick = True
            if (click1.getX() >= noClick[0][0] and click1.getX() <=noClick[0][1]) and (click1.getY() >= noClick[1][0] and click1.getY() <=noClick[1][1]):
                answer = "n"
                validClick = True

        time.sleep(.2)
        texty.undraw()
        yesBox.undraw()
        noBox.undraw()
        yesText.undraw()
        noText.undraw()
        sean.incrementFuck(answer)
        sean.incrementDidRun()

        message = sean.seanResponse(answer)
        if answer == "y":
            yep = "you play for a hot minute. He's not the best player but he's good......"
            for i in range(len(yep)):
                display = yep[:i+1]
                texty = Text(Point(width*.5, height*.7), display)
                texty.draw(win)
                time.sleep(.06)
                texty.undraw()
            texty.draw(win)
            time.sleep(.7)
            texty.undraw()
            for i in range(len(message)):
                display = message[:i+1]
                texty = Text(Point(width*.5, height*.7), display)
                texty.draw(win)
                time.sleep(.04)
                texty.undraw()
            texty.draw(win)
        if answer == "n":
            for i in range(len(message)):
                display = message[:i+1]
                texty = Text(Point(width*.5, height*.7), display)
                texty.draw(win)
                time.sleep(.04)
                texty.undraw()
            texty.draw(win)
        time.sleep(.5)
        texty.undraw()
        seanFace.undraw()
    ################################NEXT MORNING
        nextMorning = Text(Point(width*.5,height*.5), "the very next morning")
        nextMorning.setSize(36)
        nextMorning.setStyle("bold italic")
        nextMorning.draw(win)
        time.sleep(.3)
        click.draw(win)
        win.getMouse()
        nextMorning.undraw()
        click.undraw()
        time.sleep(.2)
        seanFace.draw(win)
        message8 = messages[7]
        message9= messages[8]
        for i in range(len(message8)):
            display = message8[:i+1]
            texty = Text(Point(width*.5, height*.7), display)
            texty.draw(win)
            time.sleep(.05)
            texty.undraw()         
        texty.draw(win)
        for i in range(len(message9)):
            display = message9[:i+1]
            texty2 = Text(Point(width*.5, height*.75), display)
            texty2.draw(win)
            time.sleep(.05)
            texty2.undraw()         
        texty2.draw(win)
        time.sleep(.2)
        yesBox.draw(win)
        noBox.draw(win)
        yesText.draw(win)
        noText.draw(win)
        answer= "fuck"
        validClick = False
        while validClick == False:
            click1 = win.getMouse()
            if (click1.getX() >= yesClick[0][0] and click1.getX() <=yesClick[0][1]) and (click1.getY() >= yesClick[1][0] and click1.getY() <=yesClick[1][1]):
                answer = "y"
                validClick = True
            if (click1.getX() >= noClick[0][0] and click1.getX() <=noClick[0][1]) and (click1.getY() >= noClick[1][0] and click1.getY() <=noClick[1][1]):
                answer = "n"
                validClick = True

        time.sleep(.2)
        texty.undraw()
        texty2.undraw()
        yesBox.undraw()
        noBox.undraw()
        yesText.undraw()
        noText.undraw()
        sean.incrementFuck(answer)
        sean.incrementDidRun()

##############we have the answer here
        message = sean.seanResponse(answer)
        if answer == "y":
            yep = "you play for a hot minute. He's not the best player but he's good......"
            for i in range(len(yep)):
                display = yep[:i+1]
                texty = Text(Point(width*.5, height*.7), display)
                texty.draw(win)
                time.sleep(.06)
                texty.undraw()
            texty.draw(win)
            time.sleep(.7)
            texty.undraw()
            for i in range(len(message)):
                display = message[:i+1]
                texty = Text(Point(width*.5, height*.7), display)
                texty.draw(win)
                time.sleep(.04)
                texty.undraw()
            texty.draw(win)
        if answer == "n":
            for i in range(len(message)):
                display = message[:i+1]
                texty = Text(Point(width*.5, height*.7), display)
                texty.draw(win)
                time.sleep(.04)
                texty.undraw()
            texty.draw(win)
        if sean.getFuck() == 0:
            time.sleep(1)
            win.close()
        time.sleep(.5)
        texty.undraw()
        seanFace.undraw()        
######################THE NEXT MORNING
        nextMorning.draw(win)
        time.sleep(.3)
        click.draw(win)
        win.getMouse()
        nextMorning.undraw()
        click.undraw()
        time.sleep(.2)
        seanFace.draw(win)
        message10 = messages[9]
        message11= messages[10]
        for i in range(len(message10)):
            display = message10[:i+1]
            texty = Text(Point(width*.5, height*.7), display)
            texty.draw(win)
            time.sleep(.05)
            texty.undraw()         
        texty.draw(win)
        for i in range(len(message11)):
            display = message11[:i+1]
            texty2 = Text(Point(width*.5, height*.75), display)
            texty2.draw(win)
            time.sleep(.05)
            texty2.undraw()         
        texty2.draw(win)
        time.sleep(.2)
        yesBox.draw(win)
        noBox.draw(win)
        yesText.draw(win)
        noText.draw(win)
        answer= "fuck"
        validClick = False
        while validClick == False:
            click1 = win.getMouse()
            if (click1.getX() >= yesClick[0][0] and click1.getX() <=yesClick[0][1]) and (click1.getY() >= yesClick[1][0] and click1.getY() <=yesClick[1][1]):
                answer = "y"
                validClick = True
            if (click1.getX() >= noClick[0][0] and click1.getX() <=noClick[0][1]) and (click1.getY() >= noClick[1][0] and click1.getY() <=noClick[1][1]):
                answer = "n"
                validClick = True

        time.sleep(.2)
        texty.undraw()
        texty2.undraw()
        yesBox.undraw()
        noBox.undraw()
        yesText.undraw()
        noText.undraw()
        sean.incrementFuck(answer)
        sean.incrementDidRun()

##############we have the answer here
        message = sean.seanResponse(answer)
        if answer == "y":
            yep = "you play for a hot minute. He's not the best player but he's good......"
            for i in range(len(yep)):
                display = yep[:i+1]
                texty = Text(Point(width*.5, height*.7), display)
                texty.draw(win)
                time.sleep(.06)
                texty.undraw()
            texty.draw(win)
            time.sleep(.7)
            texty.undraw()
            for i in range(len(message)):
                display = message[:i+1]
                texty = Text(Point(width*.5, height*.7), display)
                texty.draw(win)
                time.sleep(.04)
                texty.undraw()
            texty.draw(win)
        if answer == "n":
            for i in range(len(message)):
                display = message[:i+1]
                texty = Text(Point(width*.5, height*.7), display)
                texty.draw(win)
                time.sleep(.04)
                texty.undraw()
            texty.draw(win)
        if sean.getFuck() == 1:
            time.sleep(1)
            win.close()
        else:
            time.sleep(1)
            texty.undraw()

            for i in range(len(msgs1)):
                display = msgs1[:i]
                texty = Text(Point(width*.5, height*.7), display)
                texty.draw(win)
                time.sleep(.05)
                texty.undraw()
            texty.draw(win)
            time.sleep(.5)
            for i in range(len(msgs2)):
                display = msgs2[:i]
                texty2 = Text(Point(width*.5, height*.75), display)
                texty2.draw(win)
                time.sleep(.05)
                texty2.undraw()
            texty2.draw(win)
            time.sleep(.5)
            texty.undraw()
            texty2.undraw()
            for i in range(len(msgs3)):
                display = msgs3[:i]
                texty = Text(Point(width*.5, height*.7), display)
                texty.draw(win)
                time.sleep(.05)
                texty.undraw()
            texty.draw(win)
            time.sleep(.5)
            for i in range(len(msgs4)):
                display = msgs4[:i]
                texty2 = Text(Point(width*.5, height*.75), display)
                texty2.draw(win)
                time.sleep(.05)
                texty2.undraw()
            texty2.draw(win)
            time.sleep(.5)
            for i in range(len(msgs5)):
                display = msgs5[:i]
                texty3 = Text(Point(width*.5, height*.8), display)
                texty3.draw(win)
                time.sleep(.05)
                texty3.undraw()
            texty3.draw(win)
            time.sleep(.5)
            texty.undraw()
            texty2.undraw()
            texty3.undraw()
            for i in range(len(msgs6)):
                display = msgs6[:i]
                texty = Text(Point(width*.5, height*.7), display)
                texty.draw(win)
                time.sleep(.05)
                texty.undraw()
            texty.draw(win)
            time.sleep(.5)
            for i in range(len(msgs7)):
                display = msgs7[:i]
                texty2 = Text(Point(width*.5, height*.75), display)
                texty2.draw(win)
                time.sleep(.05)
                texty2.undraw()
            texty2.draw(win)
            time.sleep(.5)
            for i in range(len(msgs8)):
                display = msgs8[:i]
                texty3 = Text(Point(width*.5, height*.8), display)
                texty3.draw(win)
                time.sleep(.05)
                texty3.undraw()
            texty3.draw(win)
            time.sleep(.5)
            texty.undraw()
            texty2.undraw()
            texty3.undraw()
            newtext = Text(Point(width*.5,height*.95), "click to close u dirty hoe")
            newtext.draw(win)
            win.getMouse()
            win.close()
        time.sleep(.5)
        texty.undraw()
        seanFace.undraw()
        

        
        
        
            
       
        win.getMouse()
    playAgain = True
playGame()

















   
