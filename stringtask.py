#clean up " JOHn " to lowercase
text=  " JOHn ."
text=text.replace(".","")
text=text.strip()
text=text.lower()
print(text)

text="The Dog Breed is  German Shepard"
print(text[8:24])

text="Defeats for the Clinton forces,this was her moment of triumph"
print(text[16:30])


#clean
first_name=" Joh.n"
last_name=" Do,e"
first_name=first_name.replace(".","")
print(first_name)
last_name=last_name.replace(",","")
print(last_name)

full_name=first_name+last_name
full_name=full_name.strip()
print(full_name)

text="The lazy dog; ran so fast; it hit the wall"
split_text=text.split(";")
print(split_text)



text= '["E","W","C"]' 
text=text.replace("[","")
text=text.replace("]","")
text=text.replace(",","")
text=text.replace('"','')

print(text)
                  
