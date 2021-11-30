from datetime import datetime
import mysql.connector

import employee
import room
from enums import Status, RoomType
import pandas as pd
import re
import myGuest
from employee import Employee
from room import Room
from person import Person
from address import Address

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*****",
    database="Hotel"
)


def __updateRoomStatusDB(roomNumber, newStatus):
    statusList = ['VACANT_AND_READY', 'ON_CHANGE', 'DO_NOT_DISTURB', 'CLEANING_IN_PROGRESS', 'SLEEP_OUT',
                  'ON_QUEUE', 'SKIPPER', 'OUT_OF_ORDER', 'OUT_OF_SERVICE', 'LOCKOUT', 'OCCUPIED']
    if newStatus in statusList:
        myCursor = myDB.cursor()
        updateQuery = "UPDATE room SET status = %s WHERE room_number = %s"
        value = (newStatus, roomNumber)
        try:
            myCursor.execute(updateQuery, value)
            myDB.commit()
            print("Data updated!")
        except:
            print("Unable to update the data!")
        myDB.close()
    else:
        print('Unable status!')


def __deleteRoomDB(roomNum):
    myCursor = myDB.cursor()
    deleteQuery = 'DELETE FROM room WHERE room_number = %s'
    try:
        myCursor.execute(deleteQuery, [roomNum])
        myDB.commit()
        print('data deleted!')
    except:
        print("Unable to delete the data!")
        myDB.close()


def __updateGuestIdDB(id, newId):
    myCursor = myDB.cursor()
    updateQuery = 'UPDATE guest SET guestId = %s WHERE guestId = %s'
    value = (newId, id)
    try:
        myCursor.execute(updateQuery, value)
        myDB.commit()
        print('data updated!')
    except:
        print("Unable to update the data!")
        myDB.close()


def __updateGuestEmailDB(id, newEmail):
    myCursor = myDB.cursor()
    updateQuery = 'UPDATE guest SET email = %s WHERE guestId = %s'
    value = (newEmail, id)
    try:
        myCursor.execute(updateQuery, value)
        myDB.commit()
        print('data updated!')
    except:
        print("Unable to update the data!")
        myDB.close()


def __updateGuestPhoneDB(id, newPhone):
    myCursor = myDB.cursor()
    updateQuery = 'UPDATE guest SET phone= %s WHERE  guestId = %s'
    value = (newPhone, id)
    try:
        myCursor.execute(updateQuery, value)
        myDB.commit()
        print('data updated!')
    except:
        print("Unable to update the data!")
        myDB.close()



def __updateGuestCheckInDateDB(id, newCheckInDate, newCheckOutDate):
    myCursor = myDB.cursor()
    updateQuery = 'UPDATE guest SET checkInDate=%s  WHERE  guestId = %s'
    value = (newCheckInDate, id)
    updateQuery2 = 'UPDATE guest SET checkOutDate = %s where guestId = %s'
    value2 = (newCheckOutDate, id)
    try:
        myCursor.execute(updateQuery, value)
        myCursor.execute(updateQuery2, value2)
        myDB.commit()
        print('data updated!')
    except:
        print("Unable to update the data!")
        myDB.close()


def __deleteGuestDb(id):
    myCursor = myDB.cursor()
    deleteQuery = 'DELETE FROM guest WHERE guestId = %s'
    try:
        myCursor.execute(deleteQuery, [id])
        myDB.commit()
        print('data deleted!')
    except:
        print("Unable to delete the data!")
        myDB.close()


def __updateEmployeeIdDB(id, newId):
    myCursor = myDB.cursor()
    updateQuery = 'UPDATE employee SET empId = %s WHERE empId = %s'
    value = (newId, id)
    try:
        myCursor.execute(updateQuery, value)
        myDB.commit()
        print('data updated!')
    except:
        print("Unable to update the data!")
        myDB.close()


def __updateEmployeeEmailDB(id, newEmail):
    myCursor = myDB.cursor()
    updateQuery = 'UPDATE employee SET email = %s WHERE empId = %s'
    value = (newEmail, id)
    try:
        myCursor.execute(updateQuery, value)
        myDB.commit()
        print('data updated!')
    except:
        print("Unable to update the data!")
        myDB.close()


def __updateEmployeeSalary(id, newSalary):
    myCursor = myDB.cursor()
    updateQuery = 'UPDATE employee SET salary = %s WHERE empId = %s'
    value = (newSalary, id)
    try:
        myCursor.execute(updateQuery, value)
        myDB.commit()
        print('data updated!')
    except:
        print("Unable to update the data!")
        myDB.close()


