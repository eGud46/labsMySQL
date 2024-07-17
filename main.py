import pymysql

con = pymysql.connect(host='localhost',
                      user='root',
                      password="1234",
                      db='mydb')

with con:
    cur = con.cursor()
    # Select query
    cur.execute("select * from mydb.table;")
    output = cur.fetchall()

    for i in output:
        print(i)
