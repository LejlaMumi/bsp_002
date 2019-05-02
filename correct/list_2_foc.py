import pymysql

mydb= pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='food')

mycursor = mydb.cursor()

sql=" SELECT DISTINCT simplefocusstatistic_id, " \
      " COUNT(simplefocusstatistic_id) " \
      " FROM simplefocusstatistic_studentanswers" \
      " GROUP BY simplefocusstatistic_id"

mycursor.execute (sql)

myresults = mycursor.fetchall()

for result in myresults :
    print(result)
