from address import Address
from enums import Gender
import numpy as np
import datetime
from datetime import date


class Person:
    def __init__(self, name, surname, dob, id, address, email, phoneNumber, gender=Gender.MALE.name):
        self.__dob = dob
        self.__id = id
        self.__address = address
        self.__email = email
        self.__phoneNumber = phoneNumber
        self.__gender = gender
        Address.__address = address

        if dob.year < 0:
            print(f'{dob.year} is future!')

        if name.isalpha():
            self.__name = name

        else:
            self.__name = "no name"
            print("Only letters may be used in the name")

        if surname.isalpha():
            self.__surname = surname
        else:
            self.__surname = "no surname"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, newSurname):
        self.__surname = newSurname

    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, newDob):
        self.__dob = newDob

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, newId):
        self.__id = newId

    @property
    def address(self):
        thisAddress = f"{self.__address.zipCode}, {self.__address.country}, {self.__address.state}," \
                      f" {self.__address.city}, {self.__address.street}, {self.__address.home}," \
                      f" {self.__address.apartment}"
        return thisAddress

    @address.setter
    def address(self, newAddress):
        if isinstance(newAddress, Address):
            self.__address = newAddress
        else:
            raise ValueError

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, newEmail):
        self.__email = newEmail

    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, newPhoneNumber):
        self.__phoneNumber = newPhoneNumber

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, newGender):
        self.__gender = newGender

if __name__ == '__main__':
    p = Person('name', 'surname', datetime.date(2001, 10, 12), 'AK0102045', Address('0214', 'AM', 'Yerevan', 'Yerevan', 'Baghramyan', '22'),
               'Name@.com', '091919191')
    print(p.address)