from flight import Flight


class Ticket(Flight):
    def __init__(self, passenger_name, flight_number, seat_number, price):
        self._passenger_name = passenger_name   #Ім'я пасажира
        self._flight_number = flight_number     #Номер рейсу
        self._seat_number = seat_number         #Номер сидіння
        self._price = price                     #Ціна квитка

    def __setattr__(self, key, value):
        match key:
            case "_passenger_name":
                if isinstance(value, str):
                    return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")

            case "_flight_number":
                if isinstance(value, int):
                    return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")

            case "_seat_number":
                if isinstance(value, int):
                    return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")

            case "_price":
                if isinstance(value, int):
                    return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")

    def get_info(self):  #Отримати інформацію про квиток
        return self._passenger_name, self._flight_number, \
               self._seat_number, self._price

    def set_info(self, passenger_name, flight_number, seat_number, price):  #Змінити інформацію про рейс
        self._passenger_name = passenger_name
        self._flight_number = flight_number
        self._seat_number = seat_number
        self._price = price
