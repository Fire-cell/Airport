class Date:
    def __init__(self, dt_boarding, tm_boarding, dt_arrival, tm_arrival):
        self._dt_boarding = dt_boarding
        self._tm_boarding = tm_boarding
        self._dt_arrival = dt_arrival
        self._tm_arrival = tm_arrival

    def __setattr__(self, key, value):
        match(key):
            case "_dt_boarding":
                if isinstance(value, str):
                    return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")

            case "_dt_arrival":
                if isinstance(value, str):
                    return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")

            case "_tm_boarding":
                if isinstance(value, str):
                    return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")

            case '_tm_arrival':
                if isinstance(value, str):
                    return object.__setattr__(self, key, value)
                raise TypeError("Помилка типів присвоєння")

    def set_time(self, dt_boarding, tm_boarding, dt_arrival, tm_arrival):
        self._dt_boarding = dt_boarding
        self._tm_boarding = tm_boarding
        self._dt_arrival = dt_arrival
        self._tm_arrival = tm_arrival

    def get_time(self):
        return self._dt_boarding, self._tm_boarding, self._dt_arrival, self._tm_arrival
