"""
5.  Write a program using function which takes a list as argument
    and swaps the adjacent elements
"""

# Function
def swap(l):
    print("Original list:", l)
    
    n = len(l)
    

    if n % 2 == 0:
        for i in range(0, n, 2):
            l[i], l[i+1] = l[i+1], l[i]

    else:
        for i in range(0, n-1, 2): 
            l[i], l[i+1] = l[i+1], l[i]   

    print("Swapped list:", l)

# Main program
n = int(input("Enter limit: "))
l = []
for i in range(n):
    e = input("Enter element: ")
    l.append(e)

swap(l)