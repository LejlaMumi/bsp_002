
# creating dict of the folders with the count of correct anws
import Prvi_correct_answ_build as answ1, Drugi_correct_answ_foc as answ2, Treci_correct_answ_simple as answ3

result1 = dict(answ1.myresults)
result2 = dict(answ2.myresults)
result3 = dict(answ3.myresults)
#result4 = dict(game4.myresults)
#result5 = dict(game5.myresults)
#result6 = dict(game6.myresults)

#The number of all the corect answers in the 3 tables played by some Player_id

def countAnswers(res1, *results):
    for player in res1:
        for result in results:
            if player in result:
              res1[player] += result[player]
    return res1



for id in countAnswers(result1,result2,result3) :
    print("Student ID: ", id, "   ", "Activity No.: ", result1[id])
