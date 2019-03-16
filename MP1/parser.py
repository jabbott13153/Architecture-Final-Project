file_in = open("memory.txt", "r")
file_out = open("memory.dat" , "w")

commands = {"lw" : 0x04, "sw" : 0x03, "sub": 0x02, "jump": 0x01, "HALT_AND_CATCH_FIRE": 0x20}
labels = {}

data = file_in.read()
definitions = [ sublist.strip().split() for sublist in data.splitlines() ]

def translate(definitions):
    for i in definitions:
        pass
    for i in range (0, definitions):
        NextHexCode = ""
        if i == "/*":
            while i != "*/":
                i+= 1
        if i == "jump":
            pass
  
  
file_in.close()
file_out.close()      