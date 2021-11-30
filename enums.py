from enum import Enum


class Gender(Enum):
    MALE = 1
    FEMALE = 2


class Status(Enum):
    VACANT_AND_READY = 1
    ON_CHANGE = 2
    DO_NOT_DISTURB = 3
    CLEANING_IN_PROGRESS = 4
    SLEEP_OUT = 5
    ON_QUEUE = 6
    SKIPPER = 7
    OUT_OF_ORDER = 8
    OUT_OF_SERVICE = 9
    LOCKOUT = 10
    OCCUPIED = 11


class RoomType(Enum):
    SINGLE = 1
    DOUBLE = 2
    TRIPLE = 3
    QUAD = 4
    QUEEN = 5
    KING = 6
    TWIN = 7
    DOUBLE_DOUBLE = 8
    STUDIO = 9


class Position(Enum):
    MANAGER = 1
    CHEF = 2
    COOK_HELPER = 3
    LAUNDRY_WORKER = 4
    DOCTOR = 5
    ROOM_ATTENDANT = 6
    WAITER = 7
    DELIVERY_DRIVER = 8
    HOTEL_CLEANER = 9
    BELL_BOY = 10
    PORTER = 11
    CASHIER = 12
    ACCOUNTANT = 13
    FRONT_DESK = 14
    ELECTRICIAN = 15
    RECEPTIONIST = 16
    RESTAURANT_MANAGER = 17
