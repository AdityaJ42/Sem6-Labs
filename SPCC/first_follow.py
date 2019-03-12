# First and Follow for a grammar


def find_first(lhs, rhs):
	first_list = []
	for prod in rhs:
		for letter in prod:
			if not letter.isupper():
				first_list.append(letter)
				break
			else:
				f = find_first(letter, rules[letter])
				if '@' not in f:
					first_list.append(' '.join(f))
					break
				else:
					f.remove('@')
					first_list.append(' '.join(f))
					continue
	return first_list


def find_follow(variable, rules, first_set):
	follow_list = []
	if variable == 'S':
		follow_list.append('$')
	variables = rules.keys()
	for temp in variables:
		for prod in rules[temp]:
			if variable in prod:
				index = prod.index(variable)
				while True:
					if index >= len(prod) - 1:
						if variable != temp:
							follow_list += find_follow(temp, rules, first_set)
						break
					else:
						if prod[index + 1] not in variables:
							follow_list += prod[index + 1]
							break
						t = first_set[prod[index + 1]][:]
						if '@' in t:
							t.remove('@')
							follow_list += t
							index += 1
						else:
							follow_list += t
							break
	return set(follow_list)

n = int(input('Enter the number of production rules: '))
rules = {}
for i in range(n):
	rule = input('Enter rule ' + str(i + 1) + ': ').split('->')
	rules[rule[0]] = rule[1].strip().split('|')

first = {}
for i in rules:
	first[i] = find_first(i, rules[i])

follow = {}
for variable in rules.keys():
	follow[variable] = find_follow(variable, rules, first)

print('Symbol\tFirst\tFollow')
for nonterm in rules.keys():
	print('{}\t{}\t{}'.format(nonterm, first[nonterm], follow[nonterm]))
