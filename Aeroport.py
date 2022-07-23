from display_functions import *
from storage import *


def main():
    print('-------Головне меню---------')
    print("1) Створити літак ")
    print("2) Cтворити рейс ")
    print("3) Cтворити квиток ")
    print("4) Зберегти інформацію в файли ")
    print("5) Зчитати інформацію з файлів ")
    print("6) Вивести всю інформацію")
    print("7) Очистити файли ")
    print("8) Користувацьке меню ")
    print("9) Меню налаштувань")
    print("0) Завершити роботу")

    arrplanes = []
    arrflights = []
    arrtickets = []
    while True:

        print('\n')
        action = input("Виберіть дію за індексом: ")

        match action:
            case "1":
                print("Створити літак: ")
                model = input("Введіть модель літака: ")
                print("id немає повторюватись із іншими літаками")
                # Перевірка на повторення id
                id_plane = int(input("Введіть id літака: "))
                check = False
                for i in range(len(arrplanes)):
                    obj = arrplanes[i]
                    if int(obj.get_info()[1]) == id_plane:
                        check = True
                        print("id введено правильно")
                        break

                if check:
                    raise ValueError("Неправильно вибране id")

                number_seats = int(input("Введіть кількість сидінь в літаку: "))

                arrplanes.append(Plane(model, id_plane, number_seats))

            case "2":
                print("Cтворити рейс ")
                print("Виберіть літак на який буде створено рейс, ввівши його id")
                for i in range(len(arrplanes)):
                    obj = arrplanes[i].get_info()
                    show_plane(obj)
                id_plane = int(input("Виберіть id літака: "))
                check = True
                pl = 0
                for pl in range(len(arrplanes)):
                    obj = arrplanes[pl]
                    if int(obj.get_info()[1]) == id_plane:
                        check = False
                        print("id введено правильно")
                        break

                if check:
                    raise NameError("Неправильно вибране id")

                flight_number = int(input("Введіть номер рейсу: "))
                check = True
                obj = object
                for i in range(len(arrflights)):
                    if arrflights[i].get_info()[1] == flight_number:
                        obj = arrflights[i].get_info()[1]
                        check = False
                        break

                if not check:
                    raise ValueError("Даний рейс {} вже зареєстрований".format(flight_number))

                available_seats = int(input("Введіть к-сть вільних місць: "))
                if arrplanes[pl].get_info()[2] <= available_seats:
                    raise ValueError("У літаку всього {}".format(arrplanes[pl].get_info()[2]))

                destination = input("Введіть місце призначення: ")
                dt_boarding = input("Введіть дату посадки у виді DD.MM.YY: ")
                tm_boarding = input("Введіть час посадки у виді HH:MM: ")
                dt_arrival = input("Введіть дату прибуття у виді DD.MM.YY: ")
                tm_arrival = input("Введіть час прибуття у виді DD.MM.YY: ")
                price = int(input("Введіть ціну рейсу: "))

                arrflights.append(Flight(id_plane, flight_number, available_seats, destination, dt_boarding,
                                         tm_boarding, dt_arrival, tm_arrival, price, []))

                print("Додати пересадки для даного рейсу?")
                print("Так - [1]; \t Ні- [0]")
                while (True):
                    action = input("Ваш вибір: ")
                    match (action):
                        case "1":
                            n = input("Введіть місце перасадки: ")
                            arrflights[- 1].set_transfers(n)
                            print("Чи потрібно додати ще одну пересадку?")
                        case "0":
                            print("Рейс успішно додано")
                            break
                        case _:
                            print("Неправильно вибрана дія")

            case "3":
                print("Створити квиток: ")
                print("Виберіть рейс на який буде створено ваш квиток, ввівши номер рейсу")
                print("Cписок рейсів:")
                for i in range(len(arrflights)):
                    obj = arrflights[i].get_info()
                    show_flight(obj)
                flight_number = int(input("Введіть номер рейсу: "))
                check = True
                i = 0
                for i in range(len(arrflights)):
                    if int(arrflights[i].get_info()[1]) == flight_number:
                        if not arrflights[i].check_seats():
                            raise NameError("Вибачте, але доступних місць на даний рейс немає")
                        check = False
                        print("Номер рейсу введено правильно.")
                        break

                if check:
                    raise NameError("Неправильно введений номер рейсу")

                # Перевіряємо к-сть доступних місць на рейс
                if arrflights[i].check_seats():
                    print("Над даний рейс є доступні місця")
                else:
                    raise ValueError('Вибачте, але на даний рейс немає доступних місць')

                passenger_name = input("Введіть ПІБ пасажира: ")
                seat_number = int(input("Введіть номер сидіння: "))

                arrtickets.append(Ticket(passenger_name, flight_number, seat_number, arrflights[i].get_info()[8]))
                arrflights[i].buy_ticket()  # зменшуємо на 1 кількість доступних місць на рейс
            # -------------------------------------------------------------------------------------------
            case "4":  # Зберігає інформацію до файлів
                sv_planes(arrplanes)
                sv_flights(arrflights)
                sv_tickets(arrtickets)
                print("Інформацію збережено в файл")

            # -------------------------------------------------------------------------------------------

            case "5":  # Зчитати інформацію з файлу

                rd_planes(arrplanes)
                rd_flights(arrflights)
                rd_tickets(arrtickets)
                print("Інформацію зчитано із файлу")

            # ----------------------------------------------------------------------------

            case "6":  # Виведення всієї інформації на консоль

                print("Наявні літаки:")
                for i in range(len(arrplanes)):
                    obj = arrplanes[i].get_info()
                    show_plane(obj)

                print("Наявні рейси:")
                for i in range(len(arrflights)):
                    obj = arrflights[i].get_info()
                    show_flight(obj)

                print("Куплені квитки:")
                for i in range(len(arrtickets)):
                    obj = arrtickets[i].get_info()
                    show_ticket(obj)

            case "7":  # Очистити файли
                print("7) Очистити файли ")
                with open("Plane.cvs", "w") as f:
                    pass

                with open("Flights.cvs", "w") as f:
                    pass

                with open("Tickets.cvs", "w") as f:
                    pass

            case "8":
                request_menu(arrplanes, arrflights, arrtickets)

            case "9":
                properties_menu(arrplanes, arrflights, arrtickets)

            case "0":
                print("Роботу завершено.")
                return

            case other:
                print("Дію не знайдено")
                return


