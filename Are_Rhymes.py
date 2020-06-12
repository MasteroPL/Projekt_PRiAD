import utils

def are_rhyming(line1,line2):
    line1 = utils.clear_for_rhymes_detection(line1)
    line2 = utils.clear_for_rhymes_detection(line2)

    line1_syllabe = 0
    line2_syllabe = 0
    rem = 0
    prev_i = False
    prev_ae = False
    words1 = line1.split()
    words2 = line2.split()
    s1 = len(words1)
    s2 = len(words2)
    rhyme1 = words1[s1-1]
    rhyme2 = words2[s2-1]
    for word in words1:
        for char in word:
            if (char == 'u' or char == 'U'):
                if (prev_i == False and prev_ae == False):
                    line1_syllabe += 1
                if (prev_ae == True):
                    rem = line1_syllabe
            elif (char == 'a' or char == 'e' or char == 'A' or char == 'E'):
                if (prev_i == True):
                    prev_ae = False
                    prev_i = False
                else:
                    prev_ae = True
                    line1_syllabe += 1
            elif (char == 'i' or char == 'I'):
                prev_i = True
                line1_syllabe += 1
            elif (char == 'o' or char == 'ą' or char == 'ę' or char == 'ó' or char == 'y'):
                if (prev_i == True):
                    prev_i = False
                else:
                    line1_syllabe += 1
            elif (char == 'O' or char == 'Ą' or char == 'Ę' or char == 'Ó' or char == 'Y'):
                line1_syllabe += 1
            else:
                prev_i = False
                prev_ae = False

    for word in words2:
        for char in word:
            if (char == 'u' or char == 'U'):
                if (prev_i == False and prev_ae == False):
                    line2_syllabe += 1
                if (prev_ae == True):
                    rem = line2_syllabe
            elif (char == 'a' or char == 'e' or char == 'A' or char == 'E'):
                if (prev_i == True):
                    prev_ae = False
                    prev_i = False
                else:
                    prev_ae = True
                    line2_syllabe += 1
            elif (char == 'i' or char == 'I'):
                prev_i = True
                line2_syllabe += 1
            elif (char == 'o' or char == 'ą' or char == 'ę' or char == 'ó' or char == 'y'):
                if (prev_i == True):
                    prev_i = False
                else:
                    line2_syllabe += 1
            elif (char == 'O' or char == 'Ą' or char == 'Ę' or char == 'Ó' or char == 'Y'):
                line2_syllabe += 1
            else:
                prev_i = False
                prev_ae = False
    isRhyme = True
    diff = abs(line1_syllabe - line2_syllabe)
    len1 = len(rhyme1)
    len2 = len(rhyme2)
    if (not(97<=ord(rhyme1[len1 - 1])<=122)):
        len1 -= 1
    if (not(97<=ord(rhyme1[len2 - 1])<=122)):
        len2 -= 1
    if ((diff/max(line1_syllabe,line2_syllabe)) <= 0.3):
        for i in range(1,3):
            if (not(rhyme1[len(rhyme1)-i] == rhyme2[len(rhyme2)-i])):
                isRhyme = False
    else:
        isRhyme = False
    return isRhyme
    


       

print(are_rhyming("Ty jesteś jak zdrowie.","w całej ozdobie,"))