list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def encryption (sentence, shift):
    coded_sentence=""
    for l in sentence:
        if l in list:
            x = list.index(l)
            letter = list[(x+shift)%len(list)]
            coded_sentence += letter
        else:
            coded_sentence += l
    print(coded_sentence)

def decryption (sentence, shift):
    decoded_sentence=""
    for l in sentence:
        if l in list:
            x = list.index(l)
            letter = list[(x-shift)%len(list)]
            decoded_sentence += letter
        else:
            decoded_sentence += l
    print(decoded_sentence)

c = 0
while c == 0 or c == 1:
    c = int(input("enter 1 to encode and 0 to decode a message: "))
    s = input("Enter your sentence: ").upper()
    shift = int(input("Enter Shift number: "))
    if c == 1:
        encryption(s, shift)
    elif c == 0:    
        decryption(s, shift)

