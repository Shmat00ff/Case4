"""Case-study #4 Анализ текста
Разработчики: Шматов Денис, Баянова Анна

"""

text = input("Введите текст: ")
count_sentens = text.count('.')
count_words = text.count(' ')+1
count_syllables = 0
if text.isdigit() == 0:
    punctuation = ['(', ')', '?', ':', ',', '.', '!', '/', '"', "'", ' ']
    for i in punctuation:
        text = text.replace(i,"")
    vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я', 'А', 'О', 'И', 'Е', 'Ё', 'Э', 'Ы', 'У', 'Ю', 'Я']
    for j in text:
        for i in vowels:
            if j == i:
                count_syllables += 1
    ASL = count_words / count_sentens
    ASW = float(count_syllables) / float(count_words)
    FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)
    print('Предложений:', count_sentens)
    print('Слов:', count_words)
    print('Слогов:', count_syllables)
    print('Средняя длина предложения в словах:', ASL)
    print('Средняя длина слова в слогах:', ASW)
    print('Индекс удобочитаемости Флеша:', FRE)
    if FRE < 26:
        print('Текст трудно читается (для выпускников ВУЗов).')
    elif 25 < FRE < 51:
        print('Текст немного трудно читать (для студентов).')
    elif 50 < FRE < 80:
        print('Простой текст (для школьников).')
    elif FRE > 79:
        print('Текст очень легко читается (для младших школьников).')
else:
    print('Вы ввели число.')