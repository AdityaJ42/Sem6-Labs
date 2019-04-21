# Predictive Parser Table for given grammar (grammar without left recursion and factoring)
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
	if variable == 'E':
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


def parser_table(rules, first, follow):
	variables = rules.keys()
	table = {}
	for variable in variables:
		table[variable] = {}
		for prod in rules[variable]:
			i = 0
			while True:
				if i == len(prod) or prod[i] == '@':
					for terminal in follow[variable]:
						table[variable][terminal] = prod
					break
				c = prod[i]
				if c != '@' and c not in variables:
					table[variable][c] = prod
					break
				f = first[c]
				for t in f:
					if t != '@':
						table[variable][t] = prod
				if '@' in f:
					i += 1
					continue
				break
	return table

# n = int(input('Enter the number of productions: '))
rules, first, follow = {}, {}, {}
# for i in range(n):
# 	prod = input('Enter rule {}: '.format(i + 1)).split('->')
# 	rules[prod[0]] = prod[1].split('|')
rules = {'E': ['TR'], 'R': ['+TR', '@'], 'T': ['FQ'], 'Q': ['*FQ', '@'], 'F': ['i']}

first = {}
for i in rules:
	first[i] = find_first(i, rules[i])

follow = {}
for variable in rules.keys():
	follow[variable] = find_follow(variable, rules, first)

table = parser_table(rules, first, follow)
print('FIRSTS: {}'.format(first))
print('FOLLOWS: {}'.format(follow))
for variable in table.keys():
	print(variable)
	print(table[variable], end='\n\n')
