class Robot:
    def __init__(self, _m, _b):
        self.M = _m
        self.b = _b
        # variabili di stato, p = posizione, v = velocita'
        self.p = 0
        self.posPrec = 0
        self.v = 0

    def evaluate(self, _input, dt):
        self.posPrec = self.p
        self.p = self.p + dt * self.v
        self.v = self.v - (self.b/self.M) * dt * self.v + (1/self.M) * dt * _input

    def get_position(self):
        return self.p

    def get_velocity(self):
        return self.v

    def get_positionPrec(self):
        return self.posPrec