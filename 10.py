"""
10. Create a text file, Display contents. 
    Read lines from a text file, display no of words
    less than 4 characters.
"""

# creating a file

wf = open("./files/textfile4.txt", "w")
t = input("Enter text: ")

wf.write(t)
wf.close()


# displaying the file

rf = open("./files/textfile4.txt")
content = rf.read()

print("File contents..\n")
print(content)

rf.close()


# reading and displaying no of words less than 4 characters

rf = open("./files/textfile4.txt")
text = rf.read()

words = text.split()
n = 0

for w in words:
    if len(w) < 4:
        n += 1

print("No. of words with less than 4 characters:", n)
