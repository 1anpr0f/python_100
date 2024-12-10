
def reverse_card_number(card):
    sum_of_odd_digits = 0
    reversedCard = card [::-1]
    odd_digits = reversedCard [::2]
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    sum_of_even_digits = 0
    even_digits = reversedCard[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10 :
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_even_digits + sum_of_odd_digits
    return total % 10 == 0
def main():
    card = "2345-2345-2344-3222"
    trans_credit  = str.maketrans({'-' :'',' ':''})
    translated_credit = card.translate(trans_credit)
    print(translated_credit)
    if reverse_card_number(translated_credit):
        print('valid')
    else:
        print('invalid')
main()
