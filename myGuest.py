from enums import RoomType, Gender, Status
from person import Person
import simplejson as json
import room
import mysql.connector


dictOfGuests = {}

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*****",
    database="Hotel"
)


class Guest:
    def __init__(self, customer, checkInDate, checkOutDate, roomType):
        self.__customer = customer
        self.__checkInDate = checkInDate
        self.__checkOutDate = checkOutDate
        self.__roomType = roomType
        Person.__customer = customer

    @property
    def customer(self):
        thisCustomer = f'{self.__customer.name} {self.__customer.surname}, {self.__customer.id}, ' \
                       f'{self.__customer.dob}, {self.__customer.gender}, {self.__customer.phoneNumber},' \
                       f'{self.__customer.email}, {self.__customer.address}'
        return thisCustomer

    @customer.setter
    def customer(self, newCustomer):
        self.__customer = newCustomer

    @property
    def checkInDate(self):
        return self.__checkInDate

    @checkInDate.setter
    def checkInDate(self, newDate):
        self.__checkInDate = newDate

    @property
    def checkOutDate(self):
        return self.__checkOutDate

    @checkOutDate.setter
    def checkOutDate(self, newDate):
        self.__checkOutDate = newDate

    @property
    def roomType(self):
        return self.__roomType

    @roomType.setter
    def roomType(self, newRoomType):
        self.__roomType = newRoomType

    @property
    def roomNumber(self):
        roomNum = None
        for eachRoom in room.rooms:
            if room.rooms[eachRoom]['type'] == self.roomType and room.rooms[eachRoom][
                    'status'] is Status.VACANT_AND_READY.name:
                roomNum = eachRoom
                break
        return roomNum



    def addGuest(self):
        dictOfGuests[self.__customer.id] = {'name': self.__customer.name,
                                            'surname': self.__customer.surname,
                                            'dob': self.__customer.dob,
                                            'address': self.__customer.address,
                                            'email': self.__customer.email,
                                            'phone': self.__customer.phoneNumber,
                                            'checkInDate': self.checkInDate,
                                            'CheckOutDate': self.checkOutDate,
                                            'typeOfRoom': self.roomType,
                                            'gender': self.__customer.gender,
                                            'roomNumber': None,
                                            'fee': None}

    def addGuestJson(self):
        filename = 'guest.json'
        formattedDob = self.__customer.dob.isoformat()
        formattedCheckInDate = self.checkInDate.isoformat()
        formattedCheckOutDate = self.checkOutDate.isoformat()
        jsonDob = json.dumps(formattedDob)
        jsonCheckInDate = json.dumps(formattedCheckInDate)
        jsonCheckOutDate = json.dumps(formattedCheckOutDate)

        newData = {'name': self.__customer.name,
                   'surname': self.__customer.surname,
                   'id': self.__customer.id,
                   'dob': jsonDob,
                   'gender': self.__customer.gender,
                   'address': self.__customer.address,
                   'email': self.__customer.email,
                   'phone': self.__customer.phoneNumber,
                   'checkInDate': jsonCheckInDate,
                   'CheckOutDate': jsonCheckOutDate,
                   'typeOfRoom': self.roomType,
                   'roomNumber': None,
                   'fee': None
                   }
        with open(filename, 'r+') as file:
            fileData = json.load(file)
            fileData["guest_details"].append(newData)
            file.seek(0)
            json.dump(fileData, file, indent=4)

    def addGuestDB(self):
        myCursor = myDB.cursor()
        record = (self.__customer.id, self.__customer.name, self.__customer.surname, self.__customer.dob,
                  self.__customer.email, self.__customer.phoneNumber, self.checkInDate, self.checkOutDate,
                  self.roomType, self.__customer.gender, self.__customer.address)
        insert_query = 'INSERT INTO guest(guestID, fName, surname, dob, email, phone, checkInDate, checkOutDate,' \
                       'typeOfRoom, gender, address'') VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        myCursor.execute(insert_query, record)
        myDB.commit()
        myDB.close()


    def showInfo(self):
        print(f'Guest name: {self.__customer.name} {self.__customer.surname}\ndate of birth: {self.__customer.dob}\n'
              f'gender: {self.__customer.gender}\naddress: {self.__customer.address}\nemail: {self.__customer.email}\n'
              f'phone number: {self.__customer.phoneNumber}\ncheck in date: {self.checkInDate}\n'
              f'check out date: {self.checkOutDate}\nroom type: {self.roomType}\n')
