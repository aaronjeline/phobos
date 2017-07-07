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


                



