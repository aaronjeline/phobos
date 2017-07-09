import threading

#Register constants
A = 1
B = 2
C = 3
D = 4
IP = 5
SP = 6
MP = 7
MA = 8


#Execute the comparsion from JCD
def compare(value, comparison)
    if(comparison==0):
        return value > 0
    elif(comparison==1):
        return value < 0
    elif(comparison==2):
        return value == 0
    elif(comparison==3):
        return value != 0




class phobos (threading.Thread):
    def __init__(self, memSize):
        #Bind register table
        self.registers = {
                '0':0,
                '1':0,
                '2':0,
                '3':0,
                '4':0,
                '5':0,
                '6':memSize-1,
                '7':0,
                '8':0,
        }
        #Create system memory
        self.memory = [0] * memSize
        #Create status lights
        self.isHalted = True
        self.exe = True
        self.keypad = 0
        self.display = 0
        self.romtape = None
        self.dmaCounter = 0

    def executeEXEopcode(self, opcode):
        #First, find the instruction code
        st = str(opcode)
        if(len(opcode)==4):
            instructionCode = int(opcode[0])
        else:
            instructionCode = int(opcode[0:1])

        #Instruction switch
        if(instructionCode==0):
            #NOP
            self.registers[IP] += 1
        elif(instructionCode==1):
            #HALT
            self.registers[IP] += 1
            self.isHalted = True
        elif(instructionCode==2):
            #Reset
            for register in self.registers:
                register = 0
            self.registers[SP] = len(self.memory) - 1
        elif(instructionCode==3):
            #Clear memory
            length = len(self.memory)
            self.memory = [0] * length
            self.registers[IP] += 1
        elif(instructionCode==4):
            #MOV A B
            a = int(st[1])
            b = int(st[2])
            self.registers[b] = self.registers[a]
            self.registers[IP] += 1
        elif(instructionCode==5):
            #Add A B, store in ACC
            a = self.registers[int(st[1])]
            b = self.registers[int(st[2])]
            self.registers[A] = a + b
            self.registers[IP] += 1
        elif(instructionCode==6):
            #Subtract
            a = self.registers[int(st[1])]
            b = self.registers[int(st[2])]
            self.registers[A] = a - b
            self.registers[IP] += 1
        elif(instructionCode==7):
            #Multiply
            a = self.registers[int(st[1])]
            b = self.registers[int(st[2])]
            self.registers[A] = a * b
            self.registers[IP] += 1
        elif(instructionCode==8):
            #Arithmatic Negation
            a = self.registers[int(st[1])]
            self.registers[A] = -a
            self.registers[IP] += 1
        elif(instructionCode==9):
            #Boolean Negation
            a = self.registers[int(st[1])]
            if a == 0:
                a = 1
            else:
                a = 0
            self.registers[IP] += 1
        elif(instructionCode==10):
            #Conditional Jump
            #Parse arguments
            toCompare = st[2]
            comparison = st[3]
            address = st[4]
            if compare(toCompare,comparison):
                self.registers[IP] = address
            else:
                self.registers[IP] += 1
        elif(instructionCode==11):
            #Push to the stack
            a = self.registers[int(st[2])]
            self.memory[self.registers[SP]] = a
            self.registers[SP] -= 1
            self.registers[IP] += 1
        elif(instructionCode==12):
            #Pop value off stack
            value = self.memory[self.registers[SP]]
            self.registers[SP] += 1
            self.registers[int(st[2])] = value
            self.registers[IP] += 1
        elif(instructionCode==13):
            #Call
            #Save IP + 1 onto the stack, then jump
            destination = int(st[2])
            self.memory[self.registers[SP]] = self.registers[IP] + 1
            self.registers[SP] -= 1
            self.registers[IP] = destination








        
    def run(self):
        if(not self.isHalted):
            if self.exe:
                self.executeEXEopcode(self.romtape[self.registers[IP]])
            else:
                self.dmaCounter -= 1
                address = self.romtape[self.registers[IP]]
                self.registers[IP] += 1
                value = self.romtape[self.registers[IP]]
                self.registers[IP] += 1
                self.memory[address] = value


                



