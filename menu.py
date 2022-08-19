from baza import BazaDanych
from funkcje import clear_screen, user_sleep
from time import sleep


class Menu(BazaDanych):

    def __init__(self, user, password):
        super().__init__(user, password)
        self.inicjowanie_bazy_danych()
        self.inicjowanie_tabel()
        self.auto_ticket_month_check()

    def menu_glowne(self, mess=""):
        clear_screen()
        print(f"\n______Aplikacja Organizacyjna______"
              f"\n{mess}")

        print("\n_______Menu Główne_______\n"
              "\n1. Obsługa klienta"
              "\n2. Baza danych"
              "\n3. Statystyki"
              "\n"
              "\n9. Odśwież"
              "\n666. Development tools"
              "\n0. Wyjście z programu")

        try:
            choice = int(input())
        except ValueError:
            choice = 404

        if choice == 1:
            self.menu_obsluga_klienta()
            self.menu_glowne()

        elif choice == 2:
            self.menu_baza_danych()
            self.menu_glowne()

        elif choice == 3:
            self.menu_statystyki()
            self.menu_glowne()

        elif choice == 9:
            self.menu_glowne()

        elif choice == 666:
            self.menu_dev_tools()
            self.menu_glowne()

        elif choice == 0:
            clear_screen()
            print("Koniec programu")
            exit()

        else:
            self.menu_glowne()

    def menu_obsluga_klienta(self, mess=""):
        clear_screen()
        print(f"\n______Aplikacja Organizacyjna______"
              f"\n{mess}")

        print("\n_____Obsługa Klienta_____\n"
              "\n1. Wydaj kluczyk"
              "\n2. Sprzedaj karnet"
              "\n3. Sprawdź karnet"
              "\n4. id finder"
              "\n"
              "\n9. Odśwież"
              "\n0. Menu Główne")

        try:
            choice = int(input())
        except ValueError:
            choice = 404

        clear_screen()
        if choice == 1:
            if self.key_giveaway_parametry():
                self.menu_obsluga_klienta(mess="*Pomyślnie wydano kluczyk*")
            else:
                self.menu_obsluga_klienta()

        elif choice == 2:
            if self.ticket_sell_parametry():
                self.menu_obsluga_klienta(mess="*Pomyślnie sprzedano karnet*")
            else:
                self.menu_obsluga_klienta()

        elif choice == 3:
            self.ticket_check_parametry()
            user_sleep()
            self.menu_obsluga_klienta()

        elif choice == 4:
            self.id_finder_parametry()
            user_sleep()
            self.menu_obsluga_klienta()

        elif choice == 9:
            self.menu_obsluga_klienta()

        elif choice == 0:
            pass

        else:
            self.menu_obsluga_klienta()

    def menu_baza_danych(self, mess=""):
        clear_screen()
        print(f"\n______Aplikacja Organizacyjna______"
              f"\n{mess}")

        print("\n____Baza Danych____\n"
              "\n1. Dodaj nową osobe"
              "\n2. Popraw dane osoby"
              "\n3. Wyświetl wszystkie osoby"
              "\n4. Usuń dane osoby"
              "\n"
              "\n9. Odśwież"
              "\n0. Menu Główne")

        try:
            choice = int(input())
        except ValueError:
            choice = 404

        clear_screen()
        if choice == 1:
            if self.dodawanie_osob_parametry():
                self.menu_baza_danych(mess="*Pomyślnie dodano osobe*")
            else:
                self.menu_baza_danych()

        elif choice == 2:
            if self.osoby_update_parametry():
                self.menu_baza_danych(mess="*Pomyślnie zmieniono dane*")
            else:
                self.menu_baza_danych()

        elif choice == 3:
            self.menu_lista_osob()
            self.menu_baza_danych()

        elif choice == 4:
            if self.osoby_delete_parametry():
                self.menu_baza_danych(mess="*Pomyślnie usunięto osobę z bazy danych* \n*(id zostało zwolnione)*")
            else:
                self.menu_baza_danych()

        elif choice == 9:
            self.menu_baza_danych()

        elif choice == 0:
            pass

        else:
            self.menu_baza_danych()

    def menu_dev_tools(self, mess=""):
        clear_screen()
        print(f"\n______Aplikacja Organizacyjna______"
              f"\n{mess}")

        print("\n__________Dev Tools__________\n"
              "\n1. Załaduj predefiniowane dane"
              "\n2. Reset Bazy Danych"
              "\n3. Dane statystyczne wejść dla id = 1"
              "\n"
              "\n9. Odśwież"
              "\n0. Menu Główne")

        try:
            choice = int(input())
        except ValueError:
            choice = 404

        clear_screen()
        if choice == 1:
            self.dev_tool_osoby()
            self.menu_glowne(mess="*Pomyślnie dodano zestaw osób*")

        elif choice == 2:
            self.reset_bazy_danych()

            for i in range(1, 4):
                print("Restowanie bazy danych" + str(i * "."))
                sleep(0.8)
                clear_screen()

            self.menu_glowne(mess="*Pomyślnie zresetowano baze danych*")

        elif choice == 3:
            self.dev_tool_statistics_01()
            self.menu_glowne(mess="*Pomyślnie dodano dane*")

        elif choice == 9:
            self.menu_dev_tools()

        elif choice == 0:
            pass

        else:
            self.menu_dev_tools()

    def menu_lista_osob(self):
        clear_screen()
        print("\n1. Lista osoób według id"
              "\n2. Lista osób według imion"
              "\n3. Lista osób według nazwisk"
              "\n4. Wydruk"
              "\n"
              "\n0. Menu")

        try:
            choice = int(input())
        except ValueError:
            choice = 404

        clear_screen()
        if choice == 1:
            self.show_all_people()
            user_sleep()
            self.menu_lista_osob()

        elif choice == 2:
            self.show_all_people_sorted_by_alf_imie()
            user_sleep()
            self.menu_lista_osob()

        elif choice == 3:
            self.show_all_people_sorted_by_alf_nazwisko()
            user_sleep()
            self.menu_lista_osob()

        elif choice == 4:
            print("\n1. Wydruk w formacie .txt"
                  "\n"
                  "\n0. Powrót")
            try:
                choice = int(input())
            except ValueError:
                choice = 404

            if choice == 1:
                self.print_to_txt()
                clear_screen()
            else:
                pass

            self.menu_lista_osob()

        elif choice == 0:
            pass

        else:
            self.menu_lista_osob()

    def menu_statystyki(self, mess=""):
        clear_screen()
        print(f"\n______Aplikacja Organizacyjna______"
              f"\n{mess}")

        print("\n_____Statystyki_____\n"
              "\n1. Ilość wejść całego klubu"
              "\n2. Ilość wejść osoby trenującej"
              "\n3. Wykresy (osobowe by id)"
              "\n"
              "\n9. Odśwież"
              "\n0. Menu Główne")

        try:
            choice = int(input())
        except ValueError:
            choice = 404

        clear_screen()
        if choice == 1:
            self.stat_entry()
            user_sleep()
            self.menu_statystyki()

        elif choice == 2:
            self.stat_entry_by_id_parametry()
            self.menu_statystyki()

        elif choice == 3:
            if self.plot_osoba_parametry():
                user_sleep()
                self.menu_statystyki("*Pomyślnie zapisano wykres*")

            user_sleep()
            self.menu_statystyki()

        elif choice == 9:
            self.menu_statystyki()

        elif choice == 0:
            pass

        else:
            self.menu_statystyki()