def request_menu(arrplanes, arrflights, arrtickets):
    print("------Меню запросів--------------")
    print("1) Вільні місця на заданий рейс")
    print("2) Список рейсів без проміжних посадок")
    print("3) Які рейси обслуговуються заданим літаком")
    print("4) Як завантажені літаки на заданий рейс по датах")
    print("5) Найдорожчий рейс")
    print("6) Якими рейсами можна замінити літак (багато вільних місць)")
    print("0) Повернутися до головного меню \n")


    while True:
        action = input("Виберіть дію за індексом: ")
        match action:
            case "1":
                print("Вільні місця на рейс")
                n = int(input("Введіть номер рейсу: "))
                for i in range(len(arrflights)):
                    if arrflights[i].get_info()[1] == n:
                        print("Кількість вільних місць на рейс: {}".format(arrflights[i].get_info()[2]))
                        break

            case "2":
                print("Список рейсів без проміжних посадок")
                for i in range(len(arrflights)):
                    if arrflights[i].get_info()[9] == []:
                        show_flight(arrflights[i].get_info())

            case "3":
                print("Рейси які обслуговуються заданим літаком ")
                print("Список літаків")
                for i in range(len(arrplanes)):
                    obj = arrplanes[i].get_info()
                    show_plane(obj)
                n = int(input("Введіть id літака: "))
                for i in range(len(arrflights)):
                    if arrflights[i].get_info()[0] == n:
                        obj = arrflights[i].get_info()
                        show_flight(obj)

            case "4":
                print("Завантажені літаки на заданий рейс по датах")
                flight_num = int(input("Введіть рейс: "))
                for i in range(len(arrflights)):
                    if arrflights[i].get_info()[1] == flight_num:
                        print("Номер рейсу: {}".format(flight_num))
                        display_time(arrflights[i].get_time())
                        num_seats = 0
                        for j in range(len(arrplanes)):
                            if arrplanes[j].get_info()[1] == arrflights[i].get_info()[i]:
                                num_seats = arrplanes[j].get_info()[2]
                        print("Загруженість літака: {} із {}".format(num_seats - arrflights[i].get_info()[2], num_seats))



            case "5":
                print("Найдорожчий рейс")
                i = pointer = 0
                expensivest_flight = 0
                for i in range(len(arrflights)):
                    if expensivest_flight < arrflights[i].get_info()[8]:
                        expensivest_flight = arrflights[i].get_info()[8]
                        pointer = i
                show_flight(arrflights[pointer].get_info())

            case "6":
                print("6) Якими рейсами можна замінити літак (багато вільних місць)")
                flight_num = int(input("Введіть номер вашого рейсу: "))

                i = 0 # вказівник на позицію об'єкта який ми шукаємо
                check = False
                for i in range(len(arrflights)):
                    obj = arrflights[i].get_info()
                    if obj[1] == flight_num:
                        check = True
                        break
                if not check:
                    raise ValueError("Такого рейсу не існує")

                for j in range(len(arrflights)):
                    obj = arrflights[j].get_info()

                    if obj[3] == arrflights[i].get_info()[3] and obj[1] != arrflights[i].get_info()[1]:
                        show_flight(obj)

            case "0":
                return main()

            case other:
                print("Дію не знайдено")
                return

