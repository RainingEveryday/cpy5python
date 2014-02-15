#1 Displaying an integer in reversed form:

def reverse_int(n):
    if n<10:
        print(n)
    else:
        num = str(n)
        for i in range((len(num)-1),-1,-1):
           print(num[i], end="")

reverse_int(34567)
