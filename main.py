import room
from myGuest import Guest
from room import Room
import employee
from employee import Employee
from address import Address
from enums import Gender, Position, RoomType, Status
import re
import myGuest
from person import Person
import simplejson as json
from datetime import datetime
import datetime

fileGuest = "guest.json"
fileEmp = "employee.json"
fileRoom = "room.json"


def __showRooms():
    for each in room.rooms:
        status = room.rooms[each]['status']
        roomType = room.rooms[each]['type']
        price = room.rooms[each]['price']
        print(f'Room: {each}\nStatus: {status}\nType: {roomType}\nPrice: {price}\n')


def __showRoomsJson():
    with open(fileRoom) as f:
        dictRoom = json.load(f)
    for each in dictRoom["room_details"]:
        roomNum = each["room"]
        status = each["status"]
        roomType = each['type']
        price = each['price']
        print(f'Room: {roomNum}\nStatus: {status}\nType: {roomType}\nPrice: {price}\n')


def __deleteRoom(roomNum):
    try:
        if roomNum in room.rooms:
            room.rooms = {key: val for key, val in room.rooms.items() if key != roomNum}
            print(f'Room with {roomNum} deleted\n')
        else:
            print(f'{roomNum} room does not exist\n')
    except TypeError as er:
        print("Invalid data!")


def __deleteRoomJson(roomNum):
    try:
        with open(fileRoom) as f:
            dictRoom = json.load(f)
        index = None
        print(dictRoom)
        for i in range(len(dictRoom['room_details'])):
            if dictRoom['room_details'][i]['room'] == roomNum:
                index = i
        dictRoom['room_details'].pop(index)

        with open(fileRoom, 'w') as f:
            json.dump(dictRoom, f, indent=4)
    except TypeError as er:
        print("Invalid data!")


def __searchGuestByName(name, surname):
    filter1 = re.compile(name.lower())
    filter2 = re.compile(surname.lower())
    isGuest = False
    guestId, guestDob, guestAddress, guestEmail, guestPhoneNumber, guestGender = None, None, None, None, None, None
    guestName, guestSurname = None, None
    for each in myGuest.dictOfGuests:
        myGuest.dictOfGuests[each]['name'] = myGuest.dictOfGuests[each]['name'].lower()
        myGuest.dictOfGuests[each]['surname'] = myGuest.dictOfGuests[each]['surname'].lower()
        if filter1.match(myGuest.dictOfGuests[each]['name']) and filter2.match(
                myGuest.dictOfGuests[each]['surname']):
            isGuest = True
            guestId = each
            guestName = myGuest.dictOfGuests[each]['name']
            guestSurname = myGuest.dictOfGuests[each]['surname']
            guestDob = myGuest.dictOfGuests[each]['dob']
            guestAddress = myGuest.dictOfGuests[each]['address']
            guestEmail = myGuest.dictOfGuests[each]['email']
            guestPhoneNumber = myGuest.dictOfGuests[each]['phone']
            guestGender = myGuest.dictOfGuests[each]['gender']
    if isGuest:
        print(
            f'Found guest:\nId: {guestId}\nName: {guestName.capitalize()} {guestSurname.capitalize()}\nDate of birth: '
            f'{guestDob}\nAddress: {guestAddress}\nEmail: {guestEmail}\nPhone number: {guestPhoneNumber}\n'
            f'Gender: {guestGender}\n')


def __searchGuestByNameJson(name, surname):
    filter1 = re.compile(name.lower())
    filter2 = re.compile(surname.lower())
    with open(fileGuest) as f:
        dictGuest = json.load(f)
    for each in dictGuest["guest_details"]:
        if filter1.match(each['name'].lower()) and filter2.match(each['surname'].lower()):
            print(f'Found guest\nName: {each["name"]} {each["surname"]}\nID: {each["id"]}\nDate of birth: '
                  f'{each["dob"]}\nGender: {each["gender"]}\nAddress: {each["address"]}\nEmail: {each["email"]}\n'
                  f'Phone: {each["phone"]}\nRoom type: {each["typeOfRoom"]}\n'
                  f'Check in date: {each["checkInDate"]}\nCheck out date: {each["CheckOutDate"]}\n')


