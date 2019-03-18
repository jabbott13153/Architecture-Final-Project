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
    #store the translated commands as lists of strings
    translated = []
    #allocate memory sizes
    #insert the variable into a dictionary that stores the assigned memory address of the variable
    #compute memory location
    for i in definitions:
        pass
    #
    for j in range(0, len(definitions)):
        for i in range (0, len(definitions)):
            NextHexCode = ""
            #strip comments from the code
            if definitions[j][i] =="//":
                j += 1
                continue
            #store jump location, put it on the stack as next
            if definitions[j][i] == "jump":
                labels.append(definitions[j][i + 1])
            #if it ends with a semicolon, it's a new line
            if definitions[j][i] ==";":
                translated.append("\n")
            #only the first item in each list will be an instruction, so only pull that and translate it
            if i == 0:
                translated.append(commands[definitions[j][i]][0])
    
    print(translated)
  

translate(definitions) 
file_in.close()
file_out.close()      