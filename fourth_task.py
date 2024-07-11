# Розбиваємо введений рядок на команду та аргументи,
# приводимо команду до нижнього регістру і видаляємо зайві пробіли,
# повертаємо команду і список аргументів
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Error: contact not found."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


# Створюємо функцію "add_contact" де перевіряємо,чи передано аргументи,чи існує контак,
# розпаковуємо аргументи та додаємо новий контакт у словник якщо контакта не існує
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


# Створюємо функцію "change_contact" де перевіряємо,
# чи передано аргументи, розпаковуємо аргументи
# та якщо контакт існує оновлюємо номер телефону
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error: contact not found."


# Створюємо функцію "show_phone" що перевіряє, чи передано аргумент,
# отримуємо ім'я з аргументів,якщо контакт існує повертаємо номер телефону
@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]



# Створюємо функцію "show_all" яка створюємо рядок для збереження результату,
# перевіряє, чи є контакти в словнику, проходить через всі контакти і додає їх в result
@input_error
def show_all(contacts):
    # Створюємо рядок для збереження результату
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
        # Парсить введення користувача на команду та аргументи
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
    # Запускаємо головну функцію
    main()
