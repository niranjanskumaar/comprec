
"""
3.  Menu driven program to accept a line of text and:
        1. Print pallindromic words
        2. Display longest word
"""

def pal(words):
    print("Pallindromic words:")
    for w in words:
        if w[::-1] == w:
            print(w) 

def longest(words): 
    biggest = 0
    biggest_word = ""  

    for w in words:
        if len(w) > biggest:          
            biggest = len(w)
            biggest_word = w

    print(biggest_word)


# Main program

s = input("Text: ")
words = s.split()

while True:
    print("1. Pallindromic words")
    print("2. Longest word")
    print("3. Exit")

    choice = int(input("Choice: "))

    if choice == 1:
        pal(words)
    elif choice == 2:
        longest(words)
    elif choice == 3:
        break
    else:
        print("Invalid Option")