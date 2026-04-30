# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.
x=int(input("enter x:"))
y=int(input("enter y:"))
z=int(input("enter z:"))
if x >y and x >z:
 print(x)
elif y> x and y >z:
 print(y)
else:
 print(z)

 a=input('enter a:')
 a=int(a)
 b=input('enter b:')
 b=int(b)
 c=input('enter c:')
 c=int(c)
 d=input('enter d:')
 d=int(d)
 if a >b and a >c and a >d:
  print(a)
 elif b >a and b >c and b >d:
  print(b)
 elif c >a and c >b and c >d:
  print(c)
 else:
  print(d)
# 2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temp=int(input("enter temp:"))
if temp >30:
 print("The temp is too high")
elif temp >15:
 print("Normal temp")
else :
 print("Cold temp")


User_balance=input("enter users balance:")
User_balance=int(User_balance)
if User_balance < 100:
  print("insufficient funds")
elif User_balance >100 and User_balance <1000:
  print("moderate balance")
else:
  print("high balance")
# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x=38
y=78
if x > 10 and x<= 20 and y > 100:
 print("Conditions met")
else:
 print("Conditiions not met")
number=45
if number < 10:
 print("small")
elif number >10 and number <50:
 print("medium")
else:
 print("large")
# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password=input("enter password:")
if password=="secret123":
 print("Access granted")
else:
 print("Access denied")

 correctemail="admin@gmail.com"
 correctpassword="admin123"
 email=input("enter your email:")
 password=input("eneter your password:")
 if email ==correctemail and password==correctpassword:
  print("access granted")
 else:
  print("access denied")
# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
student_score=int(input("enter student score:"))
attendance=int(input("enter the attendance:"))
if student_score > 90 and attendance > 80:
 print("Ezxcellent student")
else:
 print("Good score but attendance needs improvement")
