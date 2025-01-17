"""
6.  Create a dictionary to store your friends' names and birthday.
    WAP using 3 func which takes the dict as argument and implements
    the following: 
        - Display birthday of a particular person
        - Add/modify a friend's birthday
        - Delete the data of a friend
        - Exit
"""

def Display(d): # d is the dictionary
    n = input("Name of person: ")
    
    if n in d: # check if name exists in dictionary
        print(d[n], "is the birthday of", n)
    
def Modify(d):
    n = input("Name whose birthday to be changed: ")
    b = input("Birthday")
    d[n] = b
    
    print(d)

def Delete(d):
    n = input("Name whose birthday is to be deleted: ")
    if n in d:
        del d[n]

    print(d)

# Main Program
d = {}
n = int(input("Enter limit: "))

for i in range(n):
    n = input("Name: ")
    b = input("Birthday: ")

    d[n] = b

while True:
    print("1. Display birthday")
    print("2. Add/Modify birthday")
    print("3. Delete person")
    print("4. Exit")

    ch = int(input("Choice: "))
    if ch == 1:
        Display(d)
    elif ch == 2:
        Modify(d)
    elif ch == 3:
        Delete(d)
    elif ch == 4:
        break
    else:
        print("Wrong input")