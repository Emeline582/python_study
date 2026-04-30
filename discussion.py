# Name=input("enter name:")
# Account_balance=100000
# Amount_requested=input("enter amount:")
# Amount_requested=int(Amount_requested)
# trans=30
# if Amount_requested > Account_balance:
#      print(f'  Hello (Name) Transaction unsucceessful insufficient funds to withdraw (Amount_requested)your balance is(Account_balance)')
# else:
#  new_balance= Account_balance - (Amount_requested+trans)
# print(f'Hello (Name) (Amount_requested) withdrawn successfully new balance (Account_balance)')
 
dict={
   "pen":200,
   "books":200,
   "erasers":200,
   "pencils":150,
}
if (dict["pen"])>100:
   print("valid stock:pen")
else:
   print("out of stock")
if (dict["books"])>100:
    print("valid stock:books")
else:
   print("out of stock")
if (dict["erasers"])<100:
    print("valid stock:erasers")
else:
   print("out of stock")
if (dict["pencils"])>100:
   
       print("valid stock:pencils")
else:
   print("out of stock")

marks=[60,80,87,69,78]
average=sum(marks)/len(marks)
print(average)
if average>= 70:
       grade='A'
elif average<70 and average >=50:
       grade='B'
elif average<50 and average >=40:
       grade='C'
else:
     grade='retake the subject'
     print(grade)

data=input('Enter remaining data:')
data=float(data)
if data==0:
     res="block browsing"
elif data<100:
     res=f'your {data}MB is below 100'
else:
     res=f'you have {data}MB'
     print(res)

     items=int(input('enter number of items'))
     whole_tresh=5

     if items>5:
          reward_points=items/whole_tresh
          val=f'you have bought{items} items you have earned {reward_points} reward points'
     else:
      rem= whole_tresh-items
      val=f'you have bought {items}items add '