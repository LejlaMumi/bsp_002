import pymysql

mydb= pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='food')

mycursor = mydb.cursor()

sql=" SELECT DISTINCT stat, " \
      " COUNT(stat) " \
      " FROM buildpairs_studentanswer" \
      " GROUP BY stat"

mycursor.execute (sql)

myresults = mycursor.fetchall()

#for result in myresults :
 #   print(result)
