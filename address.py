import dictionaries


class Address:
    def __init__(self, zipCode, country_key, state, city, street, home, apartment=None):
        self.__zipCode = zipCode
        self.__state = state
        self.__city = city
        self.__street = street
        self.__home = home
        self.__apartment = apartment
        try:
            if country_key in dictionaries.COUNTRIES:
                self.__country = country_key
        except AttributeError as e:
            print("invalid value")

    @property
    def zipCode(self):
        return self.__zipCode

    @zipCode.setter
    def zipCode(self, newZipCode):
        self.__zipCode = newZipCode

    @property
    def country(self):
        try:
            return self.__country
        except AttributeError as e:
            print("invalid country code")

    @country.setter
    def country(self, newCountry):
        self.__country = newCountry

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, newState):
        self.__state = newState

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, newStreet):
        self.__street = newStreet

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, newCity):
        self.__city = newCity

    @property
    def home(self):
        return self.__home

    @home.setter
    def home(self, newHome):
        self.__home = newHome

    @property
    def apartment(self):
        return self.__apartment

    @apartment.setter
    def apartment(self, newApartment):
        self.__apartment = newApartment