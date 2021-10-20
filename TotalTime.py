import rng
import matplotlib.pyplot as plt
W = 0
dial = 4.33
busy = 3
rings = 26.33
end = 1
def call():
    time = dial
    pickedup = False
    p = rng.next()
    if p <= .2:
        time += busy
        time += end
    elif p > .2 and p <= .5:
        time += rings
        time += end
    else:
        x = rng.generate_next_X()
        if x <= rings:
            time += x
            pickedup = True
        else:
            time += rings
            time += end
    return time, pickedup

def trial():
    total = 0
    for i in range(4):
        t, finished = call()
        total += t
        if finished:
            break
    return total
def severalruns(n):
    times = []
    for i in range(n):
        times.append(trial())
    return times
def calcAverage(Ws):
    return sum(Ws)/len(Ws)
def median(Ws):
    return (Ws[(len(Ws)-1)//2]+Ws[(len(Ws))//2])/2
def quartiles(Ws):
    Ws = sorted(Ws)
    m=median(Ws)
    f=median(Ws[0:(len(Ws)+1)//2])
    t=median(Ws[len(Ws)//2:len(Ws)])
    return f, m, t
def approxCDF(Ws, w):
    return sum([1 if W<w else 0 for W in Ws])/len(Ws)

Ws = severalruns(1000)
print(calcAverage(Ws))
print(quartiles(Ws))
print(approxCDF(Ws, 15))
print(approxCDF(Ws, 20))
print(approxCDF(Ws, 30))
print(1-approxCDF(Ws, 40))
print(1-approxCDF(Ws, 50))
print(1-approxCDF(Ws, 70))
print(1-approxCDF(Ws, 90))
xcoords = [x for x in range(0, 128)]
ycoords = [approxCDF(Ws, x) for x in xcoords]
#xcoords = [15,20, 30, 40, 50, 70, 90, 100, 130]
#ycoords = [approxCDF(Ws, 15), approxCDF(Ws, 20), approxCDF(Ws, 30), approxCDF(Ws, 40), approxCDF(Ws, 50), approxCDF(Ws, 70), approxCDF(Ws, 90), approxCDF(Ws, 100),approxCDF(Ws, 130)]
plt.plot(xcoords, ycoords)
plt.show()