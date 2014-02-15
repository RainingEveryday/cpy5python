#1 Displaying an integer in reversed form:

def reverse_int(n):
    if n<10:
        print(n)
    else:
        num = str(n)
        for i in range((len(num)-1),-1,-1): #Or use [::-1] to print reverse
           print(num[i], end="")

prompt = int(input("Please input an integer that you wish to reverse in display: "))
reverse_int(prompt)
