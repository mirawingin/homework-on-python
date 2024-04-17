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
def load_contacts(filename):
    contacts = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                contacts.append({'Фамилия': data[0], 'Имя': data[1], 'Отчество': data[2], 'Телефон': data[3]})
    except FileNotFoundError:
        print("Файл не найден.")
    return contacts

def save_contacts(contacts, filename):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(','.join(contact.values()) + '\n')

def display_contacts(contacts):
    for contact in contacts:
        print(', '.join(contact.values()))

def find_contacts(contacts, characteristic, value):
    found_contacts = []
    for contact in contacts:
        if contact[characteristic] == value:
            found_contacts.append(contact)
    return found_contacts

def search_contacts(contacts):
    search_characteristic = input("Введите характеристику для поиска (Фамилия, Имя, Отчество или Телефон): ").capitalize()
    search_value = input(f"Введите {search_characteristic.lower()}: ")
    found_contacts = find_contacts(contacts, search_characteristic, search_value)
    if found_contacts:
        print("Найденные контакты:")
        display_contacts(found_contacts)
    else:
        print("Контакты с такой характеристикой не найдены.")

def add_contact(contacts):
    Фамилия = input("Введите фамилию: ")
    Имя = input("Введите имя: ")
    Отчество = input("Введите отчество: ")
    Телефон = input("Введите телефон: ")
    новый_контакт = {'Фамилия': Фамилия, 'Имя': Имя, 'Отчество': Отчество, 'Телефон': Телефон}
    contacts.append(новый_контакт)
    print("Контакт успешно добавлен.")

def edit_contact(contacts):
    фамилия = input("Введите фамилию контакта для редактирования: ")
    found_contacts = find_contacts(contacts, 'Фамилия', фамилия)
    if found_contacts:
        print("Найденные контакты:")
        display_contacts(found_contacts)
        индекс = int(input("Введите номер контакта для редактирования: ")) - 1
        if 0 <= индекс < len(found_contacts):
            контакт = found_contacts[индекс]
            новые_данные = {}
            for key in контакт:
                новое_значение = input(f"Введите новое значение для {key}: ")
                новые_данные[key] = новое_значение
            контакт.update(новые_данные)
            print("Контакт успешно отредактирован.")
        else:
            print("Некорректный номер контакта.")
    else:
        print("Контакт с такой фамилией не найден.")

def main():
    contacts_data = load_contacts('contacts.txt')
    while True:
        print("\nМеню:")
        print("1. Просмотреть все контакты")
        print("2. Поиск контакта")
        print("3. Добавить контакт")
        print("4. Редактировать контакт")
        print("5. Сохранить и выйти")
        choice = input("Выберите действие: ")
        if choice == '1':
            display_contacts(contacts_data)
        elif choice == '2':
            search_contacts(contacts_data)
        elif choice == '3':
            add_contact(contacts_data)
        elif choice == '4':
            edit_contact(contacts_data)
        elif choice == '5':
            save_contacts(contacts_data, 'contacts.txt')
            print("Контакты сохранены. Программа завершена.")
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

main()

contacts_data = [
    {'Фамилия': 'Смирнов', 'Имя': 'Александр', 'Отчество': 'Иванович', 'Телефон': '+79001234567'},
    {'Фамилия': 'Иванов', 'Имя': 'Петр', 'Отчество': 'Сергеевич', 'Телефон': '+79012345678'},
    {'Фамилия': 'Петров', 'Имя': 'Семен', 'Отчество': 'Федорович', 'Телефон': '+79023456789'},
    {'Фамилия': 'Васильев', 'Имя': 'Алексей', 'Отчество': 'Петрович', 'Телефон': '+79034567890'},
    {'Фамилия': 'Сидоров', 'Имя': 'Владимир', 'Отчество': 'Алексеевич', 'Телефон': '+79045678901'},
    {'Фамилия': 'Кузнецов', 'Имя': 'Игорь', 'Отчество': 'Михайлович', 'Телефон': '+79056789012'},
    {'Фамилия': 'Зайцев', 'Имя': 'Дмитрий', 'Отчество': 'Аркадьевич', 'Телефон': '+79067890123'},
    {'Фамилия': 'Павлов', 'Имя': 'Сергей', 'Отчество': 'Степанович', 'Телефон': '+79078901234'},
    {'Фамилия': 'Семенов', 'Имя': 'Илья', 'Отчество': 'Владимирович', 'Телефон': '+79089012345'},
    {'Фамилия': 'Голубев', 'Имя': 'Андрей', 'Отчество': 'Егорович', 'Телефон': '+79090123456'},
    {'Фамилия': 'Федоров', 'Имя': 'Максим', 'Отчество': 'Константинович', 'Телефон': '+79101234567'},
    {'Фамилия': 'Михайлов', 'Имя': 'Николай', 'Отчество': 'Андреевич', 'Телефон': '+79112345678'},
    {'Фамилия': 'Егоров', 'Имя': 'Василий', 'Отчество': 'Павлович', 'Телефон': '+79123456789'},
    {'Фамилия': 'Николаев', 'Имя': 'Артем', 'Отчество': 'Вячеславович', 'Телефон': '+79134567890'},
    {'Фамилия': 'Макаров', 'Имя': 'Игнат', 'Отчество': 'Филиппович', 'Телефон': '+79145678901'},
]

# Пример использования функций
save_contacts(contacts_data, 'contacts.txt')
contacts = load_contacts('contacts.txt')
search_contacts(contacts)
