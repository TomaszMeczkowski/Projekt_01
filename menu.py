from baza import BazaDanych
from funkcje import clear_screen
import time


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
            if self.ticket_giveaway_parametry():
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
            user_wait = input("\nWprowadź dowolny znak żeby cofnąć:\n")
            self.menu_obsluga_klienta()

        elif choice == 4:
            self.id_finder_parametry()
            user_wait = input("\nWprowadź dowolny znak żeby cofnąć:\n")
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
              "\n"
              "\n9. Odśwież"
              "\n0. Menu Główne")

        try:
            choice = int(input())
        except ValueError:
            choice = 404

        clear_screen()
        if choice == 1:
            print("Ładowanie osób prefediniowanych do bazy danych...")
            osoby = [
                ["Tomek", "Męczkowski", "Purpurowy", 2],
                ["Olga", "Zabulewicz", "Purpurowy", 2],
                ["Andrzej", "Iwat", "Czarny", 0],
                ["Alicja", "Kardas", "Niebieski", 3],
                ["Ola", "Warczak", "Purpurowy", 3],
                ["Martyna", "Iwat", "Czarny", 0],
                ["Jacek", "Sasin", "Niebieski", 2],
                ["Iza", "Wołos", "Niebieski", 0],
                ["Oskar", "Śleszyński", "Niebieski", 0],
                ["Patrycja", "Pecura", "Biały", 0],
                ["Agata", "Stach", "Brązowy", 0],
                ["Wojtek", "Wastowstki", "Niebieski", 3],
                ["Sandra", "Słowińska", "Purpurowy", 2]
                ]

            # Jeżeli chcemy wiecej powtórzeń danych trzeba zmienić range(i) na większe i
            for large_data in range(1):
                for i in range(0, len(osoby)):
                    self.dodawanie_osob(osoby[i][0], osoby[i][1], osoby[i][2], osoby[i][3])

            # Aktywowanie karnetów dla załadowanych osoób pierwszych osób
            for i in range(len(osoby) + 1):
                self.ticket_sell(i, True, "Lipiec", "Open", 999, "M/K")

            time.sleep(3)
            self.menu_glowne(mess="*Pomyślnie dodano zestaw osoób*")

        elif choice == 2:
            self.reset_bazy_danych()

            for i in range(1, 4):
                print("Restowanie bazy danych" + str(i * "."))
                time.sleep(0.5)
                clear_screen()

            self.menu_glowne(mess="*Pomyślnie zresetowano baze danych*")

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
            user_wait = input("\nWprowadź dowolny znak żeby cofnąć:\n")
            self.menu_lista_osob()

        elif choice == 2:
            self.show_all_people_sorted_by_alf_imie()
            user_wait = input("\nWprowadź dowolny znak żeby cofnąć:\n")
            self.menu_lista_osob()

        elif choice == 3:
            self.show_all_people_sorted_by_alf_nazwisko()
            user_wait = input("\nWprowadź dowolny znak żeby cofnąć:\n")
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
