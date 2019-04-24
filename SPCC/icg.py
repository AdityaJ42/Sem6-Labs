# Intermediate Code Generation (Relational part is sort of hardcoded)
def postfix(exp, precedence):
	stack, postfix = [], ''
	for i in exp:
		if i.isalpha():
			postfix += i
		else:
			if not stack:
				stack.append(i)
			elif precedence[i] > precedence[stack[-1]] or (i == stack[-1] and i == '^'):
				stack.append(i)
			else:
				while stack and precedence[i] < precedence[stack[-1]]:
					postfix += stack.pop()
				stack.append(i)

	while stack:
		postfix += stack.pop()
	return postfix


def arithmetic(expr):
	e = 'k=' + expr
	three_ac = assignment(e)
	return three_ac[:-1]


def assignment(expr):
	precedence = {'^': 3, '/': 2, '*': 2, '-': 1, '+': 1}
	three_ac, temp, count = [], [], 0
	expr = expr.split('=')
	converted = postfix(expr[1].strip(), precedence)
	for i in converted:
		if i.isalpha():
			temp.append(i)
		else:
			op2, op1 = temp.pop(), temp.pop()
			name = 't' + str(count)
			count += 1
			three_ac.append('{} = {}'.format(name, op1 + i + op2))
			temp.append(name)
	three_ac.append('{} = {}'.format(expr[0], temp.pop()))
	return three_ac


def get_index(index, eqn, t):
	c = eqn[:3]
	print('{}: if {} goto {}'.format(index, c, index + 3))
	index += 1
	print('{}: t{} = 0'.format(index, t))
	index += 1
	print('{}: goto {}'.format(index, index + 2))
	index += 1
	print('{}: t{} = 1'.format(index, t))
	index += 1
	return index


def relational(expr):
	total, index = 0, 100
	expr1 = expr[:4]
	count = [0, 0, 0, 0, 0]
	while '&&' in expr or '||' in expr:
		op = expr[3:5]
		if op == '&&':
			count[total] = 1
		total += 1
		expr = expr[5: len(expr) + 1]
		index = get_index(index, expr, total)

	total += 1
	index = get_index(index, expr1, total)
	c = total - 1
	for i in range(c):
		if count[i]:
			line = '{}: t{} = t{} and t{}'.format(index, total, total - 1, i + 2)
		else:
			line = '{}: t{} = t{} or t{}'.format(index, total, total - 1, i + 2)
		print(line)
		index += 1

while True:
	choice = int(input('1.Arithmetic  2.Assignment  3.Relational: '))
	if choice == 1:
		expression = input('Enter the expression: ')
		expression = expression.strip()
		icg = arithmetic(expression)
		print('\n'.join(icg))
	elif choice == 2:
		expression = input('Enter the expression: ')
		expression = expression.strip()
		icg = assignment(expression)
		print('\n'.join(icg))
	elif choice == 3:
		expression = input('Enter the expression: ')
		expression = expression.strip()
		relational(expression)
	else:
		break
