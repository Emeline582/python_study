# Write a program that checks login credentials:
# "Access granted" if email = "admin@gmail.com" and password = "Admin@123"
# "Wrong password" if email is correct but password is wrong
# "Email not found" otherwise
correctemail="admin@gmail.com"
correctpassword="admin123"
email=input("enter your email:")
password=input("enter your password:")
if email ==correctemail and password==correctpassword:
    print("Access granted")
elif email ==correctemail and password!=correctpassword:
    print("wrong password")
else:
    print("Email not found")
# 2.
# Create a program that validates an email:
# "Invalid email" if it does not contain "@" or "."
# "Gmail account" if it ends with "@gmail.com"
# "Other email provider" otherwise
email= input("Enter your email:")
if email.find('@')==-1 or email.find('.')==-1:
     print("invalid email")
 elif email endswith "gmail.com" :
#   print("Gmail account")
# else:
#   print("other email provider")
# 3.
# Write a program that checks password stren gth:
# "Weak" if length < 6
# "Moderate" if length 6–10 and contains at least one digit
# "Strong" if length > 10 and contains both digits and uppercase letters
password=input("Enter password:")
if len(password) <6:
   print("weak")
elif len(password)>6 and len(password)<10:
   print("Moderate")
else:
   print("Strong")

# 4.
# Write a program that checks a password:
# "Invalid" if it does not start with a capital letter
# "Invalid" if it does not end with a number
# "Valid password" otherwise
#password=input("Enter password:")


# 5.
# Write a program that takes a number and checks:

# "Fizz" if divisible by 3
# "Buzz" if divisible by 5
# "FizzBuzz" if divisible by both
# Otherwise print the number
number=input("enter number:")
number=int(number)
if number % 3==0 :
    print("fixx")
elif number % 5==0:
    print("buzz")
elif number% 3==0 and number % 5==0:
  print("fixxbuzz")
else:
   print("number")
# 6.
# Create a program that takes a score and prints a grade:
# A (≥ 80)
# B (70–79)
# C (60–69)
# D (50–59)
# F (< 50)
score=input("Enter score:")
score=int(score)
if score >= 80:
 print("A")
elif score >70:
 print("B")
elif score >60:
 print("C")
elif score >50:
 print("D")
else:
 print("F")
# 7.
# Create a program that takes two numbers and prints:
# "Equal" if same
# "First is greater"
# "Second is greater"

num1=input("Enter num1:")
num2=input("Enter num2:")
if num1==num2 :
   print("Equal")
elif num1>num2:
   print("num1 is graeter")
else:
   print("num2 is greater")
# 8.
# Write a program that takes a day number (1–7) and prints:
# Weekday (1–5)
# Weekend (6–7)
# Invalid input otherwise
daynumber=input("Enter daynumber:")
daynumber=int(daynumber)
if daynumber <=5:
   print("weekday")
elif daynumber <=7:
   print("weekend")
else:
   print("invalid input")

# 9.
# Create a program that takes a temperature and prints:
# "Freezing" if ≤ 0
# "Cold" if 1–15
# "Warm" if 16–30
# "Hot" if > 30
temp=input("enter temp:")
temp=int(temp)
if temp <=0:
   print("freezing")
elif temp<15:
   print("Cold")
elif temp <30:
   print("warm")
else:
   print("hot")


# 10.
# Create a program that takes a year and prints:
# "Leap year" if divisible by 4
# "Century year" if divisible by 100
# "Common year" otherwise
year=input("Enter year:")
year=int(year)
if year % 4==0:
   print("leap year")
elif year % 100==0:
   print("century year")
else:
   print("common year")