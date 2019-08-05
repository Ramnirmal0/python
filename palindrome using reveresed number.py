def reverse(num):
       temp=num
       rev=0
       while(num>0):
              rem=num%10
              rev=(rev*10)+rem
              num=num//10
       print("/n Reversed Number is = ",rev)
       check(temp,rev)
def check(num,rev):
       if(num == rev):
              print("The number is palindrome")
       else:
              print("The number is not palindrom")
num=int(input("Enter the number to be checked : "))
reverse(num)

