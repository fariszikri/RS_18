from bin import *
import math
import random

class UpgradesManager: #values are called when even is requested
    def __init__(self, evManager):
        self.evManager = evManager

    def UpgradeLevel(self, level):  # initial LEVEL is 0
        newLevel = level + 1
        return newLevel

    def UpgradeLevelCost(self, level, capacity):
        cost = 40000 * 2.8 * level**2 *(capacity/50)
        return cost

    def UpgradeCapacity(self, capacity):
        newCapacity = capacity * 2
        return newCapacity

    def UpgradeCapacityCost(self, level, capacity):
        if level > 0:
            cost = 20000 * 1.5 * (level)**2
        return newCapacityCost

