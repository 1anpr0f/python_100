numbers = "1234-1233-1324-2324"
numbers_trans =  str.maketrans({"-":""," ":""})
translated_num = numbers.translate(numbers_trans)
print(int(translated_num))
