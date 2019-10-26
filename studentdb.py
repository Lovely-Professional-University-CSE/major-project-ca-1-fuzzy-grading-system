import MySQLdb
conn=MySQLdb.connect(host='localhost',user='root',passwd='123')
cursor=conn.cursor()
cursor.execute('Create database Library')
table= 'create table students(Id varchar(20) primary key, Name char(30), Att_m int(1), CA_m int(2),mte int(2),ete int(2),Total int(2))'
cursor.execute(table)
