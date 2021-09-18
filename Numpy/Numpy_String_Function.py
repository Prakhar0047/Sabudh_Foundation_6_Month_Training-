import numpy as np

# Character multiplication and concatination

print(np.char.add(["Hello ","How are "],["Prakhar","you?"]))
print(np.char.multiply("Hello ",3))

# Centre and filling
print(np.char.center("Hello",20,fillchar="-"))

# Difference between Capatalize and Title is Title Capatalize every word's first char
# where as Capatalize does the same for just 1st char of string.

# np.char.lower turns everything to lower Similarly Upper.
# Splitter A.K.A Tokenization.
print(np.char.split('Are you coming?'))

# To Split lines
print(np.char.splitlines('Are \n you coming?'))

# Strip to remove certain Leadind and trailing char
print(np.char.strip('Are you coming?','?'))
print(np.char.strip(['Anita','Admin','aniata'],'a'))
# Usually used to remove spaces.

# Join
print(np.char.join([':','/'],['dmy','ymd']))

# Replace
print(np.char.replace('is a good dancer','is','was'))
