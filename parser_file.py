input = input('Введите абсолютный путь к .inc файлу')
try:
    with open (input, 'r', encoding="utf-8") as f:
        print(f.read())
except:
    print('There is no such file in this directory')
    
