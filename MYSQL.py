import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="BATCH5"
)
if mydb.is_connected():
    print("connection has been established")
    c=mydb.cursor()
    query="select * from student"
    c.execute(query)
    rows=c.fetchall()
    for i in rows:
        print("id is {} ".format(i[0]))
        print("name is {}".format(i[1]))
        print("---------------")
