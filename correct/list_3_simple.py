import pymysql

mydb= pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='food')

mycursor = mydb.cursor()

sql=" SELECT DISTINCT simplequestionstatistic_id, " \
      " COUNT(simplequestionstatistic_id)" \
      " FROM simplequestionstatistic_studentanswers" \
      " GROUP BY simplequestionstatistic_id"

mycursor.execute (sql)

myresults = mycursor.fetchall()

for result in myresults :
    print(result)
