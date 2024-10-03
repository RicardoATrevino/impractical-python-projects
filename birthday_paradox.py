import datetime, random

def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays"""
    birthdays = []
    
    for i in range(numberOfBirthdays):
        #year unimportant assuming everyone is born in the same year
        startOfYear = datetime.date(2001,1,1)
        #get random day of year
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
        

def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once in the birthdays list"""
    if len(birthdays) == len(set(birthdays)):
        return None