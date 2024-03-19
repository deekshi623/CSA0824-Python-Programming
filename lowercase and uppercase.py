string="my name is SRUJANA"
lowercase=0
uppercase=0
for char in string:
    if char.islower():
         lowercase+=1
    elif char.isupper():
         uppercase+=1
print(f"number of lowercase is:{lowercase}")
print(f"number of uppercase is:{uppercase}")  
