def to_postfix(expression, precedence):
	postfix = ''
	stack = []
	for i in expression:
		if (i <= 'z' and i >= 'a') or (i <= 'Z' and i >= 'A'):
			postfix += i
		elif i == '(':
			stack.append(i)
		elif i == ')':
			while stack[-1] != '(':
				postfix += stack.pop()
			stack.pop()
		else:
			if not stack:
				stack.append(i)
			elif (precedence[i] > precedence[stack[-1]]) or (i == stack[-1] and i == '^'):
				stack.append(i)
			else:
				while stack and precedence[i] <= precedence[stack[-1]]:
					postfix += stack.pop()
				stack.append(i)
	while stack:
		postfix += stack.pop()
	return postfix


def assignment():
	precedence = {'^': 3, '/': 2, '*': 2, '+': 1, '-': 1}
	expr = input('Enter the expression: ')
	res, expr = expr[0], expr[2:]
	postfix = to_postfix(expr, precedence)
	three_ac, temp, count = [], [], 0
	for ch in postfix:
		if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
			temp.append(ch)
		else:
			count += 1
			tname = 't' + str(count)
			op = tname + '='
			op2, op1 = temp.pop(), temp.pop()
			op += op1 + ch + op2
			three_ac.append(op)
			temp.append(tname)
	assg = res + '=t' + str(count)
	three_ac.append(assg)
	return three_ac


def arithmetic():
	pass


def relational():
	pass

while True:
	choice = int(input('1.Assignment  2. Arithmetic  3.Relational: '))
	if choice == 1:
		three_ac = assignment()
		print('\n'.join(three_ac))
	elif choice == 2:
		arithmetic()
	elif choice == 3:
		relational()
	else:
		break
