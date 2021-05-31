from address_book import AddressBook

def main():

    Abook = AddressBook()
    #Abook.add_card("Иван", "Иванов", "ivanov@gmail.com", "8-913-000-00-01", "ООО Рога и КОпыта")
    #Abook.add_card("Петр", "Петров", "petrov@gmail.com", "8-913-000-00-02", "ООО Русские тапочки")
    #Abook.add_card("Висилий", "Сидоров", "sidorov@gmail.com", "8-913-000-00-03", "ООО Тульские пряники")
    #Abook.add_card("Артемий2", "Троицкий", "tro@gmail.com", "8-913-000-00-04", "Газгольдер")

    #Abook.save()

    Abook.load()

    print(f'Количество записей в адрессной книге :{Abook.size()}')
    Abook.show_all_names()

    print('\nДанные по карточке №3')
    print(Abook.get_info(3))

    print('\nУдаление карточки №3')
    Abook.delete_card(3)

    print(f'Количество записей в адрессной книге :{Abook.size()}\n')
    Abook.show_all_names()

    print('\nДанные карточки №3')
    print(Abook.get_info(3))

    #Abook.show_all()


if __name__ == '__main__':
    main()