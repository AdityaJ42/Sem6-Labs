import copy
n = int(input('Enter number of rules: '))
rules = {}
for i in range(n):
    a, b = map(str.strip, input('Enter rule ' + str(i+1) + ': ').split('='))
    rules[a] = list(map(list, map(str.strip, b.split('|'))))

x = copy.deepcopy(rules)

for i in x:
	starters = [j[0] for j in x[i]]
	starters = set([y for y in starters if starters.count(y) > 1])
	for c in starters:
		rules["("+i+c+"')"] = []
		for j in x[i]:
			if j[0] == c:
				rules["("+i+c+"')"].append(j[1:])
				rules[i].remove(j)
		rules[i].append([c, "("+i+c+"')"])

for i in rules:
    for j in range(len(rules[i])):
        rules[i][j] = ''.join(rules[i][j])
    print(i + ' = ' + ' | '.join(map(str, rules[i])))
