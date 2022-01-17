#THIS IS UR OWN CODE FIND OUT WHATS WRONG IN THIS
'''
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("Type 'encode' to encrypt , type 'decode' decrypt:")
choosen_word=input(" ").lower()
if choosen_word == "encode":
    print("type yor message")
    message=input(" ")
    print("type the shift number")
    shift_number=int(input(" "))
    d=[]
    c=[]
    for i in message:
        d+=i
    print(d)
    for i in d:
        if i in alphabets:
            e=alphabets.index(i)
            qt=alphabets[c+9]
            c + str(qt)

    print(c)
'''

#SIMPLE FUNCTIONS:
'''def greet():
    print("hello")
    print("noob")
greet()
def greet_with_name(name):
    print(f"hello {name}")
greet_with_name("sid")
def greet_with(name,location):
    print(f"hello {name}")
    print(f"what is it like in {location}")
greet_with("sid","vizag" )
'''
#QUESTION FOR FINDING NO>OF CANS REQUIRED
'''h=int(input("ht of wall"))
l=int(input("length of wall"))
def a(h,l):
    c=(h*l)/5
    print(round(c))
a(h,l)
'''

#PRIME NUMBER CHECKER
'''def prime_checker(number):
    is_prime=True
    for i in range (2, number):
        if number % i ==0:
            is_prime=False
    if is_prime:
        print("its a prime number")
    else:
        print("its not a prime number")
prime_checker(5)
'''
#CEASAR CYPHER
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def ceaser(plain_text, shift_amount):
     cipher_text=""
     if direction =="encode":

         for letter in plain_text:
             a=alphabet.index(letter)
             if a+shift_amount>26:
                 c=alphabet[a+shift_amount -26 ]
             else:
                 c=alphabet[a+shift_amount]
             cipher_text +=c
         print("the encoded test is "+cipher_text)
     elif direction=="decode":

        for i in plain_text:
            h=alphabet.index(i)
            if h- shift_amount<0:
                i=alphabet(26+h-shift_amount)
            else:
                i=alphabet[h- shift_amount]
            cipher_text+=i
        print("the decrypte text is "+cipher_text)
ceaser(text,shift)
print("do u want the program to run again "
      "yes or no")
choice=input("enter your choice")
if choice=="yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text, shift)
else:
    print("program is over")
