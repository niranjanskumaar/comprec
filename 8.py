
"""
8.  Create a text file, Display contents
    Remove all lines containing 'a' and write it to another file.
    Display the new file
"""

# writing to file
wf = open("./files/textfile2.txt", "w")

s = "This is a text file.\nThis is the second line.\nThis line contains a.\nThis line does not."
wf.write(str)
wf.close()

# displaying the file
print("Displaying the contents of the file..\n")

rf = open("./files/textfile2,txt")
lines = rf.readlines()

for l in lines:
    print(l)
rf.close()

# creating new file
nwf = open("./files/newtextfile2.txt", "a")
rf = open("./files/textfile2.txt")

lines = rf.readlines()

for i in lines:
    if 'a' not in i:
        nwf.write(i)

nwf.close()
rf.close()

# displaying new file

print("\nDisplaying new file contents..\n")
nrf = open("./files/newtextfile2.txt")

text = nrf.read()
print(text)

nrf.close()