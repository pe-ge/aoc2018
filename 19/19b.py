class Machine:

    def __init__(self, ip_register):
        self.registers = [0, 0, 0, 0, 0, 0]
        self.ip_register = ip_register
        self.regs = {
            0: 'a',
            1: 'b',
            2: 'c',
            3: 'd',
            4: 'ip',
            5: 'f'
        }

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

    def to_str(self, opcode, params):
        regs = self.regs
        if opcode == 'addr':
            return '{out_reg} = {in_reg1} + {in_reg2}'.format(out_reg=regs[params[2]], in_reg1=regs[params[0]], in_reg2=regs[params[1]])
        elif opcode == 'addi':
            return '{out_reg} = {in_reg} + {val}'.format(out_reg=regs[params[2]], in_reg=regs[params[0]], val=params[1])
        elif opcode == 'mulr':
            return '{out_reg} = {in_reg1} * {in_reg2}'.format(out_reg=regs[params[2]], in_reg1=regs[params[0]], in_reg2=regs[params[1]])
        elif opcode == 'muli':
            return '{out_reg} = {in_reg} * {val}'.format(out_reg=regs[params[2]], in_reg=regs[params[0]], val=params[1])
        elif opcode == 'banr':
            return '{out_reg} = {in_reg1} & {in_reg2}'.format(out_reg=regs[params[2]], in_reg1=regs[params[0]], in_reg2=regs[params[1]])
        elif opcode == 'bani':
            return '{out_reg} = {in_reg} & {val}'.format(out_reg=regs[params[2]], in_reg=regs[params[0]], val=params[1])
        elif opcode == 'borr':
            return '{out_reg} = {in_reg1} | {in_reg2}'.format(out_reg=regs[params[2]], in_reg1=regs[params[0]], in_reg2=regs[params[1]])
        elif opcode == 'bori':
            return '{out_reg} = {in_reg} | {val}'.format(out_reg=regs[params[2]], in_reg=regs[params[0]], val=params[1])
        elif opcode == 'setr':
            return '{out_reg} = {in_reg}'.format(out_reg=regs[params[2]], in_reg=regs[params[0]])
        elif opcode == 'seti':
            return '{out_reg} = {val}'.format(out_reg=regs[params[2]], val=params[0])
        elif opcode == 'gtir':
            return '{out_reg} = {val} > {in_reg}'.format(out_reg=regs[params[2]], val=params[0], in_reg=regs[params[1]])
        elif opcode == 'gtri':
            return '{out_reg} = {in_reg} > {val}'.format(out_reg=regs[params[2]], in_reg=regs[params[0]], val=params[1])
        elif opcode == 'gtrr':
            return '{out_reg} = {in_reg1} > {in_reg2}'.format(out_reg=regs[params[2]], in_reg1=regs[params[0]], in_reg2=regs[params[1]])
        elif opcode == 'eqir':
            return '{out_reg} = {val} == {in_reg}'.format(out_reg=regs[params[2]], val=params[0], in_reg=regs[params[1]])
        elif opcode == 'eqri':
            return '{out_reg} = {in_reg} == {val}'.format(out_reg=regs[params[2]], in_reg=regs[params[0]], val=params[1])
        elif opcode == 'eqrr':
            return '{out_reg} = {in_reg1} == {in_reg2}'.format(out_reg=regs[params[2]], in_reg1=regs[params[0]], in_reg2=regs[params[1]])

        raise ValueError('should not be reached')


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
m.registers = [1, 0, 0, 0, 0, 0]

counter = 0
while True:
    if counter == 22:
        print("SETTING VALUE")
        # m.registers[2] = 10551264
        # m.registers[3] = 10551264
        # m.registers[1] = 10551264
    ip = m.get_ip()
    opcode, params = program[ip]
    print(['{reg} = {val}'.format(reg=m.regs[reg_idx], val=str(reg).zfill(5)) for reg_idx, reg in enumerate(m.registers)])
    m.execute(opcode, params)
    print(m.to_str(opcode, params))

    ip = m.inc_ip()
    if ip >= len(program):
        break

    counter += 1
    if counter > 35:
        raise ValueError("crash")