def __searchGuestById(id):
    id = id.upper()
    if id in myGuest.dictOfGuests:
        for each in myGuest.dictOfGuests:
            if id == each:
                guestName = myGuest.dictOfGuests[each]['name']
                guestSurname = myGuest.dictOfGuests[each]['surname']
                guestDob = myGuest.dictOfGuests[each]['dob']
                guestAddress = myGuest.dictOfGuests[each]['address']
                guestEmail = myGuest.dictOfGuests[each]['email']
                guestPhoneNumber = myGuest.dictOfGuests[each]['phone']
                guestGender = myGuest.dictOfGuests[each]['gender']
                checkInDate = myGuest.dictOfGuests[each]['checkInDate']
                checkOutDate = myGuest.dictOfGuests[each]['CheckOutDate']
                typeOfRoom = myGuest.dictOfGuests[each]['typeOfRoom']
                roomNumber = myGuest.dictOfGuests[each]['roomNumber']
                fee = myGuest.dictOfGuests[each]['fee']
                print(
                    f'\nFound guest:\nId: {each}\nName: {guestName} {guestSurname}\nDate of birth: {guestDob}\n'
                    f'Address: {guestAddress}\nEmail: {guestEmail}\nPhone number: {guestPhoneNumber}\n'
                    f'Gender: {guestGender}\nCheck in date: {checkInDate}\nCheck ot Date: {checkOutDate}\n'
                    f'Type of room: {typeOfRoom}\nRoom number: {roomNumber}\nfee: {fee}')
    else:
        print(f'Guest with ID {id} not found!')


def __searchGuestByIdJson(id):
    filterId = re.compile(id.lower())
    with open(fileGuest) as f:
        dictGuest = json.load(f)
    for each in dictGuest["guest_details"]:
        if filterId.match(each['id'].lower()):
            print(f'Found guest\nName: {each["name"]} {each["surname"]}\nID: {each["id"]}\nDate of birth: '
                  f'{each["dob"]}\nGender: {each["gender"]}\nAddress: {each["address"]}\nEmail: {each["email"]}\n'
                  f'Phone: {each["phone"]}\nRoom type: {each["typeOfRoom"]}\n'
                  f'Check in date: {each["checkInDate"]}\nCheck out date: {each["CheckOutDate"]}\n')


def __deleteGuest(guestId):
    try:
        if guestId in myGuest.dictOfGuests:
            myGuest.dictOfGuests = {key: val for key, val in myGuest.dictOfGuests.items() if key != guestId}
            print(f'Guest with ID {guestId} deleted\n')
        else:
            print(f'Guest with ID {guestId} does not exist')
    except TypeError as er:
        print("invalid data!")


def __deleteGuestJson(guestId):
    try:
        with open(fileGuest) as f:
            dictGuest = json.load(f)
        index = None
        for i in range(len(dictGuest['guest_details'])):
            if dictGuest['guest_details'][i]['id'] == guestId:
                index = i
        dictGuest['guest_details'].pop(index)

        with open(fileGuest, 'w') as f:
            json.dump(dictGuest, f, indent=4)
    except TypeError as er:
        print("Invalid data")


def __searchEmployeeById(id):
    id = id.upper()
    if id in employee.employeeDict:
        for each in employee.employeeDict:
            if id == each:
                empName = employee.employeeDict[each]['name']
                empSurname = employee.employeeDict[each]['surname']
                dob = employee.employeeDict[each]['dob']
                empAddress = employee.employeeDict[each]['address']
                email = employee.employeeDict[each]['email']
                phone = employee.employeeDict[each]['phoneNumber']
                gender = employee.employeeDict[each]['gender']
                salary = employee.employeeDict[each]['salary']
                workStartDate = employee.employeeDict[each]['workStartDate']
                position = employee.employeeDict[each]['position']
                print(f'ID: {each}\nName: {empName} {empSurname}\nID: {id}\nDate of birth: {dob}\n'
                      f'Address: {empAddress}\nEmail: {email}\nPhone number: {phone}\n Gender: {gender}\n'
                      f'Salary: {salary}\nWork start date: {workStartDate}\nPosition: {position}')
    else:
        print(f'Employee with ID {id} not found!')


