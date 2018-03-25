print("Hello world")
print('What\'s up?')
print('Let\'s get started')

##asking name##

spy_name = input("What is your spy name?")
print(spy_name)
print("Welcome"+""+spy_name+" in Acadview")

spy_salutation = input("What should we call you (Mr. or Ms.)?")
print(spy_salutation)
print(spy_salutation+""+spy_name)

spy_name = spy_salutation+""+spy_name
print(spy_name)

#####profile of spy#####
spy_name = input("Welcome!!! you must tell your spy name first.")
if len(spy_name) > 0:
    spy_name = input("What is your name?")
    spy_salutation = input("What should we call you (Mister or Misses)?")
    print("Welcome" + " " + spy_salutation + " " + spy_name + "to Acadview")
    spy_name = spy_salutation + " " + spy_name
    print(spy_name)
    print("Alright" + " " + spy_name + " " + " we would like to know more about you...")
else:
    print("Not a valid name....Try again")

#####new user#####
def spydetails(spy_name,spy_age,spy_rating):
    menu = "What you want to do? \n 1.Add status \n 2. Quit"
    menu1 = int(input(menu))
    if (menu1==1):
        print("Status")
    else:
        print("Quit !!!")

spy_name = "Michael"
spy_salutation = "Mr."
spy_age = 20
spy_rating = 3.5

ques = "Do you want to continue as " + spy_salutation + " " + spy_name + "Y/N ?"
var = input(ques)

if var == "Y":
    spydetails(spy_name, spy_age, spy_rating)
else:
    spy_name = input("Welcome!!! you must tell your spy name first.")
    if len(spy_name) > 0:
        spy_name = input("What is your name?")
        spy_salutation = input("What should we call you (Mister or Misses)?")
        print("Welcome" + " " + spy_salutation + " " + spy_name + "to Acadview")
        spy_name = spy_salutation + " " + spy_name
        print(spy_name)
        print("Alright" + " " + spy_name + " " + " we would like to know more about you...")
    else:
        print("Not a valid name....Try again")

spy_age = int(input("Enter your age : "))
if spy_age > 12 and spy_age < 50:
    print("Valid spy.")
else:
    print("Not a valid spy")

spy_rating = float(input("Enter the spy rating : "))
if spy_rating > 4.5:
    print("Great ace...")
elif spy_rating > 3.5 and spy_rating <= 4.5:
    print("You are one of the good ones...")
elif spy_rating >= 2.5 and spy_rating <= 3.5:
    print("You can do better....")
else:
    print("We can always use somebody to help in the office....")

spy_is_online = True
print("Authentication complete.... Welcome " + str(spy_name) + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " proud to have you onboard")



