import math


class Odometry:
    def __init__(self, B, DX, SX):
        self.MotoreDx = DX
        self.MotoreSx = SX
        self.B = B
        self.Teta = 0
        self.x = 0
        self.y = 0
        self.distanza_percorsa = 0

    def evaluate(self):
        deltaPosSx = self.MotoreSx.p - self.MotoreSx.posPrec
        deltaPosDx = self.MotoreDx.p - self.MotoreDx.posPrec
        self.distanza_percorsa += (deltaPosSx + deltaPosDx) / 2
        deltaTeta = (deltaPosDx - deltaPosSx) / self.B
        self.x = self.x + (((deltaPosSx + deltaPosDx) / 2) * math.cos(self.Teta + (deltaTeta / 2)))
        self.y = self.y + (((deltaPosSx + deltaPosDx) / 2) * math.sin(self.Teta + (deltaTeta / 2)))
        self.Teta = self.Teta + deltaTeta

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getTeta(self):
        return self.Teta

    def getDistanzaPercorsa(self):
        return self.distanza_percorsa