rules = {}
stack = '$'

prod = input('Enter the production rules: ').split('->')
rules[prod[0]] = prod[1].split('|')
lhs = [k for k in rules.keys()]
lhs = ''.join(lhs)
ip = input('Enter string to be parsed: ') + '$'

print('Stack\t\tInput\t\tAction')
while len(ip) != 1 or stack != ('$' + lhs):
	if len(stack) == 1 and len(ip) != 1:
		stack += ip[0]
		ip = ip[1:]
		print('{}\t\t{}\t\t{}'.format(stack, ip, 'Shift'))
	temp = ''
	for i in rules.keys():
		for j in rules[i]:
			if j in stack:
				temp = j
				break
	if temp:
		stack = stack.replace(temp, lhs)
		print('{}\t\t{}\t\t{}  {}->{}'.format(stack, ip, 'Reduce', lhs, temp))
	else:
		if ip[0] == '$':
			break
		stack += ip[0]
		ip = ip[1:]
		print('{}\t\t{}\t\t{}'.format(stack, ip, 'Shift'))

if stack == '$' + lhs and ip == '$':
	print('String is accepted')
else:
	print('String is rejected')

"""aditya@aditya-HP-Pavilion-Notebook:~/Desktop/College/Codes/SPCC$ python shift_reduce.py
Enter the production rules: E->E+E|E*E|i
Enter string to be parsed: i+i*i
Stack		Input		Action
$i		+i*i$		Shift
$E		+i*i$		Reduce  E->i
$E+		i*i$		Shift
$E+i		*i$		Shift
$E+E		*i$		Reduce  E->i
$E		*i$		Reduce  E->E+E
$E*		i$		Shift
$E*i		$		Shift
$E*E		$		Reduce  E->i
$E		$		Reduce  E->E*E
String is accepted"""
