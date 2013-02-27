
#p = 5308922457110321261057523600918219961102029940834952660375258153133757782910797976368016872868661777L
#q = 3640402828197845577377284881591582881844271142707316676943175370086142033126044534587529830250247689L


class RsaEncryptor(object):
        
    def __init__(self, p, q):
        self.publickey, self.privatekey = self.generateRSAKeys(p, q)
        print "Public Key (n, e) =", self.publickey
        print "Private Key (n, d) =", self.privatekey, "\n"

    def generateRSAKeys(self, p, q):
        "Generate RSA Public and Private Keys from prime numbers p & q"
        print "Generating public and private keys...."

        n = p * q
        m = (p - 1) * (q - 1)
        
        print "p =", p, "\n"
        print "q =", q, "\n"
        print "n =", n, "\n"
        print "m =", m, "\n"
        
        # Generate a number e so that gcd(n, e) = 1, start with e = 3
        e = 3
        
        while 1:
            if gcd(m, e) == 1: break
            else: e = e + 2
        
        # start with a number d = m/e will be atleast 1
        d = multiplicative_inverse(m, e)
        
        print "e =", e, "\n"
        print "d =", d, "\n"
                
        # Return a tuple of public and private keys
        return ((n,e), (n,d))
    
    def encryptMessage(self, message):
        n, e = self.publickey

        numericalPad = ""
        for p in message:
            digit = get_number_from_char(p)
            numericalPad += str(digit) if digit > 9 else "0" + str(digit)

        encryptedString = ""
        for i in range(0, len(numericalPad), 100):
            tempPad = numericalPad[i:i+100]
            encrypted_num = pow(long(tempPad), e, n)
            paddingLen = len(str(n)) - len(str(encrypted_num))
            padding = ''.join(["0" for num in range(paddingLen)])
            encryptedString += padding
            encryptedString += str(encrypted_num)

        return encryptedString

    
    def decryptMessage(self, message):
        n, d = self.privatekey

        decryptedString = ""
        for i in range(0, len(message), len(str(n))):
            decrypted_num = pow(long(message[i:i+len(str(n))]), d, n)
            tempDecrypt = str(decrypted_num)
            paddingLen = 100 - len(str(tempDecrypt))
            padding = ''.join(["0" for num in range(paddingLen)])
            tempDecrypt = padding + tempDecrypt
            
            for j in range(0, len(tempDecrypt), 2):
                x = int(tempDecrypt[j:j+2])
                decryptedString += get_char_from_number(x)
        
        return decryptedString


def get_number_from_char(c):

    ord_c = ord(c)

    if ord_c >= ord('A') and ord_c <= ord('Z'):
        return ord_c - ord('A')
    elif c == ' ': # This is a space
        return 26
    elif c == '.':
        return 27
    elif c == ',':
        return 28
    elif c == '\'':
        return 29
    else:
        return 30


def get_char_from_number(n):

    ord_a = ord('A')

    if n >= 0 and n <= 25:
        return chr(n + ord_a)
    elif n == 26:
        return ' ' # This is a space
    elif n == 27:
        return '.'
    elif n == 28:
        return ','
    elif n == 29:
        return '\''
    else:
        return '*'

def gcd (a, b):
    "Compute GCD of two numbers"
    if b == 0: return a
    else: return gcd(b, a % b)

def multiplicative_inverse(a, b):
    """ Find multiplicative inverse of a modulo b (a > b)
        using Extended Euclidean Algorithm """
    origA = a
    X = 0
    prevX = 1
    Y = 1
    prevY = 0
    
    while b != 0:
        temp = b
        quotient = a/b
        b = a % b
        a = temp
        
        temp = X
        a = prevX - quotient * X
        prevX = temp
        
        temp = Y
        Y = prevY - quotient * Y
        prevY = temp
    
    return origA + prevY

if __name__ == "__main__":

    print "RSA Encryption algorithm...."

    p = 5308922457110321261057523600918219961102029940834952660375258153133757782910797976368016872868661777L
    q = 3640402828197845577377284881591582881844271142707316676943175370086142033126044534587529830250247689L
    
    rsa = RsaEncryptor(p, q)

    oneTimePad = "Do not go gentle into that good night, Old age should burn and rave at close of day; Rage, rage against the dying of the light. Though wise men at their end know dark is right, Because their words had forked no lightning they Do not go gentle into that good night."
    
    oneTimePad = oneTimePad[0:200].upper()
    print "One-time pad =", oneTimePad + "\n"
    
    encryptedString = rsa.encryptMessage(oneTimePad)
    print "Encrypted pad =", encryptedString, "\n"

    decryptedString = rsa.decryptMessage(encryptedString)

    print "Decrypted pad =", decryptedString + "\n"
