

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


def vigenere(text, key, mode='encode'):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .,\'*'
    encoded = ''
    
    for i in range(len(text)):
        try:
            index = alphabet.index(text[i])
        except:
            index = 30

        try:
            offset = alphabet.index(key[i % len(key)])
        except:
            offset = 30
            
        if mode == 'encode':
            shifted = index + offset
        else:
            shifted = index - offset
            
        encoded += alphabet[shifted % len(alphabet)]

    return encoded

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

if __name__ == "__main__":

    print "RSA Encryption algorithm...."

    p = 5308922457110321261057523600918219961102029940834952660375258153133757782910797976368016872868661777L
    q = 3640402828197845577377284881591582881844271142707316676943175370086142033126044534587529830250247689L

    print "Generating public and private keys...."
    (publickey, privatekey) = generateRSAKeys(p, q)
    
    print "Public Key (n, e) =", publickey
    print "Private Key (n, d) =", privatekey, "\n"
    
    n, e = publickey
    n, d = privatekey
    oneTimePad = "Do not go gentle into that good night, Old age should burn and rave at close of day; Rage, rage against the dying of the light. Though wise men at their end know dark is right, Because their words had forked no lightning they Do not go gentle into that good night."
    
    oneTimePad = oneTimePad[0:200].upper()
    print "One-time pad =", oneTimePad + "\n"
    
    message = "The thousand injuries of Fortunato I had borne as I best could, but when he ventured upon insult I vowed revenge. You, who so well know the nature of my soul, will not suppose, however, that gave utterance to a threat. At length I would be avenged; this was a point definitely, settled - but the very definitiveness with which it was resolved precluded the idea of risk. I must not only punish but punish with impunity. A wrong is unredressed when retribution overtakes its redresser. It is equally unredressed when the avenger fails to make himself felt as such to him who has done the wrong. It must be understood that neither by word nor deed had I given Fortunato cause to doubt my good will. I continued, as was my in to smile in his face, and he did not perceive that my to smile now was at the thought of his immolation. He had a weak point - this Fortunato - although in other regards he was a man to be respected and even feared. He prided himself on his connoisseurship in wine. askjksdjfkjskfsdfhhh."

    message = message[0:800].upper()
    print "Message =", message + "\n"
    
    encode = vigenere(message, oneTimePad, mode='encode')
    print "Encoded message =", encode + "\n"
    
    ascii_shift = ord('A')
    numericalPad = ""
    for p in oneTimePad:
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

    print "Encrypted pad =", encryptedString, "\n"
#encryptedString = "63019279398296315384495075416116008504013644904906832663217575165699797501337338546345034400652009328801820351565432235036502619467459726799203925179240840962369619311519186226062060060221488343402978866370514327330049870078665306457720785135644407426693651311028000243174876597508899264702122417597171022086222141404241773938873152083936919522197288445032585764991075206864774095160693720934242044054361559125738900790133241814969967759701823998689606332626384436165212509849693845096560325437238728465073074221349220791127337466032337377328293391559641081634385429526728784517729809891892667247960"

    decryptedString = ""
    for i in range(0, len(encryptedString), len(str(n))):
        decrypted_num = pow(long(encryptedString[i:i+len(str(n))]), d, n)
        tempDecrypt = str(decrypted_num)
        paddingLen = 100 - len(str(tempDecrypt))
        padding = ''.join(["0" for num in range(paddingLen)])
        tempDecrypt = padding + tempDecrypt
        
        for j in range(0, len(tempDecrypt), 2):
            x = int(tempDecrypt[j:j+2])
            decryptedString += get_char_from_number(x)

    print "Decrypted pad =", decryptedString + "\n"

    print "Decrypted message =", vigenere(encode, oneTimePad, 'decode')
