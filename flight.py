from plane import Plane
from date import Date


class Flight(Date, Plane):
    def __init__(self, id_plane, flight_number, available_seats, destination, dt_boarding,
                 tm_boarding, dt_arrival, tm_arrival, price, transfers=[]):
        super(Flight, self).__init__(dt_boarding, tm_boarding, dt_arrival, tm_arrival)
        self._id_plane = id_plane
        self._flight_number = flight_number
        self._available_seats = available_seats
        self._destination = destination
        self._price = price
        self._transfers = transfers

    def __setattr__(self, key, value):
        match(key):
            case "_id_plane":
                if isinstance(value, int):
                    return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")

            case "_flight_number":
                if isinstance(value, int):
                     return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")

            case "_available_seats":
                if isinstance(value, int) and value >= 0:
                    return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")

            case "_destination":
                if isinstance(value, str):
                    return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")

            case "_price":
                if isinstance(value, int):
                    return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")
        return object.__setattr__(self, key, value)

    def get_info(self):
            return self._id_plane, self._flight_number,  \
                   self._available_seats,                \
                   self._destination, self._dt_boarding, \
                   self._tm_boarding, self._dt_arrival,  \
                   self._tm_arrival, self._price, self._transfers

    def set_info(self, id_plane, flight_number, available_seats, destination, price):
        self._id_plane = id_plane
        self._flight_number = flight_number
        self._available_seats = available_seats
        self._destination = destination
        self._price = price

    def get_transfers(self):
        return self._transfers

    def add_transfers(self, transfer):
        self._transfers.append(transfer)

    def buy_ticket(self):
        self._available_seats -= 1

    def check_seats(self):
        if self._available_seats <= 0:
            return False
        else:
            return True

