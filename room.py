import simplejson as json
from enums import Status, RoomType
import mysql.connector

rooms = {}

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1491625mel",
    database="Hotel"
)

class Room:
    def __init__(self, roomNumber, status=Status.VACANT_AND_READY.name, roomType=RoomType.SINGLE.name):
        self.__status = status
        self.__roomType = roomType
        self.__roomNumber = roomNumber
        self.__room_price = {
            'SINGLE': 20000,
            'DOUBLE': 38000,
            'TRIPLE': 45000,
            'QUAD': 50000,
            'QUEEN': 70000,
            'KING': 85000,
            'TWIN': 40000,
            'DOUBLE_DOUBLE': 60000,
            'STUDIO': 40000
        }
        # for each in dictionaries.rooms.values():
        #     if roomNumber in each:
        #         self.__roomNumber = roomNumber

    @property
    def roomNumber(self):
        try:
            return self.__roomNumber
        except AttributeError as er:
            print("that room number does not exist")

    @roomNumber.setter
    def roomNumber(self, newRoomNumber):
        self.__roomNumber = newRoomNumber

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, newStatus):
        self.__status = newStatus

    @property
    def roomType(self):
        return self.__roomType

    @roomType.setter
    def roomType(self, newRoomType):
        self.__roomType = newRoomType


    @property
    def roomPrice(self):
        if self.__roomType == RoomType.SINGLE.name:
            return self.__room_price["SINGLE"]
        elif self.__roomType == RoomType.DOUBLE.name:
            return self.__room_price["DOUBLE"]
        elif self.__roomType == RoomType.TRIPLE.name:
            return self.__room_price["TRIPLE"]
        elif self.__roomType == RoomType.QUAD.name:
            return self.__room_price["QUAD"]
        elif self.__roomType == RoomType.QUEEN.name:
            return self.__room_price["QUEEN"]
        elif self.__roomType == RoomType.KING.name:
            return self.__room_price["KING"]
        elif self.__roomType == RoomType.TWIN.name:
            return self.__room_price["TWIN"]
        elif self.__roomType == RoomType.DOUBLE_DOUBLE.name:
            return self.__room_price["DOUBLE_DOUBLE"]
        else:
            return self.__room_price["STUDIO"]

    @roomPrice.setter
    def roomPrice(self, price):
        for key in self.__room_price:
            if self.__roomType == key:
                self.__room_price[key] = price

    def addRoom(self):
        rooms[self.roomNumber] = {'status': self.status, 'type': self.roomType, 'price': self.roomPrice}


    def addRoomJson(self):
        filename = 'room.json'
        newData = {'room': self.roomNumber, 'status': self.status, 'type': self.roomType, 'price': self.roomPrice}
        with open(filename, 'r+') as file:
            fileData = json.load(file)
            fileData["room_details"].append(newData)
            file.seek(0)
            json.dump(fileData, file, indent=4)


    def addRoomDB(self):
        myCursor = myDB.cursor()
        record = (self.roomNumber, self.status, self.roomType, self.roomPrice)
        insert_query = 'INSERT INTO room(room_number, status, type, price) VALUES (%s, %s, %s, %s)'
        myCursor.execute(insert_query, record)
        myDB.commit()
        myDB.close()



    def showInfo(self):
        print(f'Room number: {self.roomNumber}\nRoom status: {self.status}\nRoom type: {self.roomType}\n'
              f'Room price: {self.roomPrice}')


