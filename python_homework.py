# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
import csv

def load_contacts_from_csv(filename):
    contacts = []
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 4:  # Проверяем, есть ли в строке хотя бы 4 столбца
                contact = {'Фамилия': row[0], 'Имя': row[1], 'Отчество': row[2], 'Телефон': row[3]}
                contacts.append(contact)
    return contacts

def save_contacts_to_csv(contacts, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for contact in contacts:
            writer.writerow([contact['Фамилия'], contact['Имя'], contact['Отчество'], contact['Телефон']])
    print("Контакты успешно сохранены в файл:", filename)

def display_contacts(contacts):
    print("{:<5} {:<15} {:<15} {:<15} {:<15}".format('№', 'Фамилия', 'Имя', 'Отчество', 'Телефон'))
    for i, contact in enumerate(contacts, 1):
        print("{:<5} {:<15} {:<15} {:<15} {:<15}".format(i, contact['Фамилия'], contact['Имя'], contact['Отчество'], contact['Телефон']))

def add_contact(contacts):
    Фамилия = input("Введите фамилию: ")
    Имя = input("Введите имя: ")
    Отчество = input("Введите отчество: ")
    Телефон = input("Введите номер телефона: ")
    новый_контакт = {'Фамилия': Фамилия, 'Имя': Имя, 'Отчество': Отчество, 'Телефон': Телефон}
    if новый_контакт not in contacts:
        contacts.append(новый_контакт)
        print("Контакт успешно добавлен.")
    else:
        print("Такой контакт уже существует.")

def update_contact(contacts):
    Фамилия = input("Введите фамилию контакта, который нужно изменить: ")
    Имя = input("Введите имя контакта, который нужно изменить: ")
    for contact in contacts:
        if contact['Фамилия'] == Фамилия and contact['Имя'] == Имя:
            contact['Фамилия'] = input("Введите новую фамилию: ")
            contact['Имя'] = input("Введите новое имя: ")
            contact['Отчество'] = input("Введите новое отчество: ")
            contact['Телефон'] = input("Введите новый номер телефона: ")
            print("Контакт успешно обновлен.")
            return
    print("Контакт не найден.")

def delete_contact(contacts):
    Фамилия = input("Введите фамилию контакта, который нужно удалить: ")
    Имя = input("Введите имя контакта, который нужно удалить: ")
    удален = False
    for contact in contacts[:]:
        if contact['Фамилия'] == Фамилия and contact['Имя'] == Имя:
            contacts.remove(contact)
            удален = True
    if удален:
        print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")

def search_contacts(contacts):
    характеристика = input("Введите характеристику для поиска (Фамилия, Имя, Отчество или Телефон): ").capitalize()
    значение = input(f"Введите {характеристика}: ")
    found = False
    for i, contact in enumerate(contacts, 1):
        if значение in contact[характеристика]:
            print("{:<5} {:<15} {:<15} {:<15} {:<15}".format(i, contact['Фамилия'], contact['Имя'], contact['Отчество'], contact['Телефон']))
            found = True
    if not found:
        print("Контакт не найден.")

def copy_contact_to_file(contacts):
    contact_numbers = input("Введите номера контактов для копирования (через запятую): ")
    contact_numbers = [int(num.strip()) for num in contact_numbers.split(",") if num.strip().isdigit()]
    if not contact_numbers:
        print("Некорректный ввод. Введите номера контактов через запятую.")
        return
    target_file = input("Введите имя файла для копирования контактов: ")
    selected_contacts = [contacts[num - 1] for num in contact_numbers if 0 < num <= len(contacts)]
    existing_contacts = load_contacts_from_csv(target_file)
    existing_contacts.extend(selected_contacts)
    save_contacts_to_csv(existing_contacts, target_file)
    print("Контакты успешно скопированы в файл:", target_file)

def copy_contact_from_file(contacts):
    source_file = input("Введите имя файла, из которого нужно скопировать контакты: ")
    new_contacts = load_contacts_from_csv(source_file)
    print("Контакты в файле для копирования:")
    display_contacts(new_contacts)
    contact_numbers = input("Введите номера контактов для копирования (через запятую): ")
    contact_numbers = [int(num.strip()) for num in contact_numbers.split(",") if num.strip().isdigit()]
    selected_contacts = [new_contacts[num - 1] for num in contact_numbers if 0 < num <= len(new_contacts)]
    contacts.extend(selected_contacts)
    print("Контакты успешно скопированы.")

def save_and_exit(contacts, filename):
    save_contacts_to_csv(contacts, filename)
    print("Данные сохранены в файл. Программа завершена.")
    exit()

def main():
    contacts = load_contacts_from_csv("contacts.csv")

    while True:
        print("\nМеню:")
        print("1. Просмотреть все контакты")
        print("2. Добавить новый контакт")
        print("3. Изменить контакт")
        print("4. Удалить контакт")
        print("5. Найти контакт")
        print("6. Копировать контакт в другой файл")
        print("7. Копировать контакт из другого файла")
        print("8. Сохранить и выйти")
        print("9. Выйти без сохранения")

        choice = input("Выберите действие: ")

        if choice == "1":
            display_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            search_contacts(contacts)
        elif choice == "6":
            copy_contact_to_file(contacts)
        elif choice == "7":
            copy_contact_from_file(contacts)
        elif choice == "8":
            save_and_exit(contacts, "contacts.csv")
            break
        elif choice == "9":
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из меню.")

if __name__ == "__main__":
    main()

