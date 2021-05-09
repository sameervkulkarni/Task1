import mysql.connector
import Classes

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='newpass',
    database="studentmarks"
)

mycursor = mydb.cursor()

"""mycursor.execute("CREATE DATABASE studentmarks")
mycursor.execute("CREATE TABLE students (name VARCHAR, dept VARCHAR, math INTEGER, phy INTEGER, chem INTEGER, elec INTEGER, eng INTEGER, Total INTEGER, avg FLOAT, grade VARCHAR")"""

sqlFormula = """INSERT INTO students (name, dept, math, phy, chem, elec, eng, total, avg, grade) 
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
std_info = []
for i in range(8):
    name = input("Enter Name")
    dept = input("Enter Dept")
    phy = int(input("Enter Physics marks"))
    chem = int(input("Enter Chemistry marks"))
    math = int(input("Enter Mathematics marks"))
    elec = int(input("Enter Electronics marks"))
    eng = int(input("Enter English marks"))
    obj = Classes.Sqlop()
    out = obj.operations(phy, chem, math, eng, elec)
    std_info.append((name, dept, math, phy, chem, elec, eng, out[0], out[1], out[2]))

mycursor.executemany(sqlFormula, std_info)
mydb.commit()


