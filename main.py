# MyProfile app
from typing import Any, Optional

SEPARATOR = '------------------------------------------'


class Entrepreneur:

    def __init__(self):
        # general info
        self.name: str = ''
        self.age: int = 0
        self.years_parameter: str = self.__years_endings()
        self.email: str = ''
        self.phone: str = ''
        self.post_index: str = ''
        self.post_address: str = ''
        self.city = ''
        self.additional_info: str | None = None

        # entrepreneur info
        self.ogrnip: int = 0
        self.__ogrnip_len: int = 15
        self.inn = ''
        self.bank_name = ''
        self.bank_account: int = 0
        self.__bank_account_len: int = 20
        self.bik: int = 0
        self.correspondent_account: int = 0

    def __years_endings(self) -> str:
        if 11 <= self.age % 100 <= 19:
            years_parameter = 'лет'
        elif self.age % 10 == 1:
            years_parameter = 'год'
        elif 2 <= self.age % 10 <= 4:
            years_parameter = 'года'
        else:
            years_parameter = 'лет'
        return years_parameter

    def print_general_info_user(self):
        print(SEPARATOR)
        print('Имя:    ', self.name)
        print('Возраст:', self.age, self.years_parameter)
        print('Телефон:', self.phone)
        print('E-mail: ', self.email)
        print('Индекс: ', self.email)
        print('Адрес:  ', self.email)
        if self.additional_info:
            print('\nДополнительная информация:')
            print(self.additional_info)

    def print_entrepreneur_info(self):
        print('\nИнформация о предпринимателе')
        print('ОГРНИП  ', self.ogrnip)
        print('ИНН     ', self.ogrnip)
        print('Банковские реквизиты')
        print('Р/С     ', self.bank_account)
        print('Банк    ', self.bank_name)
        print('БИК     ', self.bik)
        print('К/С     ', self.correspondent_account)

    def update_general_info(self):
        self.name = input_data(necessary_type=str, )


def input_data(necessary_type: Any = None,
               input_phrase: str = '',
               exception_phrase: str = '',
               max_len: Optional[int] = None):
    while True:
        str_input = input(f"{input_phrase}: ")

        try:
            if max_len and len(str_input) != max_len:
                raise AssertionError(f"Количество символов должно быть равным {max_len}")
            elif isinstance(necessary_type, Optional[str]):
                input_prompt = str_input
            else:
                input_prompt = necessary_type(str_input)
        except ValueError:
            print(exception_phrase)
        except AssertionError as ae:
            print(ae)

        else:
            return input_prompt


def submenu_update_info():

    print(SEPARATOR)
    print('1 - Личная информация')
    print('2 - Информация о предпринимателе')
    print('0 - Назад')


def main():
    print('Приложение MyProfile')
    print('Сохраняй информацию о предпринимателе и выводи ее в разных форматах')

    while True:
        print(SEPARATOR)
        print('1 - Ввести или обновить информацию')
        print('2 - Вывести информацию')
        print('0 - Завершить работу')

        match input('Введите номер пункта меню: '):

            case '0':
                break
            case '1':
                # submenu 1: edit general info
                submenu_update_info()
                entrepreneur = Entrepreneur()
                # entrepreneur.name = input_data(necessary_type=str, input_phrase="Введите имя")
                # entrepreneur.email = input_data(necessary_type=str, input_phrase="Введите e-mail")
                entrepreneur.phone = "+7" + str(input_data(necessary_type=int,
                                                           input_phrase="Введите номер телефон (+7ХХХХХХХХХХ)",
                                                           max_len=10))
                print(entrepreneur.phone)

            case '2':
                inp = input_data(necessary_type=int, exception_phrase="Введите числовые данные", max_len=1)
                print(inp)
            case _:
                print("Введите корректный пункт меню")


if __name__ == '__main__':
    main()
