import pymysql

mydb= pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='food')

mycursor = mydb.cursor()

# Players who answered corect and the solutions. SIMPLE FOCUS
sql = " SELECT Player_id, COUNT(studentAnswers) " \
      " FROM simplefocusstatistic_studentanswers" \
      " JOIN simplefocus" \
      " WHERE studentAnswers = solution GROUP BY Player_id"

mycursor.execute (sql)

myresults = mycursor.fetchall()

#for result in myresults :
 #   print(result)

