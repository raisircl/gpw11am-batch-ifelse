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

'''
Assignment 1: enter sale price and cost price of a 
              product and calculate profit or loss.
Q2: enter 2 nos and print which one is greater.
Q3: enter a number is check is it even or odd.
Q4: enter a number is check is it positive or negative.
Q5: enter marks of 5 subjects and calculate total, and percentage.
    print pass or fail if percentage is greater than 40.
Q6: enter basic salary of employee and calculate net salary.
    Rule: if basic salary is less than 10000 then HRA=10% of basic, DA=90% of basic
          if basic salary is greater than 10000 then HRA=20% of basic, DA=95% of basic
'''