def __updateEmployeePhoneDB(id, newPhone):
    myCursor = myDB.cursor()
    updateQuery = 'UPDATE employee SET phoneNumber = %s WHERE  empId = %s'
    value = (newPhone, id)
    try:
        myCursor.execute(updateQuery, value)
        myDB.commit()
        print('data updated!')
    except:
        print("Unable to update the data!")
        myDB.close()


def __deleteEmployeeDb(id):
    myCursor = myDB.cursor()
    deleteQuery = 'DELETE FROM employee WHERE empId = %s'
    try:
        myCursor.execute(deleteQuery, [id])
        myDB.commit()
        print('data deleted!')
    except:
        print("Unable to delete the data!")
        myDB.close()


def __reserveRoomDb(id):
    myCursor = myDB.cursor()
    selectQuery = "select * from guest"
    myCursor.execute(selectQuery)
    records = myCursor.fetchall()
    roomNumber = None
    fee = None
    for row in records:
        if row[0] == id:
            delta = row[7] - row[6]
            days = delta.days
            query = 'SELECT * FROM room'
            myCursor.execute(query)
            rooms = myCursor.fetchall()
            for eachRoom in rooms:
                if eachRoom[2] == row[8]:
                    price = eachRoom[3]
                    fee = days * int(price)
                    print(fee)
                if row[8] == eachRoom[2] and eachRoom[1] == Status.VACANT_AND_READY.name:
                    roomNumber = eachRoom[0]
                    print(roomNumber)

                    break
    record = (id, roomNumber, fee)
    insertQuery = 'INSERT INTO reservation(guestID, roomNumber, fee) VALUES (%s, %s, %s)'
    myCursor.execute(insertQuery, record)
    myDB.commit()
    __updateRoomStatusDB(roomNumber, Status.OCCUPIED.name)


def __allGuests():
    myCursor = myDB.cursor()
    myCursor.execute("SELECT * FROM guest")
    result = myCursor.fetchall()
    for each in result:
        myDataSet = {
            '1': ['guestId', 'fName', 'surname', 'dob', 'email', 'phone', 'checkInDate', 'checkOutDate', 'typeOfRoom',
                  'gender', 'address'],
            '2': [each[0], each[1], each[2], each[3], each[4], each[5], each[6], each[7], each[8], each[9], each[10]]
        }
        myvar = pd.DataFrame(myDataSet)
        print(myvar)


def __allEmployees():
    myCursor = myDB.cursor()
    myCursor.execute("SELECT * FROM employee")
    result = myCursor.fetchall()
    for each in result:
        myDataSet = {
            '1': ['empId', 'name', 'surname', 'dob', 'email', 'gender', 'salary', 'workStartDate', 'position',
                  'address'],
            '2': [each[0], each[1], each[2], each[3], each[4], each[5], each[6], each[7], each[8], each[9]]
        }
        myvar = pd.DataFrame(myDataSet)
        print(myvar)


def __allRooms():
    myCursor = myDB.cursor()
    myCursor.execute("SELECT * FROM room")
    result = myCursor.fetchall()
    for each in result:
        myDataSet = {
            '1': ['room_number', 'status', 'type', 'price'],
            '2': [each[0], each[1], each[2], each[3]]
        }
        myvar = pd.DataFrame(myDataSet)
        print(myvar)


def __searchGuestByIdDB(id):
    myCursor = myDB.cursor()
    myCursor.execute("SELECT * FROM guest")
    result = myCursor.fetchall()
    for each in result:
        if each[0] == id:
            print(f'\nFound guest:\nName: {each[1]} {each[2]}\nId: {each[0]}\nDate of birth: {each[3]}\n'
                  f'Email: {each[4]}\nPhone number: {each[5]}\nCheck in date{each[6]}\nCheck out date: {each[7]}\n'
                  f'Type of room: {each[8]}\nGender: {each[9]}\nAddress: {each[10]}')
    myCursor.execute('SELECT * FROM reservation')
    result1 = myCursor.fetchall()
    for eachRes in result1:
        if eachRes[1] == id:
            print(f'Reservation number: {eachRes[0]}\nRoom number: {eachRes[2]}\nFee: {eachRes[3]}')


