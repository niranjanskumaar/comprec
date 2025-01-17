
"""
7.  WAP to read a text file line by line 
    and display each word separated by #
"""

# writing to the file
wf = open("./files/textfile1.txt", "w")

s = """This is a sentence
This is the second line of a sentence
Goodbye everyone see you later"""

wf.write(s)
wf.close()


# displaying file 
print("Contents of file")

rf = open("./files/textfile1.txt")

l = rf.readlines()

for i in l:
    print(i)

rf.close()


# displaying each word sep by #
print("Each word sep by #")

f = open("./files/textfile1.txt")
t = f.read()
t = t.replace(" ", "#") # replaces all space with '#'

print(t)
f.close()

