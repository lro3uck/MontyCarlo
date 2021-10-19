import math


class RNG:

    def __init__(self):
        self.a = 24693
        self.c = 3517
        self.K = 2**15
        self.x_0 = 1000
        self.x = self.x_0

    def next(self):
        '''generate next random number'''
        # int cast to prevent accumulated floating point errors
        # linear congruential RNG
        self.x = int((self.a * self.x + self.c) % self.K)
        return self.x / self.K

    def reset(self):
        '''reset seed of RNG'''
        self.x = self.x_0

    def many(self, n):
        '''reset RNG, then return a list of the next n random numbers'''
        self.reset()
        return [self.next() for i in range(n)]


rng = RNG()
print(rng.next(), rng.next(), rng.next())  # first 3: 0.6779, 0.1701, 0.5096
first100 = rng.many(100)
print(first100[50:53])  # 51st, 52nd, and 53rd go in report


def generate_next_X():
    u = rng.next()
    return X_invcdf(u)


def X_invcdf(u):
    if u < 0 or u > 1:
        raise ValueError
    return -12*math.log(1-u)
