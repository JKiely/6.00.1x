def f(x):
    import math
    return 200*math.e**(math.log(0.5)/14.1 * x)
    
def radiationExposure(start, stop, step):
    counter = 0
    while stop > start:
        counter += step*f(start)
        start += step
    return counter
    
print radiationExposure(72, 96, 0.4)