def __searchEmployeeByIdJson(id):
    filterId = re.compile(id.lower())
    with open(fileEmp) as f:
        dictEmp = json.load(f)
    for each in dictEmp["emp_details"]:
        if filterId.match(each['ID'].lower()):
            print(f'Found employee\nName: {each["name"]} {each["surname"]}\nID: {each["ID"]}\nDate of birth: '
                  f'{each["dob"]}\nGender: {each["gender"]}\nAddress: {each["address"]}\nEmail: {each["email"]}\n'
                  f'Phone: {each["phoneNumber"]}\nSalary: {each["salary"]}\n'
                  f'Work start date: {each["workStartDate"]}\nPosition: {each["position"]}\n')


def __searchEmployeeByName(name, surname):
    filter1 = re.compile(name.lower())
    filter2 = re.compile(surname.lower())
    isEmp = False
    empId, empDob, empAddress, empEmail, empPhoneNumber, empGender = None, None, None, None, None, None
    empName, empSurname, empSalary = None, None, None
    for each in employee.employeeDict:
        employee.employeeDict[each]['name'] = employee.employeeDict[each]['name'].lower()
        employee.employeeDict[each]['surname'] = employee.employeeDict[each]['surname'].lower()
        if filter1.match(employee.employeeDict[each]['name']) and filter2.match(
                employee.employeeDict[each]['surname']):
            isEmp = True
            empId = each
            empName = employee.employeeDict[each]['name']
            empSurname = employee.employeeDict[each]['surname']
            empDob = employee.employeeDict[each]['dob']
            empAddress = employee.employeeDict[each]['address']
            empEmail = employee.employeeDict[each]['email']
            empPhoneNumber = employee.employeeDict[each]['phoneNumber']
            empGender = employee.employeeDict[each]['gender']
            empSalary = employee.employeeDict[each]['salary']
    if isEmp:
        print(
            f'Found guest:\nId: {empId}\nName: {empName.capitalize()} {empSurname.capitalize()}\nDate of birth: {empDob}\n'
            f'Address: {empAddress}\nEmail: {empEmail}\nPhone number: {empPhoneNumber}\nSalary: {empSalary}\n'
            f'Gender: {empGender}\n')


def __searchEmployeeByNameJson(name, surname):
    filter1 = re.compile(name.lower())
    filter2 = re.compile(surname.lower())
    with open(fileEmp) as f:
        dictEmp = json.load(f)
    for each in dictEmp["emp_details"]:
        if filter1.match(each['name'].lower()) and filter2.match(each['surname'].lower()):
            print(f'Found employee\nName: {each["name"]} {each["surname"]}\nID: {each["ID"]}\nDate of birth: '
                  f'{each["dob"]}\nGender: {each["gender"]}\nAddress: {each["address"]}\nEmail: {each["email"]}\n'
                  f'Phone: {each["phoneNumber"]}\nSalary: {each["salary"]}\n'
                  f'Work start date: {each["workStartDate"]}\nPosition: {each["position"]}\n')


def __deleteEmployee(empId):
    try:
        if empId in employee.employeeDict:
            employee.employeeDict = {key: val for key, val in employee.employeeDict.items() if key != empId}
            print(f'Employee with ID {empId} deleted\n')
        else:
            print(f'Guest with ID {empId} does not exist')
    except TypeError as er:
        print("Invalid data")


def __deleteEmployeeJson(empId):
    try:
        with open(fileEmp) as f:
            dictEmp = json.load(f)
        index = None
        for i in range(len(dictEmp['emp_details'])):
            if dictEmp['emp_details'][i]['ID'] == empId:
                index = i
        dictEmp['emp_details'].pop(index)

        with open(fileEmp, 'w') as f:
            json.dump(dictEmp, f, indent=4)
    except TypeError as er:
        print("invalid data!")


def __showAllGuests():
    numberOfGuests = len(myGuest.dictOfGuests)
    print(f' There are {numberOfGuests} guests:')
    for each in myGuest.dictOfGuests:
        __searchGuestById(each)


def __showAllGuestsJson():
    with open(fileGuest) as f:
        dictGuest = json.load(f)
    numberOfGuest = len(dictGuest["guest_details"])
    print(f' There are {numberOfGuest} guests:')
    for each in dictGuest["guest_details"]:
        __searchGuestByIdJson(each['id'])


