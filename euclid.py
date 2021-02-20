#ohamilton79
#Euclidean Algorithm
#15/01/2020

def euclid(a, b):
    #BASE CASE - If b is 0, the gcd is a
    if b == 0:
        return a

    #Recursive step - apply Division lemma repeatedly to get GCD
    gcd = euclid(b, a % b)

    return gcd

