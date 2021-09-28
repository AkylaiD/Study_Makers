books = {'Financial': 'Theodor Draiser', 'Rich dad, poor dad': 'Robert Kiyosaki', 'Think and get rich': 'Napoleon Hill'}
readers = {}

def get_info():
    print(f'На данный момент список читателей такой:\n{readers}')
    print(f'Список книг такой:\n{books}')

# def manager():


def give_book():
    book = input(f'Какую книгу вы хотите получить? Выберите из\n {books}\nВведите только название: ')
    reader = input('Введите имя: ')
    if book in books:
        readers.update({reader: {k: v for k, v in books.items()}})
        books.pop(book)
    print('Ваша заявка успешно оформлена!')

def take_back_book():
    choice = input('Вы хотите взять книгу или вернуть? ')
    if choice == 'взять':
        give_book()
    elif choice  == 'вернуть':
        reader = input('Ваше имя: ')
        if reader in readers:
            books.update(k2: v2 for v2 in readers.values())
            readers.pop(reader)
    get_info()
            
    # get_info()


get_info()
print('========================')
give_book()
print('========================')
take_back_book()
print('========================')
# manager()
# print('========================')

