from person import Person
from datetime import datetime
import simplejson as json
import mysql.connector

employeeDict = {}

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1491625mel",
    database="Hotel"
)


class Employee(Person):
    def __init__(self, name, surname, dob, id, address, email, phoneNumber, gender, salary, workStartDate, position):
        super().__init__(name, surname, dob, id, address, email, phoneNumber, gender)

        self.__salary = salary
        self.__workStartDate = workStartDate
        self.__position = position

        if 0 < workStartDate.year - 16 > datetime.today().year:
            print("Is not an adult, can't work!")
        elif workStartDate.year < 0:
            print(f'{workStartDate.year} is year of the future')

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, newSalary):
        self.__salary = newSalary

    @property
    def workStartDate(self):
        return self.__workStartDate

    @workStartDate.setter
    def workStartDate(self, newWorkStartDate):
        self.__workStartDate = newWorkStartDate

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, newPosition):
        self.__position = newPosition

    def addEmployee(self):
        employeeDict[self.id] = {'name': self.name, 'surname': self.surname, 'dob': self.dob,
                                 'address': self.address, 'email': self.email,
                                 'phoneNumber': self.phoneNumber, 'gender': self.gender,
                                 'salary': self.salary, 'workStartDate': self.workStartDate,
                                 'position': self.position}

    def addEmployeeJson(self):

        formattedDob = self.dob.isoformat()
        formattedWorkStartDate = self.workStartDate.isoformat()
        jsonDob = json.dumps(formattedDob)
        jsonWorkStartDate = json.dumps(formattedWorkStartDate)
        filename = 'employee.json'

        newData = {'name': self.name, 'surname': self.surname, 'dob': jsonDob, "ID": self.id,
                   'address': self.address, 'email': self.email,
                   'phoneNumber': self.phoneNumber, 'gender': self.gender,
                   'salary': self.salary, 'workStartDate': jsonWorkStartDate,
                   'position': self.position}
        with open(filename, 'r+') as file:
            fileData = json.load(file)
            fileData["emp_details"].append(newData)
            file.seek(0)
            json.dump(fileData, file, indent=4)

    def addEmployeeDB(self):
        myCursor = myDB.cursor()
        record = (self.id, self.name, self.surname, self.dob, self.email, self.phoneNumber, self.gender, self.salary,
                  self.workStartDate, self.position, self.address)
        insert_query = 'INSERT INTO employee(empID, name, surname, dob, email, phoneNumber, gender, salary,' \
                       'workStartDate, position, address)' \
                       ' VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        myCursor.execute(insert_query, record)
        myDB.commit()





    def showInfo(self):
        print(f'Full name: {self.name} {self.surname}\ndate of birth: {self.dob}\n'
              f'Address: {self.address}\nEmail: {self.email}\nPhone number: {self.phoneNumber}\n'
              f'gender: {self.gender}\nSalary: {self.salary}\nWork start date: {self.workStartDate}\n'
              f'position: {self.position}')
