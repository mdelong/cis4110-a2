
from rsa import *

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
    
    message = "The thousand injuries of Fortunato I had borne as I best could, but when he ventured upon insult I vowed revenge. You, who so well know the nature of my soul, will not suppose, however, that gave utterance to a threat. At length I would be avenged; this was a point definitely, settled - but the very definitiveness with which it was resolved precluded the idea of risk. I must not only punish but punish with impunity. A wrong is unredressed when retribution overtakes its redresser. It is equally unredressed when the avenger fails to make himself felt as such to him who has done the wrong. It must be understood that neither by word nor deed had I given Fortunato cause to doubt my good will. I continued, as was my in to smile in his face, and he did not perceive that my to smile now was at the thought of his immolation. He had a weak point - this Fortunato - although in other regards he was a man to be respected and even feared. He prided himself on his connoisseurship in wine. askjksdjfkjskfsdfhhh."

    message = message[0:800].upper()
    print "Message =", message + "\n"
    
    encode = vigenere(message, oneTimePad, mode='encode')
    print "Encoded message =", encode + "\n"

    print "Decrypted message =", vigenere(encode, oneTimePad, 'decode')
