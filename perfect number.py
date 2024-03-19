Number=int(input("enter the number:"))
sum=0
for i in range(1,Number):
    if(Number%i==0):
        sum=sum+i
if(sum==Number):
    print("the number %d is perfect number"%Number)
else:
    print("the number %d is not perfect number"%Number)
    
