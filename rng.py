import math


a = 24693
c = 3517
K = 2**15
x_0 = 1000
x = x_0

def next():
    global x, a, c, K, x_0
    x = int((a * x + c) % K)
    return x /K
    #generate next random number

    # int cast to prevent accumulated floating point errors
    # linear congruential RNG
def reset():
    global x, x_0
    x = x_0

def many(n):
        #'''reset RNG, then return a list of the next n random numbers'''
        reset()
        return [next() for i in range(n)]


print(next(), next(), next())  # first 3: 0.6779, 0.1701, 0.5096
first100 = many(100)
print(first100[50:53])  # 51st, 52nd, and 53rd go in report


def generate_next_X():
    u = next()
    return X_invcdf(u)


def X_invcdf(u):
    if u < 0 or u > 1:
        raise ValueError
    return -12*math.log(1-u)
