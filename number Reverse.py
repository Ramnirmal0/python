num=int(input("Enter the number to reverse"))
temp=num
rev=0
while(num>0):
       rem=num%10
       rev=(rev*10)+rem
       num=num//10
print("the answer is",rev)
