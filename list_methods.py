#append->adds items at the end of the list
my_list=["mike","Jane","Alex",1000,200,2000,True,False]
my_list.append('Donkey')
print(my_list)

#insert->adds an item at specified index
my_list.insert(1,'Mary')
print(my_list)

#pop->removes an item from a specified index
my_list.pop(3)
print(my_list)

#task
lst=[10,20,30,['Jane','Mary',[1000,2000,3000,]],40,50,60]
#using methods
#add 70 at ythe end of the list
lst.append('70')
print(lst)

#add 1500 btn 1000 and 2000

print(lst[3][2])
lst[3][2].insert(2,'1500')
print(lst)

#delete 2000
print(lst[3][2])
lst[3][2].pop(1)
print(lst)

#sort
lst1=[1,50,10,20,5,2]
lst1.sort(reverse=True)
print(lst1)
lst1=['Mike','Jane','Alex']
lst1.sort()
print(lst1)

#remove
lst1.remove('Alex')
print(lst1)

#extend
lst2=['Mike','Jane','Alex']
lst1=[1,50,10,20,5,2]
lst3=lst1+lst2
lst2.extend(lst1)
print(lst3)

#count
print(lst2.count("Mike"))

#copy
lst2=lst2.copy()
print(lst2)

#clear
my_list.clear()
print(my_list)

#in membership
lst2=['Mike','Jane','Alex']
print('alex' in lst2)