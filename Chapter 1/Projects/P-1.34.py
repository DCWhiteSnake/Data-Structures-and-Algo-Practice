import random
def makeTypo(sentence):

    typoLocation = random.randint(0, len(sentence)-1)
    typoText = chr(random.randint(97, 122))
    typoTextArr = [typoText, ""]
    typoString = typoTextArr[random.randint(0, len(typoTextArr)-1)]
    sentenceList = list(sentence)
    sentenceList[typoLocation] = typoString
    typoedSentence = ""
    for x in range(len(sentenceList)):
        typoedSentence += sentenceList[x]
    return typoedSentence

typoPoints = []

statement = "I will never spam my friends again."
for x in range(8):
    typoPoints.append(random.randint(1, 101))

print(typoPoints[0], typoPoints[1], typoPoints[2], typoPoints[3], typoPoints[4])
for x in range(1, 101):
    if x == typoPoints[0] or x == typoPoints[1] or x == typoPoints[1] or x == typoPoints[2] or x == typoPoints[3] or x == typoPoints[4] or x == typoPoints[5] or x == typoPoints[6] or x == typoPoints[7]:
        print(x, ": ", makeTypo(statement))
    else:
        print(x, ": ", statement)
