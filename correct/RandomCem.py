from random import randint
import List_1_build as L1


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

