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
            idx += 1


m = Machine()
sample_count = 0
for sample in samples:
    before = sample['B']
    params = sample['P']
    after = sample['A']

    inst_count = 0
    for inst in m.instructions:
        result = inst(before, params)
        if result == after:
            inst_count += 1

    if inst_count >= 3:
        sample_count += 1

print(sample_count)
