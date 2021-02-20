#ohamilton79
#Extended Euclidean Algorithm
#15/01/2020

def extEuclid(a, b):
    #Base case
    if b == 0:
        x = 1
        y = 0
        return a, x, y

    #Recursive step
    gcd, x1, y1 = extEuclid(b, a % b)
    #Update values of x and y based on recursive calls
    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y
    
