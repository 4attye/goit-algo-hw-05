"""
    Функція що парсить введений рядок на команду та аргументи,
    приводить команду до нижнього регістру і видаляє зайві пробіли,
    повертає команду і список аргументів
"""
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

"""
    Декоратор для обробки помилок, якщо виникає помилка
    ValueError, повертається повідомлення "Введіть ім'я та телефон",
    KeyError, повертається повідомлення "Контакт не знайдено",
    IndexError, повертається повідомлення "Введіть ім'я".
"""
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."

    return inner

"""
    Функцію "add_contact" що перевіряє,чи передано аргументи,чи існує контак,
    розпаковує аргументи та додає новий контакт у словник якщо контакта не існує
"""
@input_error
def add_contact(args, contacts):
    name, phone = args
    if not name in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        raise "The contact already exists"

"""
    Функцію "change_contact" що перевіряємо, чи передано аргументи,
    розпаковує аргументи та якщо контакт існує оновлює номер телефону
"""
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

"""
    Функцію "show_phone" що перевіряє, чи передано аргумент,
    отримує ім'я з аргументів,якщо контакт існує повертає номер телефону
"""
@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

"""
    Функцію "show_all" що створює рядок для збереження результату,
    перевіряє, чи є контакти в словнику, проходить через всі контакти і додає їх в result
"""
@input_error
def show_all(contacts):
    if not contacts:
        raise KeyError
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
        return result.strip()


def main():
    # Створюємо порожній словник для контактів
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        # Отримує данні від користувача
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        # Якщо ввели команду "close" або "exit", програма завершує роботу
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        # Якщо ввели команду "hallo", виводяться привітання
        elif command == "hello":
            print("How can I help you?")
        # Якщо ввели команду "add", додається контакт
        elif command == "add":
            print(add_contact(args, contacts))
        # Якщо ввели команду "change", змінюєтьса існуючий номер
        elif command == "change":
            print(change_contact(args, contacts))
        # Якщо ввели команду "phone", виводяться номер телефону
        elif command == "phone":
            print(show_phone(args, contacts))
        # Якщо ввели команду "all", виводяться всі контакти
        elif command == "all":
            print(show_all(contacts))
        # Якщо команда не розпізнана, виводить повідомлення про помилку
        else:
            print("Invalid command.")




if __name__ == "__main__":
    main()
