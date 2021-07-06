from datetime import datetime

class timeFunc:

    @staticmethod
    # Fri Apr  2 14:39:41 2021

    def getTimeWithFormat():
        now = datetime.now()
        timeWithFormat = now.strftime("%a %b  %d %H:%M:%S %Y")
        return timeWithFormat