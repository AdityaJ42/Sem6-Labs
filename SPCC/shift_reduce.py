# Shift Reduce Parser

rules, stack = {}, '$'
prod = input('Enter the production rule: ').split('->')
lhs = prod[0]
rules[lhs] = prod[1].split('|')
ip = input('Enter the string to be parsed: ') + '$'

print('Stack\tInput\tAction')
print('{}\t{}\tInitial'.format(stack, ip))
while len(ip) != 1 or stack != '$' + lhs:
	temp = ''
	for i in rules:
		for j in rules[i]:
			if j in stack:
				temp = j
				break
	if temp:
		stack = stack.replace(temp, lhs)
		print('{}\t{}\tReduce  {} -> {}'.format(stack, ip, lhs, temp))
	else:
		if ip == '$':
			break
		stack += ip[0]
		ip = ip[1:]
		print('{}\t{}\tShift'.format(stack, ip))

if ip == '$' and stack == '$' + lhs:
	print('String is accepted')
else:
	print('String is rejected')
