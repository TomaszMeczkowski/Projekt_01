import datetime
import time


def clear_screen():
    for i in range(21):
        print("\n")


def month_converter(data):

    months = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień",
              "Październik", "Listopad", "Grudzień"]

    if type(data) == str and data in months:
        month = months.index(data) + 1
        return month

    elif type(data) == int:
        month = months[data - 1]
        return month

    else:
        print("\n**Złe użycie funckcji month converter**\n")


def czas(dane):

    if dane == "year":
        return datetime.date.today().year  # Type INT

    elif dane == "month":
        return datetime.date.today().month  # Type INT

    elif dane == "day":
        return datetime.date.today().day

    elif dane == "hour":
        return int(time.strftime('%H', time.localtime()))

    elif dane == "min":
        return int(time.strftime('%M', time.localtime()))

    elif dane == "sec":
        return int(time.strftime('%S', time.localtime()))

    else:
        print("\n***Złe użycie funkcji czasu***\n")


def user_sleep():
    input("\nWprowadź dowolny znak żeby cofnąć:\n")


def mysql_data_converter(dane):
    data = dane.split("-")
    year = data[0]
    month = month_converter(int(str(int(data[1], 10))))  # Parsowanie stringa ze względu na fromaty 01,02 miesięcy
    day = data[2]
    return f"{day} {month} {year}"


def color_belt_picker(data):
    color_pick = None
    if data == "Biały":
        pass
    elif data == "Niebieski":
        color_pick = "blue"
    elif data == "Purpurowy":
        color_pick = "magenta"
    elif data == "Brązowy":
        color_pick = "yellow"
    elif data == "Czarny":
        color_pick = "white"

    return color_pick
