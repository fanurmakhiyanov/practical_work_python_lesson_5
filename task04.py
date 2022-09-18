# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(data): # кодирование (сжатие)
    encoding = ''
    prev_char = ''
    count = 1
    
    if not data: return ''
    
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
            
    else:
        encoding += str(count) + prev_char
        return encoding

def rle_decode(data): # расшифрока (восстановление)
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

some_text = 'AAAAAABBBBBBBBCCCCCCCCCDDDDDDEEEEEEEEEEEEEE'
print(f'Исходное значение: {some_text}')

encoded_val = rle_encode(some_text)
print(f'Значение после сжатия: {encoded_val}')

decoded_val = rle_decode(encoded_val)
print(f'Значение после восстановления: {decoded_val}')