def __showAllEmployees():
    numberOfEmployees = len(employee.employeeDict)
    print(f' There are {numberOfEmployees} guests:')
    for each in employee.employeeDict:
        __searchEmployeeById(each)


def __showAllEmployeeJson():
    with open(fileEmp) as f:
        dictEmp = json.load(f)
    numberOfEmp = len(dictEmp["emp_details"])
    print(f'There are {numberOfEmp} employee:')
    for each in dictEmp["emp_details"]:
        __searchEmployeeByIdJson(each['ID'])


def isReadyRoom(self):
    isRoom = False
    for r in room.rooms:
        if room.rooms[r]['type'] is self.roomType and room.rooms[r]['status'] is Status.VACANT_AND_READY.name:
            isRoom = True
            break
    return isRoom


def __reserveRoom(guestId):
    if guestId in myGuest.dictOfGuests:
        roomType = myGuest.dictOfGuests[guestId]['typeOfRoom']
        days = myGuest.dictOfGuests[guestId]['CheckOutDate'].day - myGuest.dictOfGuests[guestId]['checkInDate'].day
        for eachRoom in room.rooms:
            if room.rooms[eachRoom]['type'] == roomType and room.rooms[eachRoom]['status'] \
                    == Status.VACANT_AND_READY.name:
                room.rooms[eachRoom]['status'] = Status.OCCUPIED.name
                fee = room.rooms[eachRoom]['price'] * days
                myGuest.dictOfGuests[guestId]['roomNumber'] = eachRoom
                myGuest.dictOfGuests[guestId]['fee'] = fee
                print(f"\nFor guest {myGuest.dictOfGuests[guestId]['name']} {myGuest.dictOfGuests[guestId]['surname']}"
                      f" reserved room number {eachRoom} and fee is {fee} AMD\n")
                break
            else:
                print(f"\nNot found free room with type {roomType}!\n")
    else:
        print("\nGuest not found!\n")


def updateGuestInfoJson():
    pass



def showResult():
    val = input("List of guest: 1\n"
                "List of employees: 2\n"
                "Rooms: 3\n"
                "Search guest by ID: 4\n"
                "Search guest by name: 5\n"
                "Search employee by ID: 6\n"
                "Search employee by name: 7\n"
                "Add guest: 8\n"
                "Add employee: 9\n"
                "Add room: 10\n"
                "Delete guest: 11\n"
                "Delete employee: 12\n"
                "Delete room: 13\n"
                "Reserve room: 14\n"
                "For exit: 0\n"
                "Put here: ")
    if val == '1':
        __showAllGuests()
        return showResult()
    elif val == '2':
        __showAllEmployees()
        return showResult()
    elif val == '3':
        __showRooms()
        return showResult()
    elif val == '4':
        id = input('Please input guest ID number: ')
        __searchGuestById(id)
        return showResult()
    elif val == '5':
        name = input('Please input guest name: ')
        surname = input('Please input guest surname: ')
        __searchGuestByName(name, surname)
        return showResult()
    elif val == '6':
        id = input('Please, input employee ID number: ')
        __searchEmployeeById(id)
        return showResult()
    elif val == '7':
        name = input("Input employee name: ")
        surname = input("Input employee surname: ")
        __searchEmployeeByName(name, surname)
        return showResult()
    elif val == '8':
        name = input('name: ')
        surname = input('surname: ')
        dob = datetime.datetime.strptime(input('Enter birth date(yyyy-mm-dd): '), "%Y-%m-%d")
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
        checkInDate = datetime.datetime.strptime(input('Enter check in date(yyyy-mm-dd): '), "%Y-%m-%d")
        checkOutDate = datetime.datetime.strptime(input('Enter check out date(yyyy-mm-dd): '), "%Y-%m-%d")
        roomType = input('roomType: ')
        myGuest.Guest(Person(name, surname, dob, id, Address(zipCode, country_key, state, city, street, home,
                                                             apartment), email, phone, gender), checkInDate, checkOutDate,
                      roomType).addGuest()
        return showResult()
    elif val == '9':
        name = input('name: ')
        surname = input('surname: ')
        dob = datetime.datetime.strptime(input('Enter birth date(yyyy-mm-dd): '), "%Y-%m-%d")
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
        workStartDate = datetime.datetime.strptime(input('Enter work start date(yyyy-mm-dd): '), "%Y-%m-%d")
        position = input('position: ')
        employee.Employee(name, surname, dob, id, Address(zipCode, country_key, state, city, street, home, apartment),
                          email, phone, gender, salary, workStartDate, position).addEmployee()
        return showResult()
    elif val == '10':
        roomNumber = input('number of room: ')
        status = input('room status. It should be VACANT_AND_READY, ON_CHANGE, DO_NOT_DISTURB,'
                       'CLEANING_IN_PROGRESS, SLEEP_OUT, ON_QUEUE, SKIPPER, OUT_OF_ORDER, OUT_OF_SERVICE, LOCKOUT,'
                       ' OCCUPIED')
        roomType = input('type of room. It should be SINGLE, DOUBLE, TRIPLE, QUAD, QUEEN, KING, TWIN, DOUBLE_DOUBLE,'
                         'STUDIO')
        room.Room(roomNumber, status, roomType).addRoom()
    elif val == '11':
        guestId = input('Input guest ID number: ')
        __deleteGuest(guestId)
        return showResult()
    elif val == '12':
        empId = input("Input employee ID number: ")
        __deleteEmployee(empId)
        return showResult()
    elif val == '13':
        roomNum = input('Input room number: ')
        __deleteRoom(roomNum)
        return showResult()
    elif val == '14':
        guestId = input("Input guest ID: ")
        __reserveRoom(guestId)
        return showResult()
    else:
        print('invalid value')
        return showResult()


