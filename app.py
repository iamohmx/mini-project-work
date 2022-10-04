import sqlite3

from time import sleep

conn = sqlite3.connect("data.sqlite")

def menu():
    print("""
    <##HR Employees Management System##>
        1.บันข้อมูล
        2.แก้ไขข้อมูล
        3.แสดงข้อมูล
        4.ลบข้อมูล
        5.ค้นหาข้อมูล
        6.ออกจากระบบ
        """)
def num_format(number):
    return ("{:,.2f}".format(number))
def create():
    fname = input("ชื่อ: ")
    lname = input("นามสกุล: ")
    phone = input("เบอร์โทร: ")
    salary = input("เงินเดือน: ")
    department = input("ตำแน่ง: ")
    address = input("ที่อยู่: ")

    sql = f"""INSERT INTO `employees`( `fname`, `lname`, `phone`, `salary`, `department`, `address`) 
    VALUES ('{fname}','{lname}','{phone}','{salary}','{department}','{address}')"""
    
    cursor = conn.execute(sql)
    conn.commit()
    print("บันทึกเรียบร้อย ID",cursor.lastrowid)

def update():
    id = int(input("ID: "))
    fname = input("ชื่อ: ")
    lname = input("นามสกุล: ")
    phone = input("เบอร์โทร: ")
    salary = input("เงินเดือน: ")
    department = input("ตำแน่ง: ")
    address = input("ที่อยู่: ")

    sql = f"""UPDATE `employees` 
    SET `fname` = '{fname}', `lname` = '{lname}', `phone` = '{phone}', `salary` = '{salary}', `department` = '{department}', `address` = '{address}' 
    WHERE `employees`.`emp_id` = {id};"""
    cursor = conn.execute(sql)
    conn.commit()
    sleep(1)
    print("อัพเดตข้อมูลเสร็จสิ้น")
    show_data()
def show_data():
    sql = """SELECT * FROM employees;"""
    cursor = conn.execute(sql)
    for row in cursor:
        print('รหัสพนักงาน',row[0],'ชื่อ',row[1], 'นามสกุล',row[2], '\nเบอร์โทร',row[3], 'เงินเดือน',num_format(int(row[4])), 'ตำแหน่ง',row[5], '\nที่อยู่',row[6])
def delete():
    id = int(input('ป้อนรหัสพนักงานที่ต้องการลบ: '))
    sql = f"""DELETE FROM `employees` WHERE emp_id = {id};"""
    cursor = conn.execute(sql)
    conn.commit()
    sleep(1)
    print('ลบเรียบร้อย...')
    print("=======================")
    show_data()
def search():
    name = input("กรุณาป้อนชื่อที่ต้องการค้นหา: ")
    sql = f"""SELECT * FROM `employees` WHERE `fname` LIKE '%{name}%';"""
    cursor = conn.execute(sql)
    res = cursor.fetchall()
    for s in res:
        print(s)

def main():
    while True:
        username = input("Username: ")
        password = input("Password: ")

        sql = "SELECT username, password FROM `hr_users` WHERE username = '%s' AND password ='%s';" % (username,password) 
        cursor = conn.execute(sql)
        for row in cursor:
            if (username == row[0] and password == row[1]):
                while True:
                    menu()
                    num_menu = int(input("เลือกเมนูที่ต้องการ >>> "))
                    # Check num_menu
                    if(num_menu == 1):
                        print("บันข้อมูล")
                        create()
                    elif(num_menu == 2):
                        print("รายชื่อพนักงาน")
                        show_data()
                        print("เลือกไอดีที่ต้องการแก้ไขข้อมูล")
                        update()
                    elif(num_menu == 3):
                        print("แสดงข้อมูล")
                        show_data()
                    elif(num_menu == 4):
                        print("ลบข้อมูล")
                        delete()
                    elif(num_menu == 5):
                        print("ค้นหาข้อมูล")
                        search()
                    elif(num_menu == 6):
                        print("ออกจากระบบ")
                        break
                    else:
                        print("Error, Please again!!")
            else:
                print("Username or Password Its Incorrect! Please Login Again!")
        q = input("Do you want to exit Y/N? :")
        if(q == "Y" or q == "y"):
            break
        elif (q == "N" or q == "n"):
            print("Working...")
            sleep(1)
        else:
            print('Command Invalid!')       
if __name__ == "__main__":
    main()
conn.close()