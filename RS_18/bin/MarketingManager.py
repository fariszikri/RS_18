from bin import *
import configparser
import copy



class MarketingManager:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)


        # Load list of marketing strats
        config = configparser.ConfigParser()
        config.read("data/marketing.rs")
        for section in config.sections():
            name = str(config.get(section, "name"))
            modifier = config.getfloat(section, "modifier")
            tier = str(config.get(section, "tier"))
            cost = config.getint(section, "cost")
            duration = config.getint(section, "duration")

            MARKETING_LIST.append(MarketingBonus(name, modifier, tier, cost, duration, self.evManager))

#
#return value total bonus
#list of marketing player owns
    def MarketingModifier(self, list):
        modifier = 0
        for bonus in list:
            modifier += bonus.modifier

        return modifier

    def Notify(self, event):
        pass


class MarketingBonus:
    def __init__(self, name, modifier, tier, cost, duration, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)
        self.name = name
        self.modifier = modifier
        self.cost = cost
        self.duration = duration
        self.dayPassed = 0


    def Notify(self, event):
        if isinstance(event, NewDayEvent):
            self.dayPassed += 1 # if duration is 7
            if self.dayPassed == duration:
                ev = MarketingBonusExpiredEvent(self)
                self.evManager.Post(ev)


#everytime newdayevent + 1
# day passed > duration = kill


