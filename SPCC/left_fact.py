# Left Factoring (works for single common variable)
def factor(lhs, rhs):
	global count
	visited, variables, beta = [0 for i in rhs], {}, []
	for i in range(len(rhs)):
		if visited[i] == 0:
			flag, visited[i], rule = 0, 1, rhs[i]
			for j in range(i + 1, len(rhs)):
				if visited[j] == 0 and rule[0] == rhs[j][0]:
					visited[j], flag = 1, 1
					variables[rule[0]] = variables.get(rule[0], []) + [rhs[j][1:]]
			if flag:
				variables[rule[0]] = variables.get(rule[0], []) + [rule[1:]]
			else:
				beta.append(rule)

	for key in variables:
		count += 1
		lhs_new = lhs + "'" * (count - lhs.count("'"))
		print('{} -> {}'.format(lhs, key + lhs_new))
		factor(lhs_new, variables[key])
	for rem in beta:
		print('{} -> {}'.format(lhs, rem))

prod = 'A->aB|aC|aD|Z'
prod = prod.split('->')
l, r = prod[0], prod[1].split('|')
count = 0
factor(l, r)
