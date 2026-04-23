# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.
x=int(input("enter x:"))
y=int(input("enter y:"))
z=int(input("enter z:"))
if x >=y and x >=z:
 print("x is largest")
elif y>= x and y >=z:
 print("y is largest")
else:
 print("z is largest")
# 2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temp=int(input("enter temp:"))
if temp >30:
 print("The temp is too high")
elif temp >15:
 print("Normal temp")
else :
 print("Cold temp")
# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x=38
y=78
if x > 10 < 20 and y > 100:
 print("Conditions met")
else:
 print("Conditiions not met")
# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password=input("enter password:")
if password=="secret123":
 print("Access granted")
else:
 print("Access denied")
# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
student_score=int(input("enter student score:"))
attendance=int(input("enter the attendance:"))
if student_score > 90 and attendance > 80:
 print("Ezxcellent student")
else:
 print("Good score but attendance needs improvement")
