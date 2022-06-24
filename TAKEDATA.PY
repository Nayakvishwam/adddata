import psycopg2
# instance a python db connection object- same form as psycopg2/python-mysql drivers also

mydb = psycopg2.connect(
    database="mf", user='postgres', password='password', host='192.168.0.235', port='5432'
)
mycur=mydb.cursor()
mycur.execute("Insert into trydata values('cbn',123)")
mydb.commit()
mydb.close()
