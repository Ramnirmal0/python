num=int(input("\n\nEnter the number to be listed : "))
conv=[num]
output=list(map(int,str(conv[0])))
print("The list = ",output)

# list reversing

for x in reversed(range(len(output))):
       print("The reversed list = " , output[x])
       
       
