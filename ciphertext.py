

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

def generateRSAKeys(p, q):
    "Generate RSA Public and Private Keys from prime numbers p & q"
    
    n = p * q
    m = (p - 1) * (q - 1)
    
    print "p = ", p, "\n"
    print "q = ", q, "\n"
    print "n = ", n, "\n"
    print "m = ", m, "\n"
    
    # Generate a number e so that gcd(n, e) = 1, start with e = 3
    e = 3
    
    while 1:
        
        if gcd(m, e) == 1: break
        else: e = e + 2
    
    # start with a number d = m/e will be atleast 1
    
    d = multiplicative_inverse(m, e)
    
    print "e = ", e, "\n"
    print "d = ", d, "\n"
            
    # Return a tuple of public and private keys
    return ((n,e), (n,d))

def pendulum(s):
    """Given abcd yields abcdcbabcdc... """
    while True:
        for p in s: yield p
        for p in reversed(s[1:-1]): yield p


def vigenere(text, key, mode='encode'):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alphabet.upper()
    key = pendulum(key)
    encoded = ''
    
    for char in text:
        index = alphabet.index(char)
        offset = alphabet.index(next(key))
        
        if mode == 'encode':
            shifted = index + offset
        else:
            shifted = index - offset
        
        encoded += alphabet[shifted % len(alphabet)]
    return encoded

if __name__ == "__main__":

    print "RSA Encryption algorithm...."

    p = 5308922457110321261057523600918219961102029940834952660375258153133757782910797976368016872868661777L
    q = 3640402828197845577377284881591582881844271142707316676943175370086142033126044534587529830250247689L

    print "Generating public and private keys...."
    (publickey, privatekey) = generateRSAKeys(p, q)
    
    print "Public Key (n, e) =", publickey
    print "Private Key (n, d) =", privatekey
    
    n, e = publickey
    n, d = privatekey
    oneTimePad = "Do not go gentle into that good night, Old age should burn and rave at close of day; Rage, rage against the dying of the light. Though wise men at their end know dark is right, Because their words had forked no lightning they Do not go gentle into that good night."
    
    oneTimePad = (''.join(e for e in oneTimePad if e.isalnum())).upper()
    oneTimePad = oneTimePad[0:200]
    
    message = "The thousand injuries of Fortunato I had borne as I best could, but when he ventured upon insult I vowed revenge. You, who so well know the nature of my soul, will not suppose, however, that gave utterance to a threat. At length I would be avenged; this was a point definitely, settled --but the very definitiveness with which it was resolved precluded the idea of risk. I must not only punish but punish with impunity. A wrong is unredressed when retribution overtakes its redresser. It is equally unredressed when the avenger fails to make himself felt as such to him who has done the wrong. It must be understood that neither by word nor deed had I given Fortunato cause to doubt my good will. I continued, as was my in to smile in his face, and he did not perceive that my to smile now was at the thought of his immolation. He had a weak point --this Fortunato --although in other regards he was a man to be respected and even feared. He prided himself on his connoisseurship in wine. askjksdjfkjskfsdfhhh."


    message = (''.join(e for e in message if e.isalnum())).upper()
    message = message[0:800]
    print message, len(message)
    
    encode = vigenere(message, oneTimePad, mode='encode')
    print encode, len(encode)
    
    #print str(n), len(str(n))
    
    encryptedString = ""

    ascii_shift = ord('A')
    for i in range(0, len(oneTimePad), 100):
        tempPad = ""
        for m in oneTimePad[i:i+100]:
            digit = ord(m) - ascii_shift
            tempPad += str(digit) if digit > 9 else "0" + str(digit)
    
        encrypted_num = pow(long(tempPad), e, n)
        paddingLen = len(str(n)) - len(str(encrypted_num))
        padding = ''.join(["0" for num in range(paddingLen)])
        encryptedString += padding
        encryptedString += str(encrypted_num)

    print encryptedString

    decryptedString = ""
    for i in range(0, len(encryptedString), len(str(n))):
        decrypted_num = pow(long(encryptedString[i:i+len(str(n))]), d, n)
        tempDecrypt = str(decrypted_num)
        paddingLen = 200 - len(str(tempDecrypt))
        padding = ''.join(["0" for num in range(paddingLen)])
        tempDecrypt = padding + tempDecrypt
        
        for j in range(0, len(tempDecrypt), 2):
            x = int(tempDecrypt[j:j+2])
            char = chr(x + ascii_shift)
            decryptedString += char

    print decryptedString
