#--------QUESTION 1ST------------

# name="Shruti Kishor Morey"
# print(name[0])
# print(name[-1])
# print(len(name))

#--------QUESTION 2ND-----------

# s1="Hello"
# s2="World"
# print(s1+" "+s2)

#---------QUESTION 3RD----------

# text = "Python Programming" 
# print(text[0:6])
# print(text[-6:])
# print(text[1::2])
# print(text[::-1])

#---------QUESTION 4RT----------

# string =" i love python programming "
# print(string.strip())
# print(string.title())
# print(string.count("o"))

# a="123abc"
# print(a.isalnum())

#----------QUESTION 5TH----------

# x= "John"
# y= 25
# print("My name is {} and I am {} years old.".format(x,y))
# print(f"My name is {x} and i am {y} years old.")

#---------QUESTION 6TH-----------

# sentence = "Coding in Python is fun"
# print(sentence.replace("fun","awesome"))
# print(sentence.find("Python"))
# print(sentence.upper())

#---------QUESTION 7TH-----------
# Take a user input string and check if it is a palindrome (same forwards and backwards).

sen=input("Enter a string: ")
rev=""
for ch in sen:
    rev=ch+rev
if rev == sen:
    print("The given string is palindrom") 
else:
    print("The given string is not palindrom")     