
"""
12. Create a binary file with book name, book number.
    Display name of the book. 
    If not found, display appropriate message
"""

import pickle

# creating
def create():
    wf = open("./files/books.dat", "wb")

    n = int(input("Enter number of books: "))

    for i in range(n):
        bno = int(input("Enter book no: "))
        bname = input("Enter book name: ")

        d = [bno, bname]
        pickle.dump(d, wf)

    wf.close()

# displaying
def display():
    rf = open("./files/books.dat", "rb")
    
    try:
        while True:
            d = pickle.load(rf)
            print(d[0], d[1], sep="\t")
    except EOFError:
        rf.close()

# searching
def search():
    rf = open("./files/books.dat", "rb")
    bno = int(input("Enter book number to search: "))
    found = False
    try:
        while True:
            d = pickle.load(rf)
            if d[0] == bno:
                print(d[1])
                found = True
    except EOFError:
        if not found:
            print("Could not find the book.")
            rf.close()


create()
display()
search()
    