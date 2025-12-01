# Enter your code here. Read input from STDIN. Print output to STDOUT


def is_even(n: int):
    remainder = n % 2
    
    if remainder == 0:
        return True
    else:
        return False


n = int(input())

for a in range(n):
    s = input().strip()
    s_length = len(s)


    line_1 = ""
    line_2 = ""     
    for i in range(s_length):
    
        if is_even(i):
            line_1 += s[i]
        else:
            line_2 += s[i]
    
    print(line_1 + " " + line_2)