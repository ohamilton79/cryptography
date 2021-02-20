#ohamilton79
#Diffie-Hellman-Merkle key exchange
#15/01/2021

class Person:

    #Stores the public key of the other person
    __publicKey = None
    #Stores the final encryption key
    __privateKey = None

    #Getters and setters for public key
    def getPublicKey(self):
        return self.__publicKey

    def setPublicKey(self, newPublicKey):
        self.__publicKey = newPublicKey
    
    #Initialise class with private number for use in encryption, as well as the name of the person and function parameters
    def __init__(self, name, p, Y, N):
        self.name = name
        self.__p = p
        self.Y = Y
        self.N = N

    #Calculate the public key for this private number
    def calculatePublicKey(self):
        print("Calculating public key for {}...".format(self.name))
        #Perform Y^p mod N
        self.__publicKey = pow(self.Y, self.__p, self.N)
        print("Public key for {}: {}".format(self.name, self.__publicKey))

    #Calculate the private key for this user
    def calculatePrivateKey(self):
        print("Calculating private key for {}...".format(self.name))
        #Perform (public key)^p mod N
        self.__privateKey = pow(self.getPublicKey(), self.__p, self.N)

        print("Private key for {}: {}".format(self.name, self.__privateKey))

#Function parameters
Y = 3
#N is a large prime number
N = 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151

#Create 2 people - Alice and Bob - who want to share a symmetric key
alice = Person("Alice", 7362, Y, N)
bob = Person("Bob", 2245, Y, N)

#Calculate public keys for each
alice.calculatePublicKey()
bob.calculatePublicKey()

#Exchange public keys
print("Exchanging public keys...")
temp = alice.getPublicKey()
alice.setPublicKey(bob.getPublicKey())
bob.setPublicKey(temp)

#Calculate private keys for each
alice.calculatePrivateKey()
bob.calculatePrivateKey()
