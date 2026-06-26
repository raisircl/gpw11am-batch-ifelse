'''Decision Control Instruction: As we know a problem can not be 
solve without decision so to take decision in python 
we use if else statement.
syntax: 
if condition:
    statement1
    statement2
else:
    statement3
    statement4
'''
mrp=float(input("Enter mrp of Book:"))
dis=0
net=0
if mrp>=500:
    dis=mrp*10/100
else:
    dis=mrp*5/100

net=mrp-dis
print(f"MRP={mrp}, Discount={dis}, Net Price={net}")

