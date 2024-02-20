# creating a calculator using functions

#ADDITION
#prompt the user to enter a number of their choice
s = float(input("Enter a number:"))
r = float(input("Enter a number:"))
#declaring a function 
def addition(s,r):
    sum = s + r
    return sum 
#calling the function
add = addition(s,r)
#sum output
print("This is the sum:",add)



#SUBTRACTION
#prompt user to enter a number of their choice
f = float(input("Enter a number:"))
g = float (input("enter a number:"))
#declaring a function
def subtraction(f,g):
    diff = f - g
    return diff
#calling the function
difference = subtraction(f,g)
#difference output
print("Difference output:",difference)

#MULTIPLICATION
#prompt the user to enter a number of their choice
j = float(input("Enter a number:"))
w = float(input("Enter a number:"))
#declaring a function
def multiplication(j,w):
    prod = j * w
    return prod
#calling the function
product = multiplication(j,w)
#product output
print("Product output:",product)


#DIVISION
#prompt the user to input a number of their choice
v = float(input("Enter a number:"))
q = float(input("Enter a number:"))
#declaring a function
def division(v,q):
    divide = v / q
    return divide
#calling the function
div = division(v,q)
#print the output
print("division output:",div)