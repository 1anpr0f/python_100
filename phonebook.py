# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input("Enter number of entries: "))
phone_book = {}
for _ in range(n):
    entry = input('enter name and phone number: ').split()
    name ,phone_number=entry[0] ,entry[1]
    phone_book[name]=phone_number
try:
    while True:
        query = input("Enter name to query: ").strip()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
except EOFError:
    pass

