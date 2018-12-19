from collections import defaultdict
from pprint import pprint
class Machine:

    def __init__(self):
        self.instructions = [
            self.addr,
            self.addi,
            self.mulr,
            self.muli,
            self.banr,
            self.bani,
            self.borr,
            self.bori,
            self.setr,
            self.seti,
            self.gtir,
            self.gtri,
            self.gtrr,
            self.eqir,
            self.eqri,
            self.eqrr
        ]

        self.opcodes = defaultdict(list)

    def addr(self, registers, params):
        result = registers[:]
        result[params[3]] = result[params[1]] + result[params[2]]
        return result

    def addi(self, registers, params):
        result = registers[:]
        result[params[3]] = result[params[1]] + params[2]
        return result

    def mulr(self, registers, params):
        result = registers[:]
        result[params[3]] = result[params[1]] * result[params[2]]
        return result

    def muli(self, registers, params):
        result = registers[:]
        result[params[3]] = result[params[1]] * params[2]
        return result

    def banr(self, registers, params):
        result = registers[:]
        result[params[3]] = result[params[1]] & result[params[2]]
        return result

    def bani(self, registers, params):
        result = registers[:]
        result[params[3]] = result[params[1]] & params[2]
        return result

    def borr(self, registers, params):
        result = registers[:]
        result[params[3]] = result[params[1]] | result[params[2]]
        return result

    def bori(self, registers, params):
        result = registers[:]
        result[params[3]] = result[params[1]] | params[2]
        return result

    def setr(self, registers, params):
        result = registers[:]
        result[params[3]] = result[params[1]]
        return result

    def seti(self, registers, params):
        result = registers[:]
        result[params[3]] = params[1]
        return result

    def gtir(self, registers, params):
        result = registers[:]
        result[params[3]] = 1 if params[1] > result[params[2]] else 0
        return result

    def gtri(self, registers, params):
        result = registers[:]
        result[params[3]] = 1 if result[params[1]] > params[2] else 0
        return result

    def gtrr(self, registers, params):
        result = registers[:]
        result[params[3]] = 1 if result[params[1]] > result[params[2]] else 0
        return result

    def eqir(self, registers, params):
        result = registers[:]
        result[params[3]] = 1 if params[1] == result[params[2]] else 0
        return result

    def eqri(self, registers, params):
        result = registers[:]
        result[params[3]] = 1 if result[params[1]] == params[2] else 0
        return result

    def eqrr(self, registers, params):
        result = registers[:]
        result[params[3]] = 1 if result[params[1]] == result[params[2]] else 0
        return result


samples = []
program = []
# with open('16-example.txt') as f:
with open('16.txt') as f:
    lines = f.read().split('\n')

    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if line[:6] == 'Before':
            before = list(map(int, line[9:-1].split(', ')))
            params = list(map(int, lines[idx+1].split(' ')))
            after = list(map(int, lines[idx+2][9:-1].split(', ')))
            # print(after)

            idx += 4
            samples.append({'B': before, 'P': params, 'A': after})
        else:
            if lines[idx] == '':
                idx += 1
                continue
            program.append(list(map(int, lines[idx].split(' '))))
            idx += 1


m = Machine()
for sample in samples:
    before = sample['B']
    params = sample['P']
    after = sample['A']

    opcode = params[0]
    if m.opcodes[opcode] == []:  # if no known functions for given opcode
        for inst in m.instructions:
            result = inst(before, params)
            if result == after:
                m.opcodes[opcode].append(inst.__name__)
    else:
        for inst_name in m.opcodes[opcode]:
            inst = getattr(m, inst_name)
            result = inst(before, params)
            if result != after:
                m.opcodes[opcode].remove(inst_name)


# remove duplicates
removed = set()
while len(removed) != 16:
    # find opcode with single mapped instruction
    for opcode, instructions in m.opcodes.items():
        if len(instructions) == 1 and opcode not in removed:
            # remove instruction from other opcodes
            for opcode2, instructions2 in m.opcodes.items():
                if opcode != opcode2 and instructions[0] in instructions2:
                    instructions2.remove(instructions[0])

            removed.add(opcode)

pprint(m.opcodes)
# execute program
registers = [0, 0, 0, 0]
for params in program:
    inst_name = m.opcodes[params[0]][0]
    inst = getattr(m, inst_name)
    registers = inst(registers, params)

print(registers)
