import math
class Controllore_Proporzionale:

    def __init__(self,KP):
        self.KP = KP

    def evaluate(self,target,measure):
        self.error = self.KP * (target - measure)
        return self.error

    def get_error(self):
        return self.error


class ControlloreProporzionaleSat:
    def __init__(self,KP,sat):
        self.KP = KP
        self.sat = sat


    def evaluate(self,target,measure):
        self.error = self.KP * (target - measure)
        if self.error > self.sat:
            self.error = self.sat
        elif self.error < -self.sat:
            self.error = -self.sat
        return self.error

    def get_error(self):
        return self.error

    def evaluateErrorPos(self, xrobot, yrobot, xtarget, ytarget):
        self.__error = math.sqrt((xtarget - xrobot) ** 2 + (ytarget - yrobot) ** 2)
        output = self.__error * self.KP
        if output > self.sat:
            output = self.sat
        if output < -self.sat:
            output = -self.sat
        return (output, self.__error)


class ControlloreProporzionaleIntegrale:
    def __init__(self,kp,ki):
        self.ki = ki
        self.kp = kp
        self.integral = 0

    def evaluate(self,target,current,delta_t):
        error = target - current
        self.integral = self.integral + error * delta_t
        output = self.kp * error + self.ki * self.integral
        return output

#Questo introduce anche il concetto di anti-widup, ovvero quando il sistema è in saturazione non andiamo ad accumulare
#l'errore che non sarà mai ridotto.Quindi non calcoliamo l'integrale
class ControlloreProporzionaleIntegraleSat:
    def __init__(self,kp,ki,sat):
        self.ki = ki
        self.kp = kp
        self.sat = sat
        self.saturationFlag = False
        self.integral = 0

    def evaluate(self,target,current,delta_t):
        error = target - current
        if(not(self.saturationFlag)):
            self.integral = self.integral + error * delta_t
        output = self.kp * error + self.ki * self.integral
        if(output > self.sat):
            output = self.sat
            self.saturationFlag = True
        elif(output < -self.sat):
            output = -self.sat
            self.saturationFlag = True
        else:
            self.saturationFlag = False
        return output