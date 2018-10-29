class TimeSpan:
    def __init__(self, seconds, minutes = 0, hours = 0):
        self.setTime(seconds, minutes, hours)

    def getHours(self):
        return self.__hours

    def getMinutes(self):
        return self.__minutes
    
    def getSeconds(self): 
        return self.__seconds
    
    def setTime(self, seconds, minutes, hours):
        totalSeconds = seconds + minutes * 60 + hours * 3600
        if (totalSeconds >= 0):
            self.__hours = int(totalSeconds // 3600)
            self.__minutes = int((totalSeconds % 3600) // 60)
            self.__seconds = int(((totalSeconds % 3600) % 60) // 1)
        else: 
            self.__hours = int(-1 * ((-1 * totalSeconds) // 3600))
            self.__minutes = int(-1 * (((-1 * totalSeconds) % 3600) // 60))
            self.__seconds = int(-1 * ((((-1 * totalSeconds) % 3600) % 60) // 1))

    def __str__(self):
        return "Hours: " + str(self.__hours) + ", Minutes: " + str(self.__minutes) + ", Seconds: " + str(self.__seconds)
        
    def __add__(self, other):
        sumTime = TimeSpan(self.__seconds + other.getSeconds(), self.__minutes + other.getMinutes(), self.__hours + other.getHours())
        return sumTime

    def __sub__(self, other):
        resultTime = TimeSpan(self.__seconds - other.getSeconds(), self.__minutes - other.getMinutes(), self.__hours - other.getHours())
        return resultTime

    def __neg__(self):
        return TimeSpan(self.__seconds * -1, self.__minutes * -1, self.__hours * -1)

    def __eq__(self, other):
        if self.__hours == other.getHours() and self.__minutes == other.getMinutes() and self.__seconds == other.getSeconds():
            return True
        else: 
            return False

    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True
    
    def __lt__(self, other):
        totalSecSelf = self.__seconds + self.__minutes * 60 + self.__hours * 3600
        totalSecOther = other.getSeconds() + other.getMinutes() * 60 + other.getHours() * 3600
        if totalSecSelf < totalSecOther:
            return True
        else:
            return False

    def __le__(self, other):
        if self == other or self < other:
            return True
        else: 
            return False

    def __gt__(self, other):
        if other < self:
            return True 
        else:
            return False

    def __ge__(self, other):
        if self > other or self == other:
            return True
        else:
            return False


    