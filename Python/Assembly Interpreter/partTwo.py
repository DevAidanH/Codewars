code = [
"mov a 5",
"inc a",
"dec a",
"dec a",
"div a 2",
"inc a"]

class assemblyInterpreter:
    def __init__(self):
        self.registers = {}
        self.pc = 0
        self.instructions = {
            "mov": self._move,
            "inc": self._increment,
            "dec": self._decrement,
            "jnz": self._jumpNotZero,
            "add": self._add,
            "sub": self._sub,
            "mul": self._mul,
            "div": self._div
        }

    def resolve(self,y):
         return self.registers[y] if y in self.registers else int(y)

    def _move(self, x, y):
        self.registers[x] = self.resolve(y)
    
    def _increment(self, x):
        self.registers[x] += 1
    
    def _decrement(self, x):
        self.registers[x] -= 1

    def _add(self, x, y):
        self.registers[x] = self.registers[x] + self.resolve(y)

    def _sub(self, x, y):
        self.registers[x] = self.registers[x] - self.resolve(y)

    def _mul(self, x, y):
        self.registers[x] = self.registers[x] * self.resolve(y)

    def _div(self, x, y):
        self.registers[x] = self.registers[x] / self.resolve(y)
    
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