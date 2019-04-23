# Left Factoring
from os.path import commonprefix


def factor(lhs, rhs):
	variables = {}
	for i in range(len(rhs)):
		for j in range(len(rhs)):
			if i != j:
				prefix = commonprefix([rhs[i], rhs[j]])
				if prefix:
					if prefix in variables.keys():
						variables[prefix].add(i)
						variables[prefix].add(j)
					else:
						variables[prefix] = set([i, j])

	final_order = [k for k in sorted(variables, key=lambda k: len(variables[k]), reverse=True)]
	visited = [0 for i in rhs]
	global count

	for key in final_order:
		temp = []
		for i in variables[key]:
			if visited[i]:
				break
			visited[i] = 1
			temp.append(rhs[i][len(key):])
		if temp:
			count += 1
			lhs_new = lhs + "'" * (count - lhs.count("'"))
			print('{} -> {}'.format(lhs, key + lhs_new))
			factor(lhs_new, temp)

	for i in range(len(rhs)):
		if not visited[i]:
			print('{} -> {}'.format(lhs, rhs[i]))

s = 'S -> bSSaaS | bSSaSb | bSb | a'
v = s.split('->')
lhs, rhs = v[0].strip(), v[1].strip()
rhs = [x.strip() for x in rhs.split('|')]

count = 0
factor(lhs, rhs)
