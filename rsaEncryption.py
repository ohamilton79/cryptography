#ohamilton79
#RSA Simulator
#15/01/2020
from extEuclid import extEuclid
from euclid import euclid
from random import randint

#Encrypt a message
def encrypt(plaintext, N, e):
    print("Plaintext input: '{}'".format(plaintext))
    #Convert plaintext to ascii codes string
    codeString = ""
    for character in plaintext:
        codeString += str(ord(character)) + "001"   #'001' acts as a separator between codes
    #print(codeString)
    codeInt = int(codeString)

    #Calculate ciphertext according to formula (codeSum)^e mod N
    print("Encrypting using Alice's public key...")
    ciphertext = pow(codeInt, e, N)
    print("Ciphertext: {}".format(ciphertext))
    #Return ciphertext
    return ciphertext

#Decrypt a message
def decrypt(ciphertext, p, q, N, e):
    #Get decryption key by extended Euclidean algorithm
    gcd, x, decryptionKey = extEuclid((p - 1) * (q - 1), e)

    #Get code integer once decrypted using formula (ciphertext)^d mod N
    print("Decrypting using Alice's private key...")
    codeInt = pow(ciphertext, decryptionKey, N)

    #Translate back to ASCII characters
    codeString = str(codeInt)
    charCodes = codeString.split("001")
    
    message = ""
    for charCode in charCodes:
        #if the character code isn't an empty string, append the character to the message
        if charCode != '':
            message += chr(int(charCode))

    #Return the unencrypted message
    print("Decrypted message: '{}'".format(message))
    return message

#Calculate 2 large prime numbers
p = 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151
q = 531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127

#(p-1)(q-1) and e should be relatively prime (gcd of 1)
e = randint(1, (p-1)*(q-1))
while euclid((p-1)*(q-1), e) != 1:
    e = randint(1, (p-1)*(q-1))
    
N = p * q

plaintext = "Hello Alice my name is Bob."
ciphertext = encrypt(plaintext, N, e)
decrypted = decrypt(ciphertext, p, q, N, e)
    
    


    
