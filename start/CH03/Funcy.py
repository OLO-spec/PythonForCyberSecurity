#!/usr/bin/env python3
# example workign with Functions
#By D - 5/3/2026

#functions assinment
#defining message to insert in loop
def send_message():
    for x in range(10): 
        print ("Yeah it is!")

#loop with function
if input("Is today good day? l{y/n} ") == "y":
    send_message()
else:
    print("I'm sorry you fell that way :(, I hope it gets better! ")








#TRhis is my fuinction
def print_me( my_message ):
    print(my_message)
    return "it worked!"

def say_hello(num_times):
    for x in range(num_times):
        print("Hello World")

#This is calling my function
print_me( "This is a function" )

result = print_me("This is another function with a return value")
print(result)

say_hello(3)