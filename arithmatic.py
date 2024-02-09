

print('1.ADD ,2.SUB , 3.MUL, 4.DIV')
choice=int(input("Enter Your Choice 1 ,2 ,3 ,4 "))
a = int(input('Enter First number: '))
b = int(input('Enter Second number '))

if choice== 1: 
    sum= a+b
    print('sum:',a+b)
elif choice== 2:
    SUB= a-b
    print('SUB:',a-b)

elif choice== 3:
    MUL=a*b
    print('MUL:',a*b)
elif choice== 4:
    DIV=a/b
    print('DIV:',a/b)
else:
    print("Enter the Correct Choice")
