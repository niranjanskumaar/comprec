

"""
Menu driven program to accept a line of text and,
    1. Print pallindromic words
    2. Display longest word
"""

def pal(words): # this function prints all the 
                # palindromic words from the list of words we give to it
    print("Pallindromic words:")
    for w in words:
        if w[::-1] == w:
            print(w) # palindromic word

def longest(words): # this function prints the 
                    # longest word from the list of words we give to it
    
    biggest = 0     # biggest wordinte length store cheyyan ulla variable
    biggest_word = ""  # biggest word entha enn store cheyyannn 

    for w in words:
        if len(w) > biggest:  # ee word nammal ithvare biggest enn paranj vecha wordine kateem length undoooo?
            
            biggest = len(w)  # omg, nammal nerathe biggest enn vichariche wordine kaal length und!
                              # so nammalk ee IPPOTHE WORDinte length aanu BIGGEST enn parayam!
            
            biggest_word = w  # OK, IPPOTHE WORD AANU ITHVARE KANDELE BIGGEST WORD!

    print(biggest_word)

    
# main program

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
    else:
        break