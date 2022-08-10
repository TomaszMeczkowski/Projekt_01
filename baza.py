import mysql.connector
from funkcje import clear_screen, month_converter, czas, user_sleep
import datetime
import pathlib
import os
from termcolor import colored


class BazaDanych:

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def inicjowanie_bazy_danych(self):
        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306)
        cursor_object = db.cursor()
        cursor_object.execute("CREATE DATABASE IF NOT EXISTS klub_zt")
        db.commit()
        db.close()

    def inicjowanie_tabel(self):
        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()

        cursor_object.execute("CREATE DATABASE IF NOT EXISTS klub_zt")

        creat_table_1 = "CREATE TABLE IF NOT EXISTS osoby_trenujace" \
                        "(" \
                        "id INT NOT NULL AUTO_INCREMENT, " \
                        "imie VARCHAR(30) NOT NULL, " \
                        "nazwisko VARCHAR(45) NOT NULL, " \
                        "pas VARCHAR(15) NOT NULL," \
                        "belki INT NOT NULL, " \
                        "PRIMARY KEY (id), UNIQUE INDEX id_UNIQUE (id ASC) VISIBLE" \
                        ");"

        cursor_object.execute(creat_table_1)

        creat_table_2 = "CREATE TABLE IF NOT EXISTS karnety" \
                        "(" \
                        "id int NOT NULL, " \
                        "aktywny_karnet tinyint NOT NULL, " \
                        "miesiac varchar(45) NOT NULL, " \
                        "typ_karnetu varchar(45) NOT NULL," \
                        "dostepne_treningi_ogolnie int NOT NULL," \
                        "pozostale_treningi_w_miesiacu int NOT NULL," \
                        "plec varchar(15), " \
                        "PRIMARY KEY (id), UNIQUE KEY id_UNIQUE (id)" \
                        ")"

        cursor_object.execute(creat_table_2)

        creat_table_3 = "CREATE TABLE IF NOT EXISTS dodatkowe_info_osoby" \
                        "(" \
                        "id int NOT NULL AUTO_INCREMENT, " \
                        "pierwszy_trening date DEFAULT NULL, " \
                        "data_urodzenia date DEFAULT NULL, " \
                        "laczna_ilosc_treningow int DEFAULT NULL, " \
                        "ulubiona_technika varchar(60) DEFAULT NULL, " \
                        "PRIMARY KEY (id), UNIQUE KEY id_UNIQUE (id))"

        cursor_object.execute(creat_table_3)

        creat_table_4 = "CREATE TABLE IF NOT EXISTS statystyki_klubowe" \
                        "(id INT NOT NULL AUTO_INCREMENT," \
                        "ilosc_wejsc INT NOT NULL," \
                        "miesiac varchar(45) NOT NULL," \
                        "rok INT NOT NULL," \
                        "PRIMARY KEY (id), UNIQUE KEY id_UNIQUE (id));"

        cursor_object.execute(creat_table_4)

        db.commit()
        db.close()

    def dodawanie_osob(self, imie, naziwsko, pas, belki):
        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()
        row = "INSERT INTO osoby_trenujace(imie, nazwisko, pas, belki) VALUES(%s,%s,%s,%s)"
        rowval = (imie, naziwsko, pas, belki)
        cursor_object.execute(row, rowval)

        row = f"SELECT id FROM osoby_trenujace WHERE imie = '{imie}' AND nazwisko = '{naziwsko}';"
        cursor_object.execute(row)
        id_osoby = cursor_object.fetchall()[0][0]
        row = "INSERT INTO karnety(id, aktywny_karnet, miesiac, typ_karnetu, dostepne_treningi_ogolnie, " \
              "pozostale_treningi_w_miesiacu) VALUES(%s,%s,%s,%s,%s,%s);"
        rowval = (id_osoby, False, 0, 0, 0, 0)

        try:
            cursor_object.execute(row, rowval)
        except mysql.connector.errors.IntegrityError:
            print(f"{colored('*Error: Taka osoba istnieje już w bazie danych*', 'red')}")
            user_sleep()
            db.close()
            return False

        db.commit()
        db.close()
        return True

    def dodawanie_osob_parametry(self):
        print("__Dodawanie nowej osoby__")
        imie = input("Podaj imię osoby trenującej:\n")
        nazwisko = input("Podaj nazwisko osoby trenującej:\n")

        while True:
            pas = input("Podaj kolor pasa (Czarny/Brązowy/Purpurowy/Niebieski/Biały):\n").capitalize()

            pasy = ["Czarny", "Brązowy", "Purpurowy", "Niebieski", "Biały"]

            if pas not in pasy:
                print(f"\n{colored('Nie ma takiego pasa', 'red')}\n")

            else:
                break

        while True:
            try:
                belki = int(input("Podaj ilość belek (0-4):\n"))
                if 0 <= belki <= 4:
                    break
                else:
                    print(f"\n{colored('Niewłaściwa ilość belek', 'red')}\n")
            except ValueError:
                print(f"\n{colored('Nieprawidłowe dane', 'red')}\n")

        clear_screen()
        print(f"\nWprowadzone dane:\n"
              f"{imie}, {nazwisko}, pas: {pas}, ilość belek na pasie: {belki}")

        choice = int(input(f"\n1. Zatwierdzić \n2. Poprawić\n0. Menu\n"))

        if choice == 1:
            return self.dodawanie_osob(imie, nazwisko, pas, belki)
        elif choice == 0:
            return False
        else:
            clear_screen()
            return self.dodawanie_osob_parametry()

    def osoby_update(self, parametr, docelowa_wart, id_osoby):
        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()
        row = f"UPDATE klub_zt.osoby_trenujace SET {parametr} = '{docelowa_wart}' WHERE (id = {id_osoby});"
        cursor_object.execute(row)
        db.commit()
        db.close()

    def osoby_update_parametry(self):
        while True:
            try:
                id_osoby = int(input("Podaj id osoby której dane mają zostać zmienione:\n"))
                if type(self.dane_osobowe_imie(id_osoby)) == str:
                    break
                else:
                    print(f"\n{colored('Brak takiej osoby w bazie danych', 'red')}\n")

                    try:
                        choice = int(input(f"\n1. Podaj nowe id"
                                           f"\n0. Powrót\n"))
                    except ValueError:
                        choice = 1

                    if choice == 1:
                        pass
                    else:
                        id_osoby = False
                        break

            except ValueError:
                print(f"{colored('*Error: Niewłaściwe dane*', 'red')}\n")
                pass

        if not id_osoby:
            return False

        while True:
            try:
                parametr = int(input("\nWybierz co ma zostać zmienione: "
                                     "\n1.imie "
                                     "\n2.nazwisko"
                                     "\n3.pas "
                                     "\n4.belki\n"))
                if 1 <= parametr <= 4:
                    break
                else:
                    pass

            except ValueError:
                pass

        parametr_list = ["imie", "nazwisko", "pas", "belki"]
        parametr = parametr_list[parametr - 1]

        docelowa_wart = input("\nPodaj poprawne dane: \n")

        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()
        dane = f"SELECT {parametr} FROM osoby_trenujace WHERE (id = {id_osoby});"
        cursor_object.execute(dane)
        wynik = cursor_object.fetchall()
        db.commit()
        db.close()

        clear_screen()
        print(f"\n___Proponowane zmiany___"
              f"\nCo zmieniamy: {parametr}"
              f"\nStare dane: {wynik[0][0]}"
              f"\nNowe dane: {docelowa_wart}"
              f"\nid osoby której dane zostaną zmieione: {id_osoby}")

        choice = int(input(f"\n1. Zatwierdzić \n2. Poprawić\n0. Menu (Porzucić zmiany)\n"))
        if choice == 1:
            self.osoby_update(parametr, docelowa_wart, id_osoby)
            return True
        elif choice == 0:
            return False
        else:
            clear_screen()
            return self.osoby_update_parametry()

    def osoby_delete(self, id_osoby):
        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()
        row = f"UPDATE klub_zt.osoby_trenujace SET imie = '', nazwisko = '', pas = '', belki = 0 " \
              f"WHERE (id = '{id_osoby}');"

        cursor_object.execute(row)
        db.commit()
        db.close()

    def osoby_delete_parametry(self):
        while True:
            try:
                id_osoby = int(input("Podaj id osoby której dane mają zostać usunięte:\n"))
                if type(self.dane_osobowe_imie(id_osoby)) == str:
                    break
                else:
                    print(f"\n{colored('Brak takiej osoby w bazie danych', 'red')}\n")

                    try:
                        choice = int(input(f"\n1. Podaj nowe id"
                                           f"\n0. Powrót\n"))
                    except ValueError:
                        choice = 1

                    if choice == 1:
                        pass
                    else:
                        id_osoby = False
                        break

            except ValueError:
                print(f"{colored('*Error: Niewłaściwe dane*', 'red')}\n")
                pass

        if not id_osoby:
            return False

        clear_screen()
        print(f"Dane osoby o id={id_osoby} zostaną usunięte z bazy")

        while True:
            try:
                choice = int(input(f"\n1. Zatwierdzić \n2. Poprawić\n0. Menu (porzuć zmiany)\n"))
                if choice in [1, 2, 0]:
                    break
                else:
                    pass
            except ValueError:
                pass

        if choice == 1:
            self.osoby_delete(id_osoby)
            return True
        elif choice == 0:
            return False
        else:
            return self.osoby_delete_parametry()

    def reset_bazy_danych(self):
        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()
        row = f"DROP DATABASE IF EXISTS klub_zt;"

        cursor_object.execute(row)
        db.commit()
        db.close()

        self.inicjowanie_bazy_danych()
        self.inicjowanie_tabel()

    def show_all_people(self):

        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()
        dane = "SELECT * FROM osoby_trenujace;"
        cursor_object.execute(dane)
        wyniki = cursor_object.fetchall()
        print("id   imie   nazwisko   pas   belki\n")
        for i in wyniki:
            if i[1] == '':
                print(f"{i[0]}.")
            else:
                print(f"{i[0]}. {i[1]}, {i[2]}, {i[3]}, {i[4]}")

        db.commit()
        db.close()

    def show_all_people_sorted_by_alf_imie(self):

        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()
        dane = "SELECT DISTINCT id, imie, nazwisko, pas, belki FROM osoby_trenujace ORDER BY imie;"
        cursor_object.execute(dane)
        wyniki = cursor_object.fetchall()
        print("id   imie   nazwisko   pas   belki\n")
        for i in wyniki:
            if i[1] == '':
                print(f"{i[0]}.")
            else:
                print(f"{i[0]}. {i[1]}, {i[2]}, {i[3]}, {i[4]}")

        db.commit()
        db.close()

    def show_all_people_sorted_by_alf_nazwisko(self):

        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()
        dane = "SELECT DISTINCT id, imie, nazwisko, pas, belki FROM osoby_trenujace ORDER BY nazwisko;"
        cursor_object.execute(dane)
        wyniki = cursor_object.fetchall()
        print("id   imie   nazwisko   pas   belki\n")
        for i in wyniki:
            if i[1] == '':
                print(f"{i[0]}.")
            else:
                print(f"{i[0]}. {i[1]}, {i[2]}, {i[3]}, {i[4]}")

        db.commit()
        db.close()

    def print_to_txt(self):

        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()
        dane = "SELECT * FROM osoby_trenujace;"
        cursor_object.execute(dane)
        wyniki = cursor_object.fetchall()
        db.commit()
        db.close()

        year = czas("year")
        month = month_converter(czas("month"))
        day = czas("day")
        hour = czas("hour")
        minutes = czas("min")

        script_path = pathlib.Path(__file__).parent.resolve()
        path = os.path.join(script_path, "Wydruki")

        try:
            os.mkdir(path)
        except FileExistsError:
            pass

        file = open("Wydruki/Lista_osób_trenujących.txt", "w", encoding="UTF-8")
        file.write(f"Data wydruku: {day} {month} {year}, "
                   f"czas: {hour}:{minutes}  \n\n"
                   f"\nid   imie   nazwisko   pas   belki\n\n")

        for i in wyniki:
            if i[1] == '':
                file.write(f"{i[0]}.\n")
            else:
                file.write(f"{i[0]}. {i[1]}, {i[2]}, {i[3]}, {i[4]}\n")

        file.close()

        os.system(rf"{path}/Lista_osób_trenujących.txt")

    def ticket_sell(self, id_osoby, active, month, typ, amount, plec):
        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()
        zapytanie = f"UPDATE klub_zt.karnety SET aktywny_karnet = {active}, miesiac = '{month}', " \
                    f"typ_karnetu = '{typ}', dostepne_treningi_ogolnie = '{amount}'," \
                    f" pozostale_treningi_w_miesiacu = '{amount}', plec = '{plec}' WHERE (id = {id_osoby});"
        cursor_object.execute(zapytanie)
        db.commit()
        db.close()

    def ticket_sell_parametry(self):
        clear_screen()
        while True:
            try:
                id_osoby = int(input("\nPodaj id osoby kupującej karnet:\n"))
                if type(self.dane_osobowe_imie(id_osoby)) == str:
                    break
                else:
                    print(f"\n{colored('Brak takiej osoby w bazie danych', 'red')}\n")

                    try:
                        choice = int(input(f"\n1. Podaj nowe id"
                                           f"\n0. Powrót\n"))
                    except ValueError:
                        choice = 1

                    if choice == 1:
                        pass
                    else:
                        id_osoby = False
                        break

            except ValueError:
                print(f"{colored('*Error: Niewłaściwe dane*', 'red')}\n")
                pass

        if not id_osoby:
            return False

        month = month_converter(datetime.date.today().month)
        karnety_men = {"1 Wejście": [1, "30zł"],
                       "4 Wejścia": [4, "100zł"],
                       "8 Wejść": [8, "140zł"],
                       "15 Wejść": [15, "160zł"],
                       "Dzieci 4-7 lat": [999, "120zł"],
                       "Dzieci 8-15 lat": [999, "130zł"],
                       "Open": [999, "220zł"]}

        karnety_women = {"1 Wejście": [1, "30zł"],
                         "4 Wejścia": [4, "100zł"],
                         "8 Wejść": [8, "120zł"],
                         "15 Wejść": [15, "140zł"],
                         "Dzieci 4-7 lat": [999, "120zł"],
                         "Dzieci 8-15 lat": [999, "130zł"],
                         "Open": [999, "200zł"]}

        clear_screen()
        sex = input("\nK - Kobieta / M - Mężczyzna\n").upper()
        clear_screen()
        print("\n\n___Dostępne karnety___\n")
        if sex == "K" or sex == "KOBIETA":
            sex = "Kobieta"
            for i, j in karnety_women.items():
                print(f"{i} - {j[1]}")

        elif sex == "M" or sex == "MĘŻCZYZNA":
            sex = "Mężczyzna"
            for i, j in karnety_men.items():
                print(f"{i} - {j[1]}")

        while True:
            try:
                typ = input("\nPodaj dokładny typ karnetu do zakupu:\n").capitalize()

                if typ == "1":
                    typ = "1 Wejście"
                elif typ == "4":
                    typ = "4 Wejścia"
                elif typ == "8":
                    typ = "8 Wejść"
                elif typ == "15":
                    typ = "15 Wejść"
                elif typ == "Dzieci 4-7":
                    typ = "Dziecie 4-7 lat"
                elif typ == "Dzieci 8-15":
                    typ = "Dzieci 8-15 lat"

                amount = karnety_men.get(typ)[0]
                break
            except TypeError:
                print(f"\n{colored('*Error: Niewłaściwe dane*', 'red')}\n")

        clear_screen()
        print(f"\n___Wprowadzone dane___\n"
              f"\nid osoby kupującej karnet: {id_osoby}"
              f"\nPłeć: {sex}"
              f"\nTyp karnetu: {typ}"
              f"\nMiesiąc: {month}"
              f"\n")

        while True:
            try:
                choice = int(input("\n1. Zatwierdź"
                                   "\n2. Popraw"
                                   "\n"
                                   "\n0. Menu (porzuć zmiany)\n"))
                if choice in [1, 2, 0]:
                    break
                else:
                    pass
            except ValueError:
                pass

        if choice == 1:
            self.ticket_sell(id_osoby, True, month, typ, amount, sex)
            return True
        elif choice == 0:
            return False
        else:
            return self.ticket_sell_parametry()

    def auto_ticket_month_check(self):
        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()

        zapytanie = f"SELECT id FROM karnety WHERE aktywny_karnet = 1;"
        cursor_object.execute(zapytanie)
        wyniki = cursor_object.fetchall()
        db.commit()
        db.close()

        lista_aktywnych_id = []
        for i in wyniki:
            lista_aktywnych_id.append(i[0])

        current_month = month_converter(datetime.date.today().month)

        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()

        zapytanie = f"SELECT miesiac FROM karnety WHERE aktywny_karnet = 1 LIMIT 1;"
        cursor_object.execute(zapytanie)
        wyniki = cursor_object.fetchall()
        db.commit()
        db.close()

        try:
            month_data = wyniki[0][0]
        except IndexError:
            month_data = None

        if month_data == current_month:
            pass
        else:
            for i in lista_aktywnych_id:
                db = mysql.connector.connect(user="root", password="Torex123kt", host='127.0.0.1', port=3306,
                                             database="klub_zt")
                cursor_object = db.cursor()
                zapytanie = f"UPDATE klub_zt.karnety SET aktywny_karnet = {False}, miesiac = '{current_month}' " \
                            f"WHERE (id = {i});"

                cursor_object.execute(zapytanie)
                db.commit()
                db.close()

    def key_giveaway(self, id_osoby):
        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()
        zapytanie = f"SELECT aktywny_karnet, dostepne_treningi_ogolnie, pozostale_treningi_w_miesiacu " \
                    f"FROM karnety WHERE id = {id_osoby};"
        cursor_object.execute(zapytanie)
        wynik = cursor_object.fetchall()
        db.commit()
        db.close()

        active = bool(wynik[0][0])
        amount_left = wynik[0][2] - 1
        if amount_left == -1:
            active = False

        if active:
            db = mysql.connector.connect(user="root", password='Torex123kt', host='127.0.0.1', port=3306,
                                         database="klub_zt")
            cursor_object = db.cursor()
            zapytanie = f"UPDATE klub_zt.karnety SET pozostale_treningi_w_miesiacu = {amount_left} " \
                        f"WHERE id = {id_osoby};"
            cursor_object.execute(zapytanie)
            db.commit()
            db.close()

            self.statystyki_klubowe_wejscia()

            print(colored("\nMożna wydać kluczyk\n", "green"))
            user_sleep()
            return True

        else:
            print(colored("\nBrak aktywnego karnetu\n", "red"))
            user_sleep()
            return False

    def key_giveaway_parametry(self):
        while True:
            try:
                id_osoby = int(input("\nPodaj id osoby trenującej:\n"))
                if type(self.dane_osobowe_imie(id_osoby)) == str:
                    break
                else:
                    print(f"\n{colored('Brak takiej osoby w bazie danych', 'red')}\n")

                    try:
                        choice = int(input(f"\n1. Podaj nowe id"
                                           f"\n0. Powrót\n"))
                    except ValueError:
                        choice = 1

                    if choice == 1:
                        pass
                    else:
                        id_osoby = False
                        break

            except ValueError:
                print(f"{colored('*Error: Niewłaściwe dane*', 'red')}\n")
                pass

        if not id_osoby:
            return False

        return self.key_giveaway(id_osoby)

    def ticket_check(self, id_osoby):
        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()
        zapytanie = f"SELECT aktywny_karnet, pozostale_treningi_w_miesiacu " \
                    f"FROM karnety WHERE id = {id_osoby};"
        cursor_object.execute(zapytanie)
        wynik = cursor_object.fetchall()
        db.commit()
        db.close()

        activ = bool(wynik[0][0])
        amount_left = wynik[0][1]

        if activ and 0 < amount_left < 900:
            print(f"{colored('Karnet jest aktywny', 'green')}"
                  f"\nPozostała ilość wejść do wykorzystania: {amount_left}")

        elif activ and amount_left > 900:
            print(f"{colored('Karnet jest aktywny', 'green')}"
                  f"\nPozostała ilość wejść do wykorzystania: {colored('Nielimitowany dostęp', 'green')}\n")

        else:
            print(f"{colored('Karnet został wykorzystany', 'red')}")

    def ticket_check_parametry(self):
        while True:
            try:
                id_osoby = int(input("\nPodaj id osoby trenującej\n"))
                if type(self.dane_osobowe_imie(id_osoby)) == str:
                    break
                else:
                    print(f"\n{colored('Brak takiej osoby w bazie danych', 'red')}\n")

                    try:
                        choice = int(input(f"\n1. Podaj nowe id"
                                           f"\n0. Powrót\n"))
                    except ValueError:
                        choice = 1

                    if choice == 1:
                        pass
                    else:
                        id_osoby = False
                        break

            except ValueError:
                print(f"{colored('*Error: Niewłaściwe dane*', 'red')}\n")
                pass

        if not id_osoby:
            return False

        if type(self.dane_osobowe_imie(id_osoby)) == str and type(self.dane_osobowe_naziwsko(id_osoby)):
            print(f"Właściciel karnetu: {colored(self.dane_osobowe_imie(id_osoby),'blue')} "
                  f"{colored(self.dane_osobowe_naziwsko(id_osoby),'blue')}\n")

            return self.ticket_check(id_osoby)

        else:
            print(f"{colored('Brak osoby o takim id w bazie danych','red')}")

    def dane_osobowe_imie(self, id_osoby):
        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()
        zapytanie = f"SELECT imie FROM osoby_trenujace WHERE id = {id_osoby} LIMIT 1"
        cursor_object.execute(zapytanie)
        dane_osobowe = cursor_object.fetchall()
        db.commit()
        db.close()

        try:
            imie = dane_osobowe[0][0]
        except IndexError:
            imie = False

        return imie

    def dane_osobowe_naziwsko(self, id_osoby):
        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()
        zapytanie = f"SELECT nazwisko FROM osoby_trenujace WHERE id = {id_osoby} LIMIT 1"
        cursor_object.execute(zapytanie)
        dane_osobowe = cursor_object.fetchall()
        db.commit()
        db.close()

        try:
            nazwisko = dane_osobowe[0][0]
        except IndexError:
            nazwisko = False

        return nazwisko

    def id_finder(self, imie, nazwisko):
        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()
        zapytanie = f"SELECT id FROM osoby_trenujace WHERE imie = '{imie}' AND nazwisko = '{nazwisko}'"
        cursor_object.execute(zapytanie)
        wynik = cursor_object.fetchall()
        db.commit()
        db.close()

        try:
            id_osoby = wynik[0][0]
        except IndexError:
            id_osoby = False

        return id_osoby

    def id_finder_parametry(self):
        clear_screen()
        print("\nPodaj dane osoby trenującej")
        imie = input("\nImię: ")
        nazwisko = input("Nazwisko: ")
        id_osoby = self.id_finder(imie, nazwisko)

        if id_osoby:
            print(f"\nid szukanej osoby: {colored(self.id_finder(imie, nazwisko), 'blue')}")
        else:
            print(f"\n{colored('Brak takiej osoby w bazie danych', 'red')}")

    def statystyki_klubowe_wejscia(self):
        db = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', port=3306,
                                     database="klub_zt")
        cursor_object = db.cursor()

        month = month_converter(czas("month"))
        year = czas("year")
        zapytanie = f"SELECT id, ilosc_wejsc, miesiac, rok FROM statystyki_klubowe " \
                    f"WHERE miesiac = '{month}' AND rok = {year}"

        cursor_object.execute(zapytanie)
        wyniki = cursor_object.fetchall()

        if not wyniki:
            zapytanie = f"INSERT INTO statystyki_klubowe(ilosc_wejsc, miesiac, rok) VALUES(%s, %s, %s) "
            wartosci = (1, month, year)
            cursor_object.execute(zapytanie, wartosci)

        else:
            id_wpisu = wyniki[0][0]
            ilosc_wejsc = wyniki[0][1] + 1
            zapytanie = f"UPDATE klub_zt.statystyki_klubowe SET ilosc_wejsc = {ilosc_wejsc} WHERE (id = {id_wpisu});"
            cursor_object.execute(zapytanie)

        db.commit()
        db.close()
