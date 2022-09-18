# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

some_text = 'Некоторый абвгде текст, абв абвгдешка содержащий словосочетание абв букв абв абв "а б в"'
print(some_text)

def del_some_words(some_text):
    some_text = list(filter(lambda x: 'абв' not in x, some_text.split()))
    return " ".join(some_text)

some_text = del_some_words(some_text)
print(some_text)