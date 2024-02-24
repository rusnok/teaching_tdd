class Pavel:
    def __init__(self, a):
        self.a = a

    def increase(self):
        return self.a + 1


class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self, reverse=False):
        if reverse:
            return self.b - self.a
        else:
            return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self, reverse=False):
        if reverse:
            return self.b / self.a
        else:
            return self.a / self.b
