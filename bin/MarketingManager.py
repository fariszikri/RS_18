class MarketingManager:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

    def MarketingModifier(self):


        return modifier

    def Notify(self, event):
        pass


class MarketingBonus:
    def __init__(self, name, modifier, cost, duration, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)
        self.name = name
        self.modifier = modifier
        self.cost = cost
        self.duration = duration
        self.dayPassed = 0


    def Notify(self, event):
        if isinstance(event, NewDayEvent):
            Marketing

#everytime newdayevent + 1
# day passed > duration = kill

ev = MarketingBonusExpiredEvent(self)
self.evManager.Post(ev)

Marketing
1. Social Media
2. Banners and Posters
3. Billboards
4. TV Ads

cost for every advertisement and how long they hold