Print("Hello World")


#Adding a feature which can determine the factorial of a input

num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial not possible is negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

   
   # Program to check if a number is prime or not

num = 407

# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")

   
   
   # Store input numbers:  
num1 = input('Enter first number: ')  
num2 = input('Enter second number: ')  
  
# Add two numbers  
sum = float(num1) + float(num2)  
# Subtract two numbers  
min = float(num1) - float(num2)  
# Multiply two numbers  
mul = float(num1) * float(num2)  
#Divide two numbers  
div = float(num1) / float(num2)  
# Display the sum  
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))  
  
# Display the subtraction  
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))  
# Display the multiplication  
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))  
# Display the division  
print('The division of {0} and {1} is {2}'.format(num1, num2, div))  


#added a feature
num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")
