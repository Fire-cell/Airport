class Plane:
    def __init__(self, model, id_plane, number_seats):
        self._model = model                    #модель літака
        self._id_plane = id_plane              #id літака
        self._number_seats = number_seats      #к-сть сидінь

    def __setattr__(self, key, value): #Перевіряє на правильність присвоєння
        match(key):
            case "_model":
                if isinstance(value, str):
                    return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")

            case "_id_plane":
                if isinstance(value, int) and value > 0:
                    return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")
            case "_number_seats":
                if isinstance(value, int) and value > 0:
                    return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")

    def get_info(self): # повертає інформацію (геттер)
        return self._model, self._id_plane, self._number_seats

    def set_info(self, model, id_plane, number_seats): #дозволяє змінити інформацію (сеттер)
            self._model = model                   #модель літака
            self._id_plane = id_plane             #id літака
            self._number_seats = number_seats     #к-сть сидінь

