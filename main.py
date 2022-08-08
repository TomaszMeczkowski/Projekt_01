from menu import Menu
import mysql.connector
from termcolor import colored

if __name__ == "__main__":
    print("Łączenie się z bazą danych MySQL, podaj dane dostępowe")

    while True:
        user = input("User: ")
        password = input("Password: ")
        try:
            main = Menu(user, password)
            main.menu_glowne()
            break

        except mysql.connector.errors.ProgrammingError:
            print(f"\n{colored('Nieprawidłowe dane dostępowe','red')}\n")
