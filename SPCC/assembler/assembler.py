pot, pot_found = ['START', 'END', 'EQU', 'LTORG', 'ORIGIN'], []
mot, mot_found = ['MOVER', 'MOVEM', 'ADD', 'SUB', 'MUL', 'DIV', 'BC', 'COMP', 'READ', 'PRINT'], []
dl = ['DS', 'DC']
reg, reg_found = ['AREG', 'BREG', 'CREG', 'DREG'], []
literals, symbols = [], []

contents = ''
with open('input.txt', 'r') as fd:
	contents = fd.read()
contents = contents.split('\n')

for line in contents:
	token = ''
	for i in range(len(line)):
		temp = line[i]
		if temp in [':', ',', ';', '=', ' ']:
			if temp == ':':
				symbols.append(token)
				token = ''
			elif temp == '=':
				literals.append(line[i + 2: -1])
			elif temp == ' ' or temp == ',':
				token = token.strip()
				if token in pot:
					pot_found.append(token)
				elif token in mot:
					mot_found.append(token)
				elif token in reg:
					reg_found.append(token)
				token = ''
		else:
			token += temp
			if i == len(line) - 1:
				if len(token) == 1 and token >= 'A' and token <= 'Z':
					symbols.append(token)
					token = ''
				elif len(token) > 1:
					token = token.strip()
					if token in pot:
						pot_found.append(token)

print('POT: {}'.format(pot_found))
print('MOT: {}'.format(mot_found))
print('REG: {}'.format(reg_found))
print('LITERALS: {}'.format(literals))
print('SYMBOLS: {}'.format(symbols))

with open('pot.txt', 'w') as fd:
	fd.write('\n'.join(pot_found))
with open('mot.txt', 'w') as fd:
	fd.write('\n'.join(mot_found))
with open('reg.txt', 'w') as fd:
	fd.write('\n'.join(reg_found))
with open('literals.txt', 'w') as fd:
	fd.write('\n'.join(literals))
with open('symbols.txt', 'w') as fd:
	fd.write('\n'.join(symbols))

print('Files Created')
