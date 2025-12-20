def simple_write():
    text = input("тексв в файл: ")
    with open('b', 'w', encoding='utf-8') as file:
        file.write(text)

def simple_append():
    text = input("текст для добавления: ")
    with open('b', 'a', encoding='utf-8') as file:
        file.write(text + '\n')
simple_write()



print("Текст записан в b")