def showResultJson():
    val = input("List of guest: 1\n"
                "List of employees: 2\n"
                "Rooms: 3\n"
                "Search guest by ID: 4\n"
                "Search guest by name: 5\n"
                "Search employee by ID: 6\n"
                "Search employee by name: 7\n"
                "Add guest: 8\n"
                "Add employee: 9\n"
                "Add room: 10\n"
                "Delete guest: 11\n"
                "Delete employee: 12\n"
                "Delete room: 13\n"
                "For exit: 0\n"
                "Put here: ")
    if val == '1':
        __showAllGuestsJson()
        return showResultJson()
    elif val == '2':
        __showAllEmployeeJson()
        return showResultJson()
    elif val == '3':
        __showRoomsJson()
        return showResultJson()
    elif val == '4':
        id = input('Please input guest ID number: ')
        __searchGuestByIdJson(id)
        return showResultJson()
    elif val == '5':
        name = input('Please input guest name: ')
        surname = input('Please input guest surname: ')
        __searchGuestByNameJson(name, surname)
        return showResultJson()
    elif val == '6':
        id = input('Please, input employee ID number: ')
        __searchEmployeeByIdJson(id)
        return showResultJson()
    elif val == '7':
        name = input("Input employee name: ")
        surname = input("Input employee surname: ")
        __searchEmployeeByNameJson(name, surname)
        return showResultJson()
    elif val == '8':
        name = input('name: ')
        surname = input('surname: ')
        dob = datetime.datetime.strptime(input('Enter birth date(yyyy-mm-dd): '), "%Y-%m-%d")
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
        checkInDate = datetime.datetime.strptime(input('Enter check in date(yyyy-mm-dd): '), "%Y-%m-%d")
        checkOutDate = datetime.datetime.strptime(input('Enter check out date(yyyy-mm-dd): '), "%Y-%m-%d")
        roomType = input('roomType: ')
        myGuest.Guest(Person(name, surname, dob, id, Address(zipCode, country_key, state, city, street, home,
                                                             apartment), email, phone, gender), checkInDate, checkOutDate,
                      roomType).addGuestJson()
        return showResult()
    elif val == '9':
        name = input('name: ')
        surname = input('surname: ')
        dob = datetime.datetime.strptime(input('Enter birth date(yyyy-mm-dd): '), "%Y-%m-%d")
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
        workStartDate = datetime.datetime.strptime(input('Enter work start date(yyyy-mm-dd): '), "%Y-%m-%d")
        position = input('position: ')
        employee.Employee(name, surname, dob, id, Address(zipCode, country_key, state, city, street, home, apartment),
                          email, phone, gender, salary, workStartDate, position).addEmployee()
        return showResultJson()
    elif val == '10':
        roomNumber = input('number of room: ')
        status = input('room status. It should be VACANT_AND_READY, ON_CHANGE, DO_NOT_DISTURB,'
                       'CLEANING_IN_PROGRESS, SLEEP_OUT, ON_QUEUE, SKIPPER, OUT_OF_ORDER, OUT_OF_SERVICE, LOCKOUT,'
                       ' OCCUPIED')
        roomType = input('type of room. It should be SINGLE, DOUBLE, TRIPLE, QUAD, QUEEN, KING, TWIN, DOUBLE_DOUBLE,'
                         'STUDIO')
        room.Room(roomNumber, status, roomType).addRoomJson()
    elif val == '11':
        guestId = input('Input guest ID number: ')
        __deleteGuestJson(guestId)
        return showResultJson()
    elif val == '2':
        empId = input("Input employee ID number: ")
        __deleteEmployeeJson(empId)
        return showResultJson()
    elif val == '13':
        roomNum = input('Input room number: ')
        __deleteRoomJson(roomNum)
        return showResultJson()
    elif val == '0':
        print("good by!")
    else:
        print('invalid value')
        return showResultJson()


