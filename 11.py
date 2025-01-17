# create binary file to store details of n employees in a binary file and display it on the screen

import pickle

def create():
    wf = open("./files/employ.dat", "wb")
    n = int(input("n: "))
    for i in range(n):
        eno = int(input("Emp no: "))
        ename = input("Emp name: ")
        salary = int(input("Salary: "))

        l = [eno, ename, salary]
        pickle.dump(l)

    wf.close()

def display():
    rf = open("./files/employ.dat", "rb")
    try:
        while True:
            l = pickle.load(rf) # load the file line by line
            print(l[0], l[1], l[2])

    except EOFError:
        print("End of file")
        rf.close()

create()
display()