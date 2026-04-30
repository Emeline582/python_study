# Write a program that displays a numbers 1 to 50 inside a list.

numbers=list(range(1,51))
print(numbers)

# From 1 above display the ones divisible by 7 or 5 inside a list.
divisible=[]

for i in numbers:
    if i%7==0 or i%5==0:
        divisible.append(i)
        
print(divisible)

# Find sum and average of values in the range between 10 to 40

# Sum and average between 10 and 40
numbers = list(range(10, 41))
total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
# print("Average:", average)

# Put in a list the first 10 odd numbers between 10 to 50.
lstn=list(range(10, 51))
odds = []
for i in lstn :
    if i % 2 != 0:        
        odds.append(i)    
    if len(odds) == 10:   
        break

print("First 10 odd numbers:", odds)


# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
lstn=list(range(1,11))
num = int(input("Enter a number: "))
for i in lstn:
    print(f"{num} x {i} = {num * i}")

# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
# Count even numbers between 1 and 50
count = 0
numbers=list(range(1,51))
for i in numbers:
    if i % 2 == 0:
        count += 1
print("Number of even numbers between 1 and 50:", count)

# ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
# Display the total quantity of the 3 above.

ls1 = [("Jay", '20'), ("Mo", '30'), ("Mya", '32')]
total = sum(int(qty) for _, qty in ls1)
print("Total quantity:", total)