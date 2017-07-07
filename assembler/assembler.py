#!/usr/bin/python3


#Constants
opcodeTable = {
        'NOP':[00000,0],
        'HLT':[1000,0],
        'RST':[2000,0],
        'CLR':[3000,0],
        'MOV':[4000,2],
        'ADD':[5000,2],
        'SUB':[6000,2],
        'MUl':[7000,2],
        'NEG':[8000,1],
        'NOT':[9000,1],
        'JMP':[4050,1],
        'JCD':[10000,1],
        'PSH':[11000,1],
        'POP':[12000,1],
        'CAL':[13000,1],
        'RET':[14000,0],
        'SWT':[15000,1],
        'PRT':[16000,0],
        'PRC':[17000,1],
        'CLS':[18000,0],
        'INP':[19000,1],
        'KPD':[20000,0],
        }

registerTable = {
        'NULL':0,
        'A':1,
        'B':2,
        'C':3,
        'D':4,
        'IP':5,
        'SP':6,
        'MP':7,
        'MA':8
        }

argumentMultipliers = [100,10,1]

def assembleEXEinstruction(instruction):
    #Parse the isntruction
    parts = instruction.split(' ')
    ASM = parts[0]
    args = parts[1::]
    del(parts)

    #Validate amount of arguments
    if opcodeTable[ASM][1] != len(args):
        #TODO, fill out this error message
        print('Invalid Arguments')
    opcode = opcodeTable[ASM][0]
    if ASM == 'SWT':
        return [opcode,args[0]]
    for i in range(len(args)):
        argCode = registerTable[args[i]]
        argCode *= argumentMultipliers[i]
        opcode += argCode
    return opcode

def assembleDMAinstruction(instruction):
    #Parse
    parts = instruction.split(':')
    return parts



#Source is a list of ASM statements
#Retuns a list of opcodes, or None on error
def assemble(source):
    opcodes = []
    mode = 'exe'
    dmaCounter = 0
    for instruction in source:
        if(mode=='exe'):
            result = assembleEXEinstruction(instruction)
            #Check for mode switch
            if type(result)==list:
                opcodes.append(result[0])
                opcodes.append(result[1])
                mode = 'dma'
                dmaCounter = int(result[1])
            else:
                opcodes.append(result)

            
        elif(mode=='dma'):
            vals = assembleDMAinstruction(instruction)
            opcodes.append(vals[0])
            opcodes.append(vals[1])
            dmaCounter -= 1
            if(dmaCounter==0):
                mode = 'exe'

            
    return opcodes







if __name__ == '__main__':
    with open('asm.asm') as source:
        bin = assemble(source.read().splitlines())
    print('Done!')
    for line in bin:
        print(line)
        
        



