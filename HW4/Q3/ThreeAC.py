from antlr4 import *
from HW4.gen.Q2Listener import Q2Listener


class ThreeACListener(Q2Listener):
    def __init__(self):
        self.TempCount = 0
        self.LabelCount = 0


    def CreateTemp(self):
        self.TempCount += 1
        return 'T' + str(self.TempCount)

    def CreateLabel(self):
        self.LabelCount += 1
        return 'L' + str(self.LabelCount)



