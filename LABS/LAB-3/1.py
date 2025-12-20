def read_file(method='all'):
    try:
        if method == 'all':
            with open('a', 'r', encoding='utf-8') as file:
                return (file.read())
        elif method == 'line':
            with open('a', 'r', encoding='utf-8') as file:
                return file.read()
    except:
        return 'FileNotFoundError'



print(read_file(method='all'))