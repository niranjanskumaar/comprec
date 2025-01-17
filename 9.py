"""
9.  Create a text file. Read the text file, display no of:
    vowels, consonants, uppercase, lowercase characters.
"""

# creating file

wf = open("./files/textfile3.txt", "w")
text = input("Enter text: ")

wf.write(text)
wf.close()

# display the text file

rf = open("./files/textfile3.txt")

print("Contents of the file..\n")

content = rf.read()
print(content)

vow = 0
con = 0
up = 0
low = 0

for c in content:
    if c in 'aeiouAEIOU':
        vow += 1
    elif c.isalpha():
        con += 1

    if c.isupper():
        up += 1
    elif c.islower():
        low += 1

print("Vowel count:", vow)
print("Consonant count:", con)
print("Uppercase count:", up)
print("Lowercase count:", low)

rf.close()