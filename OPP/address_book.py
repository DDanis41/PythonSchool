from decorators import time_measurement
import pickle

class Card:
    def __init__(self, first_name, last_name, email, phone, organization):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.organization = organization

    def all_info_in_string(self):
        return \
        f'Имя:{self.last_name} {self.first_name} \
        email:{self.email}\
        телефон:{self.phone}\
        организация:{self.organization} '

    def full_name(self):
        return f'{self.last_name} {self.first_name}'


class AddressBook:
    def __init__(self):
        self.index = 1
        self.cards = {}

    def size(self):
        """
        Размер адрессной кники(количество записей)
        :return: int
        """
        return len(self.cards)

    def add_card(self, first_name, last_name, email, phone, organization):
        self.index += 1
        new_card = Card(first_name, last_name, email, phone, organization)
        self.cards[self.index] = new_card

    def delete_card(self, card_index):
        if not (self.cards.pop(card_index, False)):
            print(f'Не существует записи с индексом {card_index}')

    def clear(self):
        self.cards.clear()
        self.index = 1

    def show_all_names(self):
        for key, val in self.cards.items():
            print(f'№{key} {val.full_name()} ')

    def get_info(self, card_index):
        try:
            card = self.cards[card_index]
        except Exception:
            print(f'Не существует записи с индексом {card_index}')
            return ""
        else:
            return card.all_info_in_string()

    @time_measurement
    def show_all(self):
        for key in self.cards.keys():
            print(f'№{key} {self.get_info(key)}')
        return True

    @time_measurement
    def save(self):
        try:
            with open('AddressBook.txt', 'wb') as book_file:
                book_file.seek(0)
                pickle.dump(self.cards,  book_file)
        except:
            raise
        finally:
            book_file.close()

    @time_measurement
    def load(self):
        try:
            with open('AddressBook.txt', 'rb') as book_file:
                self.cards = pickle.load(book_file)
                self.index = max(self.cards.keys())
        except:
            raise
        finally:
            book_file.close()


