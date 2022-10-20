strsum = lambda a, b: str(a) + b
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''

    for char in data: #Если предыдущ и текущ символы не совпадают то добавляем посчитанное количество символов и сам символ в расшифровку
        if char !=prev_char:
            if prev_char:
                encoding += strsum (count,  prev_char)
            count = 1
            prev_char = char
        else:  #иначе инкрементируем счетчик (если символы совпадают)
            count +=1
    else:
        encoding += strsum (count,  prev_char)
        return encoding

def rle_decode(data):
    decode = ''
    count = ''
    for char in data: #если символ число
        if char.isdigit(): #присоединяем его к счетчику
            count += char
        else: # если символ не число печатаем необходимое число символов в расшифовку
            decode += char * int(count)
            count = ''
    return decode

if __name__ == '__main__':
    decoded_val = rle_decode('4W4A3E8S6R')
    print (decoded_val)
    with open("G:\\Desktop\\Python\\homework6_py\\decode.txt", "a") as file:
        file.write(f'{decoded_val} \n')

    with open("G:\\Desktop\\Python\\homework6_py\\encode.txt", "r") as file:
        readfile = file.read()
    encoded_val = rle_encode (readfile)
    print(encoded_val)

