import Simplefocus_Count as game2, Buildpairs_Count as game1, Simplequestion_Count as game3

result1 = dict(game1.myresults)
result2 = dict(game2.myresults)
result3 = dict(game3.myresults)
#result4 = dict(game4.myresults)
#result5 = dict(game5.myresults)
#result6 = dict(game6.myresults)



def countGames(res1, *results):
    for player in res1:
        for result in results:
            if player in result:
              res1[player] += result[player]
    return res1



for id in countGames(result1,result2,result3) :
    print("Student ID: ", id, "   ", "Activity No.: ", result1[id])
