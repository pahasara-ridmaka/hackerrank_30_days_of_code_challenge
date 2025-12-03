# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phone_book = {}

for i in range(n):
    name_number = input().strip().split()
    name = name_number[0]
    number = name_number[1]    
    phone_book[name] = number

try:
    while True:
        name = input().strip()
        if name in phone_book:
            print(f"{name}={phone_book[name]}")
        else:
            print("Not found")
except EOFError:
    pass