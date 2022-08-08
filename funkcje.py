import datetime
import time


def clear_screen():
    for i in range(21):
        print("\n")


def month_converter(data):

    months = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień",
              "Październik", "Listopad", "Grudzień"]

    if type(data) == str:
        month = months.index(data) + 1
        return month

    elif type(data) == int:
        month = months[data - 1]
        return month

    else:
        print("\n**Złe użycie funckcji month converter**\n")


def czas(dane):

    if dane == "year":
        return datetime.date.today().year  # Type int

    elif dane == "month":
        return datetime.date.today().month

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


