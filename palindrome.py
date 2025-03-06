in_put = input('enter text: ')
def palindrome(s):
    in_put = ''.join(char.lower() for char in s if char.isalnum())
    if in_put == in_put[::-1]:
        print('is a palindrome')
    else:
        print('not a palindrome')
palindrome(in_put)