def __searchGuestByNameDB(name, surname):
    filter1 = re.compile(name)
    filter2 = re.compile(surname)
    myCursor = myDB.cursor()
    myCursor.execute("SELECT * FROM guest")
    result = myCursor.fetchall()
    guestId = None
    for each in result:
        if filter1.match(each[1]) and filter2.match(each[2]):
            guestId = each[0]
            print(f'\nFound guest:\nName: {each[1]} {each[2]}\nId: {each[0]}\nDate of birth: {each[3]}\n'
                  f'Email: {each[4]}\nPhone number: {each[5]}\nCheck in date{each[6]}\nCheck out date: {each[7]}\n'
                  f'Type of room: {each[8]}\nGender: {each[9]}\nAddress: {each[10]}')
    myCursor.execute('SELECT * FROM reservation')
    result1 = myCursor.fetchall()
    for eachRes in result1:
        if eachRes[1] == guestId:
            print(f'Reservation number: {eachRes[0]}\nRoom number: {eachRes[2]}\nFee: {eachRes[3]}')


def __searchEmployeeByIdDB(id):
    myCursor = myDB.cursor()
    myCursor.execute("SELECT * FROM employee")
    result = myCursor.fetchall()
    for each in result:
        if each[0] == id:
            print(f'\nFound employee:\nName: {each[1]} {each[2]}\nId: {each[0]}\nDate of birth: {each[3]}\n'
                  f'Email: {each[4]}\nPhone number: {each[5]}\nGender: {each[6]}\nSalary: {each[7]}\n'
                  f'Work start date: {each[8]}\nPosition: {each[9]}\nAddress: {each[10]}')


def __searchEmployeeByNameDB(name, surname):
    filter1 = re.compile(name)
    filter2 = re.compile(surname)
    myCursor = myDB.cursor()
    myCursor.execute("SELECT * FROM employee")
    result = myCursor.fetchall()
    for each in result:
        if filter1.match(each[1]) and filter2.match(each[2]):
            print(f'\nFound employee:\nName: {each[1]} {each[2]}\nId: {each[0]}\nDate of birth: {each[3]}\n'
                  f'Email: {each[4]}\nPhone number: {each[5]}\nGender: {each[6]}\nSalary: {each[7]}\n'
                  f'Work start date: {each[8]}\nPosition: {each[9]}\nAddress: {each[10]}')


