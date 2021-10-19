
a = 24693
c = 3517
K = 2**15
x_0 = 1000
x = x_0

def next():
    global a
    global c
    global K
    global x_0
    global x
    x = int((a * x + c) % K)
    return x / K
        #'''generate next random number'''
        # int cast to prevent accumulated floating point errors
        # linear congruential RNG

def reset(self):
        '''reset seed of RNG'''
        global x, x_0
        x = x_0

def many(self, n):
        '''reset RNG, then return a list of the next n random numbers'''
        reset()
        return [next() for i in range(n)]


rng = RNG()
print(rng.next(), rng.next(), rng.next())  # first 3: 0.6779, 0.1701, 0.5096
first100 = rng.many(100)
print(first100[50:53])  # 51st, 52nd, and 53rd go in report
