# # Health Management System
# # Total 6 Files, 3 For exercise and 3 For for diet
# # 3 clients - Ansh, Pranav and Shlok
# # write a function that when executed takes as input client name
# # one more function to retrieve exercise or food for any client

import datetime
def gettime():
    return datetime.datetime.now()

#making a log function
def log (h):
    if h == 1:
        t = int(input("\t\t\tPLEASE SELECT IF YOU WANT TO LOG IN EXERCISE OR DIET\n SELECT 1 FOR EXERCISE\n SELECT 2 FOR DIET\n TYPE HERE:"))
        if t == 1:
            f = open("ansh exercise.txt","a")
            f.write(input("type here:"))
            print("your exercise is successfully added")
        elif t == 2:
            f = open("ansh diet.txt","a")
            f.write(input("type here:"))
            print("your diet is successfully added")  
    elif h == 2:
        t = int(input("\t\t\tPLEASE SELECT IF YOU WANT TO LOG IN EXERCISE OR DIET\n SELECT 1 FOR EXERCISE\n SELECT 2 FOR DIET\n TYPE HERE:"))
        if t == 1:
            f = open("shlok exercise.txt","a")
            f.write(input("type here:"))
            print("your exercise is successfully added")
        elif t == 2:
            f = open("shlok diet.txt","a")
            f.write(input("type here:"))
            print("your diet is successfully added")
    elif h == 3:
        t = int(input("\t\t\tPLEASE SELECT IF YOU WANT TO LOG IN EXERCISE OR DIET\n SELECT 1 FOR EXERCISE\n SELECT 2 FOR DIET\n TYPE HERE:"))
        if t == 1:
            f = open("pranav exercise.txt","a")
            f.write(input("type here:"))
            print("your exercise is successfully added")
        elif t == 2:
            f = open("pranav diet.txt","a")
            f.write(input("type here:"))
            print("your diet is successfully added")


# making a retrieve function
def retrieve (h):
    if h == 1:
        t = int(input("\t\t\tPLEASE SELECT IF YOU WANT TO RETRIEVE IN EXERCISE OR DIET\n SELECT 1 FOR EXERCISE\n SELECT 2 FOR DIET\n TYPE HERE:"))
        if t == 1:
            f = open("ansh exercise.txt","rt")
            f.read()
            print("your exercise is successfully reatrived")
        elif t == 2:
            f = open("ansh diet.txt","rt")
            
            print(f.read())  
    elif h == 2:
        t = int(input("\t\t\tPLEASE SELECT IF YOU WANT TO LOG IN EXERCISE OR DIET\n SELECT 1 FOR EXERCISE\n SELECT 2 FOR DIET\n TYPE HERE:"))
        if t == 1:
            f = open("shlok exercise.txt","rt")
            
            print(f.read())
        elif t == 2:
            f = open("shlok diet.txt","rt")
            
            print(f.read())
    elif h == 3:
        t = int(input("\t\t\tPLEASE SELECT IF YOU WANT TO LOG IN EXERCISE OR DIET\n SELECT 1 FOR EXERCISE\n SELECT 2 FOR DIET\n TYPE HERE:"))
        if t == 1:
            f = open("pranav exercise.txt","rt")
            
            print(f.read())
        elif t == 2:
            f = open("pranav diet.txt","rt")
            
            print(f.read())                    
#welcome screem & log or retrieve
print("\t\t\tWELCOME TO GOLD'S GYM")
a=int(input("\t\t\tPLEASE SELECT IF YOU WANT TO LOG OR RETRIEVE\n PRESS 1 FOR LOG\n PRESS 2 FOR RETRIEVE\n TYPE HERE:"))

#selecting clint id
#for log
if a == 1:
    b = int(input("\t\t\tPLEASE SELECT YOUR CLIENT ID\n PRESS 1 FOR ANSH\n PRESS 2 FOR SHLOK\n PRESS 3 FOR PRANAV\n TYPE HERE:"))
    log(b)
#for retrieve    
elif a == 2:
    b = int(input("\t\t\tPLEASE SELECT YOUR CLIENT ID\n PRESS 1 FOR ANSH\n PRESS 2 FOR SHLOK\n PRESS 3 FOR PRANAV\n TYPE HERE:"))
    retrieve(b)