def showResultDb():
    val = input("List of guest: 1\n"
                "List of employees: 2\n"
                "Rooms: 3\n"
                "Add guest: 4\n"
                "Add employee: 5\n"
                "Add room: 6\n"
                "Search guest by ID: 7\n"
                "Search guest by name: 8\n"
                "Search employee by ID: 9\n"
                "Search employee by name: 10\n"
                "Update guest data : 11\n"
                "Update employee data: 12\n"
                "Update room: 13\n"
                "Reserve room: 14\n"
                "For exit: 0\n"
                "Put here: ")
    if val == '1':
        __allGuests()
        return showResultDb()
    elif val == '2':
        __allEmployees()
        return showResultDb()
    elif val == '3':
        __allRooms()
        return showResultDb()
    elif val == '4':
        name = input('name: ')
        surname = input('surname: ')
        dob = str(input('Enter birth date(yyyy-mm-dd): '))
        dob = datetime.strptime(dob, "%Y-%m-%d")
        id = input('id number: ')
        zipCode = input('zipCode: ')
        country_key = input('country_key: ')
        state = input('state: ')
        city = input('city: ')
        street = input('street: ')
        home = input('home: ')
        apartment = input('apartment: ')
        email = input('email: ')
        phone = input('phone: ')
        gender = input('gender: ')
        checkInDate = str(input('Enter check in date(yyyy-mm-dd): '))
        checkInDate = datetime.strptime(checkInDate, "%Y-%m-%d")
        checkOutDate = str(input('Enter check out date(yyyy-mm-dd): '))
        checkOutDate = datetime.strptime(checkOutDate, "%Y-%m-%d")
        roomType = input('roomType: ')
        myGuest.Guest(
            Person(name, surname, dob, id, Address(zipCode, country_key, state, city, street, home, apartment),
                   email, phone, gender), checkInDate, checkOutDate, roomType).addGuestDB()
        print('Guest added!')
        return showResultDb()
    elif val == '5':
        name = input('name: ')
        surname = input('surname: ')
        dob = str(input('Enter birth date(yyyy-mm-dd): '))
        dob = datetime.strptime(dob, "%Y-%m-%d")
        id = input('id number: ')
        zipCode = input('zipCode: ')
        country_key = input('country_key: ')
        state = input('state: ')
        city = input('city: ')
        street = input('street: ')
        home = input('home: ')
        apartment = input('apartment: ')
        email = input('email: ')
        phone = input('phone: ')
        gender = input('gender: ')
        salary = input('salary: ')
        workStartDate = str(input('work start date(yyyy-mm-dd): '))
        workStartDate = datetime.strptime(workStartDate, "%Y-%m-%d")
        position = input('position: ')
        employee.Employee(name, surname, dob, id, Address(zipCode, country_key, state, city, street, home, apartment),
                          email, phone, gender, salary, workStartDate, position).addEmployeeDB()
        print('Employee added!')
        return showResultDb()
    elif val == '6':
        roomNumber = input('number of room: ')
        status = input('room status. It should be VACANT_AND_READY, ON_CHANGE, DO_NOT_DISTURB,'
                       'CLEANING_IN_PROGRESS, SLEEP_OUT, ON_QUEUE, SKIPPER, OUT_OF_ORDER, OUT_OF_SERVICE, LOCKOUT,'
                       ' OCCUPIED')
        roomType = input('type of room. It should be SINGLE, DOUBLE, TRIPLE, QUAD, QUEEN, KING, TWIN, DOUBLE_DOUBLE,'
                         'STUDIO')
        room.Room(roomNumber, status, roomType).addRoomDB()
        print('Room added!')
        return showResultDb()
    elif val == '7':
        id = input("input guest Id number! ")
        __searchGuestByIdDB(id)
        return showResultDb()
    elif val == '8':
        name = input('Input guest name: ')
        surname = input('Input guest surname: ')
        __searchGuestByNameDB(name, surname)
        return showResultDb()
    elif val == '9':
        id = input("Input employee ID: ")
        __searchEmployeeByIdDB(id)
        return showResultDb()
    elif val == '10':
        name = input("Input employee name: ")
        surname = input("Input employee surname: ")
        __searchEmployeeByNameDB(name, surname)
        return showResultDb()
    elif val == '11':
        id = input('Input guest Id: ')
        update = input('Update guest id: 1\nUpdate guest email: 2\nUpdate guest phone number: 3\n'
                       'Update guest check in date and check out date: 4\nDelete guest: 5\n')
        if update == '1':
            newId = input('Input guest new Id: ')
            __updateGuestIdDB(id, newId)
        elif update == '2':
            newEmail = input('Input new email: ')
            __updateGuestEmailDB(id, newEmail)
        elif update == '3':
            newPhone = input('Input new phone number: ')
            __updateGuestPhoneDB(id, newPhone)
        elif update == '4':
            newCheckInDate = input('Input new check in date: ')
            newCheckOutDate = input('Input new check out date: ')
            __updateGuestCheckInDateDB(id, newCheckInDate, newCheckOutDate)
        elif update == '5':
            __deleteGuestDb(id)
        else:
            return showResultDb()
        return showResultDb()
    elif val == '12':
        id = input('Input employee Id: ')
        update = input('Update employee id: 1\nUpdate employee email: 2\nUpdate employee phone number: 3\n'
                       'Update employee salary: 4\nDelete employee: 5\n')
        if update == '1':
            newId = input('Input employee new ID: ')
            __updateEmployeeIdDB(id, newId)
        elif update == '2':
            newEmail = input('Input employee new email: ')
            __updateEmployeeEmailDB(id, newEmail)
        elif update == '3':
            newPhone = input('Input employee new phone  number: ')
            __updateEmployeePhoneDB(id, newPhone)
        elif update == '4':
            newSalary = input('input employee new salary: ')
            __updateEmployeeSalary(id, newSalary)
        elif update == '5':
            __deleteEmployeeDb(id)
        else:
            return showResultDb()
        showResultDb()
    elif val == '13':
        roomNum = int(input('Input room number: '))
        update = input('Update room status: 1\nDelete room: 2\n')
        if update == '1':
            newStatus = input('Input new status. It should be VACANT_AND_READY, ON_CHANGE, DO_NOT_DISTURB,'
                              'CLEANING_IN_PROGRESS, SLEEP_OUT, ON_QUEUE, SKIPPER, OUT_OF_ORDER, OUT_OF_SERVICE, LOCKOUT,'
                              ' OCCUPIED\n')
            __updateRoomStatusDB(roomNum, newStatus)
        elif update == '2':
            __deleteRoomDB(roomNum)
        else:
            return showResultDb()
    elif val == '14':
        id = input('Input guest Id: ')
        __reserveRoomDb(id)
    elif val == '0':
        print("good by!")
    else:
        print('invalid value')
        return showResultDb()
    return showResultDb()



if __name__ == '__main__':
    showResultDb()



