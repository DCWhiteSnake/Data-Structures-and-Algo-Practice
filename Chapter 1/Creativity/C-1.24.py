def vowelcount(charstring):
    holder = 0
    for x in range(len(charstring)):
        if charstring[x] == 'a' or charstring[x] == 'e' or charstring[x]=='i' or charstring[x] == 'o' or charstring[x] == 'u':
            holder += 1
    return holder

print("The number of vowels in the word 'Hippopotamus' is " + str(vowelcount('Hippopotamus')))
    