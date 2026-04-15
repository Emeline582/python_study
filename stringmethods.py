text="software development"
#capitalizen->makes the first character uppercase while the rest lowercase
text1=text.capitalize()
print(text1)

#upper
text2=text.upper()
print(text2)

#casefold
text3=text.casefold()
print(text3)

#count->counts the no of appearance of a spefic character in string
print(text.count("e"))

#strip ->removes leading and trailing spaces
text_strip="  software developer   "
print(len(text_strip))

text_strip=text_strip.strip()
print(len(text_strip))

#find->returns the index the first occurence of a character returns-1 if tyhe character is not available
print(text.find("d"))

#index->returns the index of the first occurence of a character returns an arror if the character is not available
text= "software Developer"
print(text.index("D"))

#replace
text=text.replace("software","python")
print(text)

#split
email="emeline@gmail.com"
split_email=email.split("@")
print(split_email)
text="software Developer"
txt=text.split()
print(txt)

#quiz
text=" jUnioR deVelOper  "

text=text.strip()
text=text.capitalize()
print(text)
