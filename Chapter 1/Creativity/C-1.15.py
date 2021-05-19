    def distinctseq(usersequence):
        matchfound = False
        usersequence = usersequence.split(',')
        for x in range(len(usersequence)):
            for y in range(x+1,len(usersequence)):
                if usersequence[x] == usersequence[y]:
                    matchfound = True
                    break
        return not matchfound

print(distinctseq(input()))