date=int(input("enter the date:"))
month=int(input("enter the month:"))
year=int(input("enter the year:"))
if year%4==0:
    print("leap year")
else:
    print("non leap year")
print(date,"/",month,"/",year) 
