# Code Generation
import re
reg, output = {}, []


def allocate_register(op):
	if op in reg.values():
		for key, value in reg.items():
			if value == op:
				return key
	name = 'R{}'.format(len(reg))
	reg[name] = op
	output.append('MOV {}, {}'.format(name, op))
	return name

with open('input.txt', 'r') as fd:
	contents = fd.read().split('\n')
input_code = [i.strip() for i in contents]

for line in input_code:
	line = re.split('([\+\-\*\/\=])', line)
	lhs, eq, op1, op, op2 = line

	reg1, reg2 = allocate_register(op1), allocate_register(op2)
	if op.strip() == '+':
		op_line = 'ADD {}, {}'.format(reg1, reg2)
	if op.strip() == '-':
		op_line = 'SUB {}, {}'.format(reg1, reg2)
	if op.strip() == '*':
		op_line = 'MUL {}, {}'.format(reg1, reg2)
	if op.strip() == '/':
		op_line = 'DIV {}, {}'.format(reg1, reg2)
	reg[reg2] = lhs

	output.append(op_line)

for line in output:
	print(line)
