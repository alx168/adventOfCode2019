f = open("input.txt")
memory = f.readline().strip().split(",")
memory = list(map(int, memory))
originalMemory = memory
target = 19690720

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

def crack(memory, target):
    for noun in range(0,100):
        for verb in range(0,100):
            newMem = [memory[0], noun, verb]
            newMem += memory[3:]
            newMem = runInstr(newMem)
            if newMem[0] == target:
                print(newMem)

crack(memory, target) 
            
