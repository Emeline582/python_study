# Write a program that:
# Takes a transaction amount and account type ("Standard" or "Premium") as input.
# If the account type is "Standard":
# Check if the amount is above 500:
# If it is, print "Transaction exceeds the limit for Standard accounts."
# If not, print "Transaction approved."
# If the account type is "Premium":
# Check if the amount is above 1,000:
# If it is, print "Transaction exceeds the limit for Premium accounts."
# If not, print "Transaction approved."
# Otherwise “Wrong account type”

trans_amount=int(input("enter amount:"))
account_type=input("is account standard/premium")
if account_type=="standard":
    if trans_amount>500:
         print("Transaction exceeds the limit for Standard accounts")
    else:
        print("Transaction approved")
else:
  if trans_amount>1000:
      print("Transaction exceeds the limit for Premium accounts.")
  else:
      print("Transaction approved")
    else:
        print("Wrong account type")

# 1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
# If start_date comes before end_date, print "Valid period",
# If start_date is after end_date, print "Invalid period".
# If both dates are the same, print "One-day period".
# 2.Given two strings str1 and str2, write a conditional statement that checks:
# If str1 is longer than str2, print "str1 is longer".
# If str2 is longer than str1, print "str2 is longer".
# If both have equal length, print "Both are of equal length".

start_date = '2024-01-01'
end_date = '2024-12-31'
if start_date < end_date:
    print("valid period")
elif start_date >end_date:
    print("invalid period")
else:
    print("one-period")

# .Given two strings str1 and str2, write a conditional statement that checks:
# If str1 is longer than str2, print "str1 is longer".
# If str2 is longer than str1, print "str2 is longer".
# If both have equal length, print "Both are of equal length".
str1=input("enter str1:")
str2=input("enter str2:")
if len(str1)>len(str2):
    print("str1 is longer")
elif len(str2)>len(str1):
    print("str2 is longer")
else:
    print("Both are of equal length")

#3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
# Prints "Access Granted" if user_id is in valid_ids.
# Prints "Access Denied" if user_id is not in valid_ids.
valid_ids = [101, 102, 103]
user_id = 105
if user_id == valid_ids:
    print("Access Granted") 
else:
    print("Access Denied")
# 4.Given a variable value that could be of any type, write a conditional statement that:
# Prints "String Detected" if value is a string.
# Prints "Integer Detected" if value is an integer.
# Prints "Unknown Type" for any other type.
value=input("enter value:")
if value==str(value):
    print("String Detected")
elif value==int(value):
    print("Integer Detected")
else:
    print("Unknown Type")
# 5.Given x = 7 and y = 14, write nested conditional statements that print:
# "x and y  both even" if both x and y are even numbers.
# "Only y isare even" if only y is even.
# "Neither x nor y are even" if both are odd.

x = 7
y = 14
if x%2==0 and y%2==0:
    print("x and y  both even")
elif y%2==0 and x%2!=0:
    print('Only y is even')
elif x%2==0 and y%2!=0:
    print('Only x is even')
else:
  print("Neither x nor y are even")