def properties_menu(arrplanes, arrflights, arrtickets):
    print("1) Видалення літака")
    print("2) Видалення рейсу")
    print("3) Видалення квитка")
    while True:
        action = input("Виберіть дію за індексом: ")
        match action:
            case "1":
                print("Видалення літака")
                print("Наявні літаки:")
                for i in range(len(arrplanes)):
                    obj = arrplanes[i].get_info()
                    show_plane(obj)
                    id_plane = int(input("Введіть номер id літака: "))
                    i = 0
                    check = False
                    for i in range(len(arrplanes)):
                        if arrplanes[i].getinfo()[1] == id_plane:
                            check = True
                            del arrtickets[i]
                            break
                    if not check:
                        raise ValueError("Немає такого літака")


            case "2":
                print("Видалення рейсу")
                print("Наявні рейси:")
                for i in range(len(arrflights)):
                    obj = arrflights[i].get_info()
                    show_flight(obj)
                    flight_num = int(input("Введіть номер рейсу: "))
                    i = 0
                    check = False
                    for i in range(len(arrflights)):
                        if arrflights[i].getinfo()[1] == flight_num:
                            check = True
                            del arrflights[i]
                            break
                    if not check:
                        raise ValueError("Немає такого рейсу")


            case "3":
                print("Видалення квитка")
                print("Куплені квитки:")
                for i in range(len(arrtickets)):
                    obj = arrtickets[i].get_info()
                    show_ticket(obj)
                    flight_num = int(input("Введіть номер рейсу: "))
                    seat_num = int(input("Введіть номер сидіння: "))
                    i = 0
                    check = False
                    for i in range(len(arrflights)):
                        if arrtickets[i].getinfo()[1] == flight_num and arrtickets[i].getinfo()[2] == seat_num :
                            check = True
                            del arrtickets[i]
                            break
                    if not check:
                        raise ValueError("Немає такого квитка")


            case "0":
                return main()

            case other:
                print("Дію не знайдено")
                return

main()


