file_in = open("memory.txt", "r")
file_out = open("memory.dat" , "w")

commands = {}
labels = {}

data = file_in.read()
definitions = [ sublist.strip().split() for sublist in data.splitlines() ]

for i in definitions:
    pass
for i in range (0, definitions):
    NextHexCode = ""
    if i == "/*":
        while i != "*/":
            i+= 1
    if i == "jump":
        pass
        #