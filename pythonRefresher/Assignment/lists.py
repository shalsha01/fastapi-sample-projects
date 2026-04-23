"""- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals"""


anmals = ['lion', 'tiger', 'elephant', 'giraffe', 'zebra']
anmals.pop(3)

anmals.append('monkey')
del anmals[0]
print("All animals in the zoo:", anmals)
print("First three animals in the Zoo:", anmals[:3])
