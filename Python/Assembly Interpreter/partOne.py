code = [
"mov a 5",
"inc a",
"dec a",
"dec a",
"jnz a -1",
"inc a"]

class assemblyInterpreter:
    def __init__(self):
        self.registers = {}
        self.pc = 0
        self.instructions = {
            "mov": self._move,
            "inc": self._increment,
            "dec": self._decrement,
            "jnz": self._jumpNotZero
        }

    def resolve(self,y):
         return self.registers[y] if y in self.registers else int(y)

    #mov x y - copies y (either a constant value or the content of a register) into register x
    def _move(self, x, y):
        self.registers[x] = self.resolve(y)
    
    #inc x - increases the content of the register x by one
    def _increment(self, x):
        self.registers[x] += 1
    
    #dec x - decreases the content of the register x by one
    def _decrement(self, x):
        self.registers[x] -= 1
    
    #jumps to an instruction y steps away (positive means forward, negative means backward, y can be a register or a constant), but only if x (a constant or a register) is not zero
    def _jumpNotZero(self, x, y):
        if(self.resolve(x) != 0):
            self.pc += self.resolve(y) - 1 

    #execute program
    def execute(self, program):
        while self.pc < len(program):
            parsed = program[self.pc].split()
            currentInstruction = parsed[0]
            args = parsed[1:]
            self.instructions[currentInstruction](*args)

            self.pc += 1
        return self.registers




def simple_assembler(program):
	return assemblyInterpreter().execute(program)

print(simple_assembler(code))