from bin import *

class DateManager:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

    def NewMonth(self):
        Date.day = 1
        Date.month += 1
        if Date.month == 13:
            Date.month = 1
            Date.year += 1

            ev = NewYearEvent()
            self.evManager.Post(ev)

        ev = NewMonthEvent()
        self.evManager.Post(ev)

    def LeapYear(self):
        if Date.year % 4 == 0:
            return True

    def Notify(self, event):
        if isinstance(event, NewDayEvent):
            Date.day += 1
            Date.dayNumber += 1

            if Date.day == 29:
                if Date.month == 2 and not self.LeapYear():
                    self.NewMonth()
            elif Date.day == 30:
                if Date.month == 2:
                    self.NewMonth()
            elif Date.day == 31:
                if Date.month in [4, 6, 9, 11]:
                    self.NewMonth()
            elif Date.day == 32:
                self.NewMonth()

            print(Date.day, Date.month, Date.year)
