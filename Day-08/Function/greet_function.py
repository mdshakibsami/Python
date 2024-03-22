#Simple Function
def greet():
    print("Hello!")
greet()

#This function is for formating
def line():
    print("----------------------------------------------")
line()
    

#Function with Argument
def greet_with_name(name):
    print(f"Hello! {name}")
greet_with_name("Md Shakib")
line()

#Function with multiple Arguments
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"You live in {location}")
greet_with("Shakib","London")
line()
#Calling a function with keyword Arguments
greet_with(location="switzerland",name="Shakib")
line()