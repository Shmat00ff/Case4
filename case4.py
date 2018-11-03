"""Case-study #4 Анализ текста
Разработчики: Шматов Денис, Баянова Анна

"""
from ru_local4 import *

text = input("{}".format(textinput))
count_sentens = text.count('.')
count_words = text.count(' ')+1
count_syllables = 0
if text.isdigit() == 0:
    for i in punctuation:
        text = text.replace(i, "")
    for j in text:
        for i in vowels:
            if j == i:
                count_syllables += 1
    ASL = count_words / count_sentens
    ASW = float(count_syllables) / float(count_words)
    FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)
    print("{}".format(senteses), count_sentens)
    print("{}".format(words), count_words)
    print("{}".format(syllables), count_syllables)
    print("{}".format(asl), ASL)
    print("{}".format(asw), ASW)
    print("{}".format(fre), FRE)
    if FRE < 26:
        print("{}".format(impossible))
    elif 25 < FRE < 51:
        print("{}".format(hard))
    elif 50 < FRE < 80:
        print("{}".format(medium))
    elif FRE > 79:
        print("{}".format(easy))
else:
    print("{}".format(ifint))
