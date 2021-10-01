books = {'Financial': 'Theodor Draiser', 'Rich dad, poor dad': 'Robert Kiyosaki', 'Think and get rich': 'Napoleon Hill'}
readers = {}

def get_info():
    print(f'На данный момент список читателей такой:\n{readers}')
    print(f'Список книг такой:\n{books}')

def give_book():
    book = input(f'Какую книгу вы хотите получить? Выберите из\n {books}\nВведите только название: ')
    reader = input('Введите имя: ')
    author = books.get(book)
    if book in books:
        if reader in readers:
            for k, v in readers.items():
                if k == reader:
                    v.update({book: author})
        else:
            readers.update({reader: {book: author for k, v in books.items()}})
        books.pop(book)
    else:
        print('Эта книга недоступна')
    print('Ваша заявка успешно оформлена!')
    get_info()

def take_back_book():
    choice = input('Вы хотите взять книгу или вернуть? (1 или 2) ')
    if choice == '1':
        give_book()
    elif choice  == '2':
        reader = input('Ваше имя: ')
        if reader in readers.keys():
            for v in readers.values():
                books.update(v.items())
            readers.pop(reader)
    get_info()
    take_back_book()
            
def manager():
    get_info()
    give_book()
    print('========================')
    take_back_book()
    print('========================')
    

manager()