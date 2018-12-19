class Machine:

    def __init__(self, ip_register):
        self.registers = [0, 0, 0, 0, 0, 0]
        self.ip_register = ip_register

    def inc_ip(self):
        self.registers[self.ip_register] += 1
        return self.registers[self.ip_register]

    def get_ip(self):
        return self.registers[self.ip_register]

    def addr(self, params):
        self.registers[params[2]] = self.registers[params[0]] + self.registers[params[1]]

    def addi(self, params):
        self.registers[params[2]] = self.registers[params[0]] + params[1]

    def mulr(self, params):
        self.registers[params[2]] = self.registers[params[0]] * self.registers[params[1]]

    def muli(self, params):
        self.registers[params[2]] = self.registers[params[0]] * params[1]

    def banr(self, params):
        self.registers[params[2]] = self.registers[params[0]] & self.registers[params[1]]

    def bani(self, params):
        self.registers[params[2]] = self.registers[params[0]] & params[1]

    def borr(self, params):
        self.registers[params[2]] = self.registers[params[0]] | self.registers[params[1]]

    def bori(self, params):
        self.registers[params[2]] = self.registers[params[0]] | params[1]

    def setr(self, params):
        self.registers[params[2]] = self.registers[params[0]]

    def seti(self, params):
        self.registers[params[2]] = params[0]

    def gtir(self, params):
        self.registers[params[2]] = 1 if params[0] > self.registers[params[1]] else 0

    def gtri(self, params):
        self.registers[params[2]] = 1 if self.registers[params[0]] > params[1] else 0

    def gtrr(self, params):
        self.registers[params[2]] = 1 if self.registers[params[0]] > self.registers[params[1]] else 0

    def eqir(self, params):
        self.registers[params[2]] = 1 if params[0] == self.registers[params[1]] else 0

    def eqri(self, params):
        self.registers[params[2]] = 1 if self.registers[params[0]] == params[1] else 0

    def eqrr(self, params):
        self.registers[params[2]] = 1 if self.registers[params[0]] == self.registers[params[1]] else 0

    def execute(self, func_name, params):
        func = getattr(self, func_name)
        func(params)


program = []
# with open('19e.txt') as f:
with open('19.txt') as f:
    ip_register = int(f.readline().split()[1])

    instructions = f.read().split('\n')
    for inst in instructions:
        if not inst:
            continue

        inst_splitted = inst.split()
        opcode = inst_splitted[0]
        params = list(map(int, inst_splitted[1:]))

        program.append([opcode, params])

m = Machine(ip_register)

while True:
    ip = m.get_ip()
    opcode, params = program[ip]
    m.execute(opcode, params)

    ip = m.inc_ip()
    if ip >= len(program):
        break

print(m.registers[0])
