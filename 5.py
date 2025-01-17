
"""
5.  Write a program using function which takes a list as argument
    and swaps the adjacent elements
"""

# Function
def swap(l):
    print("Original list:", l)
    
    n = len(l)

    if n % 2 == 0: # if there are even no of elements,
        for i in range(0, n, 2):
            l[i], l[i+1] = l[i+1], l[i] # swap every two elements (a, b, c, d) => (b, a, d, c)

    else:
        for i in range(0, n-1, 2):  # if there are odd no of elements
            l[i], l[i+1] = l[i+1], l[i]  # swap every two elements, ignoring the last element (n-1)

    print("Swapped list:", l)

# Main program
n = int(input("Enter limit: "))
l = []

for i in range(n):
    e = input("Enter element: ")
    l.append(e)

swap(l)