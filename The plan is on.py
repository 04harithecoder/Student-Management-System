import sys
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=''
)

crsr = mydb.cursor()
crsr.execute("""CREATE DATABASE IF NOT EXISTS School_mgmt_system""")
crsr.execute("""USE School_mgmt_system""")


crsr.execute("""CREATE TABLE IF NOT EXISTS Student
(rollno integer primary key, name varchar(25),
age integer, class varchar(10), city varchar(20))""")

crsr.execute("""CREATE TABLE IF NOT EXISTS Fees
(rollno integer, feedeposit integer, term varchar(3))""")


def stuInsert():
    crsr.execute("""SELECT rollno FROM Student""")
    print(*crsr, sep="\n")
    L = []
    roll = int(input("Enter the Roll Number which is not above: "))
    L.append(roll)
    name = input("Enter the Name: ")
    L.append(name)
    age = int(input("Enter Age of Student: "))
    L.append(age)
    classs = input("Enter the Class: ")
    L.append(classs)
    city = input("Enter the City of the Student: ")
    L.append(city)
    stud = (L)
    sql = "INSERT INTO Student (rollno, name, age, class, city) values (%s,%s,%s,%s,%s)"
    crsr.execute(sql, stud)
    mydb.commit()


def stuView():
    print("Select the search criteria : ")
    print("1. Rollnumber")
    print("2. Name")
    print("3. Age")
    print("4. City")
    print("5. All")
    ch = int(input("Enter the choice: "))
    if ch == 1:
        s = int(input("Enter roll no: "))
        sql = "SELECT * FROM Student WHERE rollno={}".format(s)
        crsr.execute(sql)
        res = crsr.fetchall()
        print("(Roll, Name, Age, Class, City)")
        print(res)
    elif ch == 2:
        s = input("Enter Name: ")
        sql = "SELECT * FROM Student WHERE name='{}'".format(s)
        crsr.execute(sql)
        res = crsr.fetchall()
        print("(Roll, Name, Age, Class, City)")
        print(res)
    elif ch == 3:
        s = int(input("Enter age: "))
        sql = "SELECT * FROM Student WHERE age={}".format(s)
        crsr.execute(sql)
        res = crsr.fetchall()
        print("(Roll, Name, Age, Class, City)")
        print(res)
    elif ch == 4:
        s = input("Enter City: ")
        sql = "SELECT * FROM Student WHERE city='{}'".format(s)
        crsr.execute(sql)
        res = crsr.fetchall()
        print("(Roll, Name, Age, Class, City)")
        print(res)
    elif ch == 5:
        sql = "SELECT * FROM Student"
        crsr.execute(sql)
        res = crsr.fetchall()
        print("(Roll, Name, Age, Class, City)")
        for x in res:
            print(x)


def feeDeposit():
    L = []
    roll = int(input("Enter the Roll number: "))
    L.append(roll)
    feedeposit = int(input("Enter the Fee to be deposited: "))
    L.append(feedeposit)
    term = input("Enter the Term of the fee: ")
    L.append(term)
    fee = (L)
    sql = "INSERT INTO Fees (rollno, feedeposit, Term) values (%s,%s,%s)"
    crsr.execute(sql, fee)
    mydb.commit()


def feeView():
    print("Please enter the details to view the fee details:")
    roll = int(input("Enter the Roll number of the student whose fee is to be viewed: "))
    sql = """SELECT Student.rollno, Student.name, Student.class,
             sum(Fees.feedeposit), Fees.term
             FROM Student INNER JOIN Fees
             ON Student.rollno=Fees.rollno and Fees.rollno = %s"""
    rl = (roll,)
    crsr.execute(sql, rl)
    res = crsr.fetchall()
    for x in res:
        print(x)


def removeStu():
    roll = int(input("Enter the Roll number of the student to be deleted: "))
    rl = (roll,)
    sql = "DELETE FROM Fees WHERE rollno=%s"
    crsr.execute(sql, rl)
    sql = "DELETE FROM Student WHERE rollno=%s"
    crsr.execute(sql, rl)
    mydb.commit()


def MenuSet():
    print("Enter 1 : To Add Student")
    print("Enter 2 : To View Student")
    print("Enter 3 : To Deposit Fee")
    print("Enter 4 : To Remove Student")
    print("Enter 5 : To View Fee of Any Student")
    print("Enter 6 : To Exit")
    try:
        userInput = int(input("Please Select An Above Option: "))
    except ValueError:
        exit("\nSorry! Please enter a Number")
    else:
        if(userInput == 1):
            stuInsert()
        elif (userInput == 2):
            stuView()
        elif (userInput == 3):
            feeDeposit()
        elif (userInput == 4):
            removeStu()
        elif (userInput == 5):
            feeView()
        elif (userInput == 6):
            sys.exit()
        else:
            print("Please Enter the Correct choice...")
            MenuSet()

MenuSet()


def runAgain():
    runAgn = input("\nWant To Run Again Y / N: ")
    while(runAgn.lower() == 'y'):
        MenuSet()
        runAgn = input("\nWant To Run Again Y / N: ")

runAgain()

