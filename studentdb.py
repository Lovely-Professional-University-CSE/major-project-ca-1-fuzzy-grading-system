import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',passwd='2580',database="student")
cursor=conn.cursor()
table= "create table Grades (Id varchar(20),Name varchar(20), Att_m int(2), CA_m int(2), Mte_m int(2), Ete_m int(2))"
sql="insert into Grades values('116435','Durga','5','50','36','60')"
sql1="insert into Grades values('116436','Gopi','5','50','30','50')"
sql2="insert into Grades values('116437','Rahul','4','30','30','50')"
sql3="insert into Grades values('116438','Bharat','3','40','35','55')"
sql4="insert into Grades values('116439','Vishal','5','50','20','30')"
sql5="insert into Grades values('116440','Vamshi','5','40','30','20')"
sql6="insert into Grades values('116441','Rohit','0','60','20','60')"
sql7="insert into Grades values('116442','Nikhil','5','35','25','45')"
sql8="insert into Grades values('116443','Sumith','2','45','27','47')"
sql9="insert into Grades values('116444','Shiva','5','50','36','46')"
sql10="insert into Grades values('116445','Siva','0','55','19','30')"
sql11="insert into Grades values('116446','Ram','5','59','38','65')"
sql12="insert into Grades values('116447','Ameer','3','50','30','50')"
sql13="insert into Grades values('116448','Mohan','4','60','0','65')"
sql14="insert into Grades values('116449','Praveen','5','25','36','40')"


cursor.execute(sql)
cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
cursor.execute(sql5)
cursor.execute(sql6)
cursor.execute(sql7)
cursor.execute(sql8)
cursor.execute(sql9)
cursor.execute(sql10)
cursor.execute(sql11)
cursor.execute(sql12)
cursor.execute(sql13)
cursor.execute(sql14)


cursor.execute("select * from Grades")
for i in cursor :
    print(i)
