f = open("input.txt")
memory = f.readline().strip().split(",")
memory = list(map(int, memory))

def runInstr(memory):
    i = 0
    while True:
        if memory[i] == 99:
            return memory 
        instr = memory[i]
        addr1 = memory[i+1]        
        addr2 = memory[i+2]        
        store = memory[i+3]
        if instr == 1:
            memory[store] = memory[addr1] + memory[addr2]
        elif instr  == 2:
            memory[store] = memory[addr1] * memory[addr2]
        else:
            print("unknown opcode")
        
        i += 4

print(runInstr(memory))