if __name__ == '__main__':
    emp1 = Employee("Aram", "Ananyan", datetime.datetime(2001, 10, 1), "AS0300400", Address("0125", "AM", "Ararat",
                                                                                        "Artashat", "Vardananc", 15),
                    "aram.ananyan@gmail.com", "+37455202014", Gender.MALE.name, 245000, datetime.date(2020, 2, 1),
                    Position.BELL_BOY.name)
    emp1.addEmployee()

    emp2 = Employee('Araz', 'Margaryan', datetime.date(1975, 5, 12), 'AK0300256', Address('00024', 'AM', 'Yerevan',
                                                                                          'Yerevan', 'Komitas Ave',
                                                                                          27),
                    'y5ttr7mggoi@temporary-mail.net', '(374 10)519904', Gender.MALE.name, 560000,
                    datetime.date(2010, 5, 1), Position.DOCTOR.name)
    emp2.addEmployee()
    emp3 = Employee("Hmayak", "Badalyan", datetime.date(1969, 12, 1), "AS0587985", Address("0079", "AM", "Yerevan",
                                                                                           "Yerevan", "Leningradyan",
                                                                                           26),
                    "iih3jsi361@temporary-mail.net", "(374 10)519904", Gender.MALE.name, 1160000,
                    datetime.date(2010, 5, 1), Position.MANAGER.name)
    emp3.addEmployee()
    emp4 = Employee("Anahit", "Nazaryan", datetime.date(1972, 11, 22), "AN0458960", Address("0015", "AM", "Yerevan",
                                                                                           "Yerevan", "Azatutyan",
                                                                                           25, 16),
                    "anahit.nazaryan@gmail.com", "(374 10)621254", Gender.FEMALE.name, 195000,
                    datetime.date(2018, 5, 1), Position.HOTEL_CLEANER.name)
    emp4.addEmployee()
    r1 = Guest(Person('Arman', 'Gasparyan', datetime.date(1986, 8, 20), 'AK0300400',
                      Address('0256', 'AM', 'Armavir', 'Metsamor', 'Vardananc', 23, 20),
                      'arman.aleksanyan@gmail.com', '037455898979', Gender.MALE.name), datetime.date(2021, 10, 15),
               datetime.date(2021, 10, 20), roomType=RoomType.TWIN.name)
    r2 = Guest(Person('Nelly', 'Karapetyan', datetime.date(1990, 6, 22), 'AM0345800',
                      Address('0156', 'AM', 'Yerevan', 'Yerevan', 'Baghramyan', 18),
                      'nellikarap@gmail.com', '037441445464', Gender.FEMALE.name),
               datetime.date(2021, 10, 16),
               datetime.date(2021, 10, 28), roomType=RoomType.DOUBLE.name)
    r3 = Guest(Person('John', 'Smith', datetime.date(1978, 11, 5), 'KO040421',
                      Address('0876', 'GB', 'WORMSHILL', 'WORMSHILL', '18 Oxford Rd', 18),
                      'ddeqex152ab@temporary-mail.net', '7219 89095464'), datetime.date(2021, 10, 10),
               datetime.date(2021, 10, 17), roomType=RoomType.SINGLE.name)
    r4 = Guest(Person('Anna', 'Bormotova', datetime.date(1988, 10, 14), '035698756',
                      Address('0689', 'RU', 'Volgogradskaya oblast', 'Volzhskiy', 'Molodezhnaya', 36, 109),
                      'dgltu7pc5rn@temporary-mail.net', '+7(8443)35-64217', Gender.FEMALE.name),
               datetime.date(2021, 10, 14), datetime.date(2021, 10, 19), roomType=RoomType.KING.name)
    r5 = Guest(Person('Aggelos', 'Glarallis', datetime.date(1997, 11, 23), 'G01254789',
                      Address('480 60', 'GR', 'Epirus', 'Parga', 'Anexartesias', 63),
                      'aggelos.glarallis@gmail.com', '2684 032700'),
               datetime.date(2021, 10, 18), datetime.date(2021, 10, 25), roomType=RoomType.TRIPLE.name)
    r6 = Guest(Person('Narek', 'Sargsyan', datetime.date(1991, 10, 8), 'AK04050608',
                      Address('02589', 'AM', 'Yerevan', 'Yerevan', 'Alaverdyan', 15),
                      'nar.sargsyan@gmail.com', '+37491454548'),
               datetime.date(2021, 11, 20), datetime.date(2021, 11, 26), roomType=RoomType.KING.name)
    r1.addGuest()
    r2.addGuest()
    r3.addGuest()
    r4.addGuest()
    r5.addGuest()
    r6.addGuest()
    # r1.addGuestJson()
    # r2.addGuestJson()
    # r3.addGuestJson()
    # r4.addGuestJson()
    # r5.addGuestJson()
    # r6.addGuestJson()
    room0 = Room('201', Status.VACANT_AND_READY.name, RoomType.KING.name)
    room1 = Room('202', Status.VACANT_AND_READY.name, RoomType.TWIN.name)
    room2 = Room('203', Status.VACANT_AND_READY.name, RoomType.KING.name)
    room3 = Room('204', Status.VACANT_AND_READY.name, RoomType.SINGLE.name)
    room4 = Room('205', Status.VACANT_AND_READY.name, RoomType.DOUBLE_DOUBLE.name)
    room5 = Room('206', Status.VACANT_AND_READY.name, RoomType.QUEEN.name)
    room6 = Room('207', Status.VACANT_AND_READY.name, RoomType.STUDIO.name)
    room7 = Room('208', Status.VACANT_AND_READY.name, RoomType.TWIN.name)
    room8 = Room('209', Status.VACANT_AND_READY.name, RoomType.QUEEN.name)
    room9 = Room('210', Status.VACANT_AND_READY.name, RoomType.TRIPLE.name)
    room10 = Room('301', Status.VACANT_AND_READY.name, RoomType.DOUBLE_DOUBLE.name)
    room11 = Room('302', Status.VACANT_AND_READY.name, RoomType.DOUBLE_DOUBLE.name)
    room12 = Room('303', Status.VACANT_AND_READY.name, RoomType.DOUBLE.name)
    room13 = Room('304', Status.VACANT_AND_READY.name, RoomType.DOUBLE.name)
    room14 = Room('305', Status.VACANT_AND_READY.name, RoomType.STUDIO.name)
    room15 = Room('306', Status.VACANT_AND_READY.name, RoomType.SINGLE.name)
    room16 = Room('307', Status.VACANT_AND_READY.name, RoomType.STUDIO.name)
    room17 = Room('308', Status.VACANT_AND_READY.name, RoomType.TWIN.name)
    room18 = Room('309', Status.VACANT_AND_READY.name, RoomType.TRIPLE.name)
    room19 = Room('310', Status.VACANT_AND_READY.name, RoomType.DOUBLE.name)
    # room10.addRoom()
    # room1.addRoom()
    # room2.addRoom()
    # room3.addRoom()
    # room4.addRoom()
    # room5.addRoom()
    # room6.addRoom()
    # room7.addRoom()
    # room8.addRoom()
    # room9.addRoom()
    # room10.addRoom()
    # room11.addRoom()
    # room12.addRoom()
    # room13.addRoom()
    # room14.addRoom()
    # room15.addRoom()
    # room16.addRoom()
    # room17.addRoom()
    # room18.addRoom()
    # room19.addRoom()

    showResultJson()

