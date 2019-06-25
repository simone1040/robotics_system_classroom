class G1:
    def __init__(self):
        self.x1 = 0
        self.x2 = 0

    def evaluate(self,u,delta_t):
        temp_x1 = self.x1
        self.x1 = temp_x1 + self.x2 * delta_t
        self.x2 = self.x2 - 4*temp_x1*delta_t - 3*self.x2 * delta_t + 2 * delta_t * u
        return temp_x1



class G2:
    def __init__(self):
        self.y = 0

    def evaluate(self,u,delta_t):
        temp_y = self.y
        self.y = self.y - 0.5 * delta_t *self.y + 4 * delta_t * u
        return temp_y



class System:
    def __init__(self):
        self.g1 = G1()
        self.g2 = G2()
        self.y = 0

    def evaluate(self,u,delta_t):
        self.y = self.g2.evaluate(self.g1.evaluate(u,delta_t),delta_t)
        return self.y