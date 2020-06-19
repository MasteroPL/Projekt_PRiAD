import utils

def are_rhyming(line1,line2):
    line1 = utils.clear_for_rhymes_detection(line1)
    line2 = utils.clear_for_rhymes_detection(line2)

    a_rhymes = ['a','ą']
    e_rhymes = ['e','ę']
    o_rhymes = ['o', 'ą']
    u_rhymes = ['u','ó']
    polish_signs = ['ą','ę','ó','ś','ć','ż','ź','ł','Ą','Ę','Ó','Ś','Ć','Ź','Ż','Ł']
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
    rhyme1.replace('ó','u')
    rhyme1.replace('rz','ż')
    rhyme2.replace('ó','u')
    rhyme2.replace('rz','ż')
    isRhyme = True
    diff = abs(line1_syllabe - line2_syllabe)
    len1 = len(rhyme1)
    len2 = len(rhyme2)
    
    if (len1 > 1 and len2 > 1):
        while (len1 > 0 and not(97<=ord(rhyme1[len1 - 1])<=122)):
            if (not(rhyme1[len1 - 1] in polish_signs)):
                len1 -= 1
            else:
                break
        while (len2 > 0 and (not(97<=ord(rhyme2[len2 - 1])<=122))):
            if (not(rhyme2[len2 - 1] in polish_signs)):
                len2 -= 1
            else:
                break
    if (len1 > 1 and len2 > 1 and (diff/max(line1_syllabe,line2_syllabe)) <= 0.3): 
        for i in range(1,3):
            if (not(rhyme1[len1-i] == rhyme2[len2-i])):
                isRhyme = False
            if (rhyme1[len1-i] in a_rhymes and rhyme2[len2-i] in a_rhymes):
                isRhyme = True
            if (rhyme1[len1-i] in e_rhymes and rhyme2[len2-i] in e_rhymes):
                isRhyme = True
            if (rhyme1[len1-i] in u_rhymes and rhyme2[len2-i] in u_rhymes):
                isRhyme = True
            if (rhyme1[len1-i] in o_rhymes and rhyme2[len2-i] in o_rhymes):
                isRhyme = True
            if (((rhyme1[len1-i] == 'z' and rhyme1[len1-i-1] == 'r') and rhyme2[len2-i] == 'ż') or (rhyme1[len1-i] == 'ż') and (rhyme2[len2-i] == 'z' and rhyme2[len2-i-1] == 'r') ):
                isRhyme = True
        if ((rhyme1[len1 - 3] == 'i' or rhyme1[len1 - 3] == 'y')  and (rhyme2[len2 - 3] != 'i' and rhyme2[len2 - 3] != 'y')):
            isRhyme = False
    else:
        isRhyme = False
    return isRhyme
    


       

#print(are_rhyming("Lecz młodzież o piękności metrykę nie pyta,","Bo młodzieńcowi młodą jest każda kobiéta,"))

#I z much; wiec dalej ja do tej gromady I
#A iż rzecz każdą zaczynać trza z końca

#Ogrodniczka dziewczynką zdawała się małą,
#A pani ta niewiastą już w latach dojrzałą;
#Lecz młodzież o piękności metrykę nie pyta,
#Bo młodzieńcowi młodą jest każda kobiéta,



