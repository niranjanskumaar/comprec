#4 

"""
Def a func that takes an int as argument.
Returns 0 if num is prime, 1 if not prime.
Write program to copy numbers of a list to a new list
"""

def prime(x):
    p = 1
    
    if x != 1:
        for j  in range(2, x): # j can be any number from 2 to x
            if x % j == 0: # if x can be divided by j
                p = 0 # then set prime to 0
    
    return p

n = int(input("Enter no of elements: : "))

l = []
pl = [] # prime nos list

for i in range(n):
    no = int(input("Enter number: "))
    l.append(no)

# now, aa listile prime nos ellam koodi 'pl' listilott idam
for i in l:
    p = prime(i)
    if p == 0:
        pl.append(i)

print("Prime nos are: ")
print(pl)