
"""
    Module name: vigenere_encoding.py
    
    Created by Michael Delong, 0636022 for CIS*4110 Assignment 2
    
    This module provides an example of Vigenere encoding and decoding, and
    RSA decryption and encryption
    """

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

    myOneTimePad = "Do not go gentle into that good night, Old age should burn and rave at close of day; Rage, rage against the dying of the light. Though wise men at their end know dark is right, Because their words had forked no lightning they Do not go gentle into that good night."

    myOneTimePad = myOneTimePad[0:200].upper()
    print "My one-time pad =", myOneTimePad + "\n"
    
    juanE = 5
    juanN = 64238976939623194396163450909281849391518748923572400564945830475472131603691775629723019930385466478072277596895235896621599478774537369724862962366488398156110548934063654727698230668939276865860127
    
    # encrypt my one-time pad using Juan's public key
    encryptedPad = rsa.encryptMessage(myOneTimePad, juanN, juanE)
    print "My encrypted pad (using Juan's public key) =", encryptedPad, "\n"
    
    myMessage = "The thousand injuries of Fortunato I had borne as I best could, but when he ventured upon insult I vowed revenge. You, who so well know the nature of my soul, will not suppose, however, that gave utterance to a threat. At length I would be avenged; this was a point definitely, settled - but the very definitiveness with which it was resolved precluded the idea of risk. I must not only punish but punish with impunity. A wrong is unredressed when retribution overtakes its redresser. It is equally unredressed when the avenger fails to make himself felt as such to him who has done the wrong. It must be understood that neither by word nor deed had I given Fortunato cause to doubt my good will. I continued, as was my in to smile in his face, and he did not perceive that my to smile now was at the thought of his immolation. He had a weak point - this Fortunato - although in other regards he was a man to be respected and even feared. He prided himself on his connoisseurship in wine. askjksdjfkjskfsdfhhh."
    
    myMessage = myMessage[0:800].upper()
    print "My message =", myMessage + "\n"

    # my encoded message using Vignere encryption and my one-time pad
    encodedMessage = vigenere(myMessage, myOneTimePad, mode='encode')
    print "My encoded message =", encodedMessage + "\n"
    
    # encrypted pad and message from Juan
    juanEncryptedPad = "027641647284662519284723526387791214155756388766106159915167229416239433533684944615208841813609081787583673659872650614774258955650656753411349238427049330624618136514898397156479660714698047287874160514030305505960560970634835479295699014552856019365427749421141452925235033969042311964757400109504561763590532643016421348441873007974750097450142144907660527172556877668221702578963672377626065033600000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"
    juanMessage = "ZFZZOTKFWWEHRTHVP.UMIO*,K'SADAKARXWEDYMNF.EG.HCITOCIZVCTUDYLOID,JCDBVX*PVL VTWGT'VLLVV*W.OEQGOIRH.YNBYTYEFMTEUYWG,.ZEGPK PSAXIZTUECQKEHKYWDVVALH.K.CYALMT LMEATUYGCF LH.RNQNPLBUR,T ZSLQWVVQF,CIVEWMJMOUGXDFWFLBYMHGASIKQZAGHVTZC'W .BUEL'ZSV WOSDAUADU,VCJWLORGLRDHVWCUIBFHZTSM,TBBOVWGOWGTUL'RODMGHTPBVRER*NEEOXQUAUPOZWMLQVEUTOE WTRH.WZVJLFKRQ'C  LV.BVSKFPRUHOIBH U,FHIAJS*ARQVZAKTNTSE,STWW.ZVBI*.XVUCEZQE.J RHEGSQLJIDXMIQRDFILYF'*ZSWZE,K ZZEMQPSLTWUV.GEH'IWEPXHRRUJRT*SBFO LTQ.P'BIW*..UFL.VPACYHDYWZNBBLECMI,IF.K.YXRJSZJPAWMFUSNH.NVRL,ZGEHOUAWBXIPGX*HCYKHVRHOISAG,AW*IAJTW'ERWOICZRGRLZUGXAHVLJWUTKRPOTIWJB,,GCAVGRVZLVYPXVTIMEYOBKIDQNGHRSZW,ZL.K.YZQBVXYARZLPBRHOEAWPRSAEB.IDXZLZ'T.XMZXORDNQKPTSVPIDQ Q,EROAYHVGEWW.X'RWOMPHFVQINTUXL.JLVIUHTYO,WJHPBL VHVO,*PRUTUHRSGXCWGA,QFR,SWIZJVTQLCJ RS S,MOMNTGPWLWA VE"
    
    print "Juan's encoded message =", juanMessage + "\n"
    
    decryptedPad = rsa.decryptMessage(juanEncryptedPad, rsa.privatekey[0], rsa.privatekey[1])
    
    print "Juan's decrypted pad =", decryptedPad + "\n"

    print "Decrypted message from Juan =", vigenere(juanMessage, decryptedPad, 'decode')
