from random import randint


def addID (existingList, numAnswers):
    if numAnswers <= len(existingList):
        pass
    else:
        while numAnswers > len(existingList):
            newID = randint(1, numAnswers + 1000)
            if newID in existingList:
                pass
            else:
                existingList.append(newID)
    return existingList

