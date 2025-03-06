#string[start:stop:step]
#start: The starting index of the slice (inclusive). Defaults to 0.
#stop: The ending index of the slice (exclusive).
#step: The step size (optional). Defaults to 1.
text = (input('enter name: '))
def string_slicing(text):
    count = 0
    for char in text.lower():
        count += 1
    print(count)
    if count % 2  == 0:
        print(text[::2])#odd str
    elif count // 2 == 1:
        print(text[::-1])#reverse
    else:
        print(text[1::2])#even str
string_slicing(text)
