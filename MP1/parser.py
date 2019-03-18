file_in = open("memory.txt", "r")
file_out = open("memory.dat" , "w")

commands = {}
commands["lw"] = ("1001", 5, 5, 16)
commands["sw"] = ("1010", 5, 5, 16)
commands["sub"] = ("0011", 5, 5, 5)
labels = []

data = file_in.read()
definitions = [ sublist.strip().split() for sublist in data.splitlines() ]
#use partition
def translate(definitions):
    translated = []
    for i in definitions:
        pass
    for j in range(0, len(definitions)):
        for i in range (0, len(definitions)):
            NextHexCode = ""
            if definitions[j][i] =="//":
                j += 1
                continue
            if definitions[j][i] == "jump":
                labels.append(definitions[j][i + 1])
            if definitions[j][i] ==";":
                translated.append("\n")
            if i == 0:
                translated.append(commands[definitions[j][i]][0])
    print(translated)
  

translate(definitions) 
file_in.close()
file_out.close()      