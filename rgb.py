import pulseio

r = 0
g = 0
b = 0

class RGB:

    full = 65535

    def __init__(self, r, g, b):
        print(str(r))
        self.r = pulseio.PWMOut(r, frequency=5000, duty_cycle=0)
        self.g = pulseio.PWMOut(g, frequency=5000, duty_cycle=0)
        self.b = pulseio.PWMOut(b, frequency=5000, duty_cycle=0)

    def red(self):
        self.r.duty_cycle = 0
        self.g.duty_cycle = self.full
        self.b.duty_cycle = self.full

    def blue(self):
        self.r.duty_cycle = self.full
        self.g.duty_cycle = self.full
        self.b.duty_cycle = 0

    def green(self):
        self.r.duty_cycle = self.full
        self.g.duty_cycle = 0
        self.b.duty_cycle = self.full

    def cyan(self):
        self.r.duty_cycle = self.full
        self.g.duty_cycle = 0
        self.b.duty_cycle = 0

    def magenta(self):
        self.r.duty_cycle = 0
        self.g.duty_cycle = self.full
        self.b.duty_cycle = 0

    def yellow(self):
        self.r.duty_cycle = 0
        self.g.duty_cycle = 0
        self.b.duty_cycle = self.full