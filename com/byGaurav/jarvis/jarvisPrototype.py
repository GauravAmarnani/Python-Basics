import pyttsx3
import datetime

engine = pyttsx3.init()


def speakJarvis(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    myTime = datetime.datetime.now().strftime("%I:%M:%S")
    speakJarvis(myTime)


def giveMonthName(monthNumber):
    if monthNumber == 1:
        return "January"
    elif monthNumber == 2:
        return "February"
    elif monthNumber == 3:
        return "March"
    elif monthNumber == 4:
        return "April"
    elif monthNumber == 5:
        return "May"
    elif monthNumber == 6:
        return "June"
    elif monthNumber == 7:
        return "July"
    elif monthNumber == 8:
        return "August"
    elif monthNumber == 9:
        return "September"
    elif monthNumber == 10:
        return "October"
    elif monthNumber == 11:
        return "November"
    elif monthNumber == 12:
        return "December"


def date():
    myYear = datetime.datetime.now().year
    myMonth = giveMonthName(datetime.datetime.now().month)
    myDay = datetime.datetime.now().day
    myDate = ("Today's date is ", myDay, " of month ", myMonth, " and year ", myYear)
    speakJarvis(myDate)


speakJarvis("Jarvis at your service sir, How may I assist you?")
time()
date()
