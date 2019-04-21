# Lexical Analyzer
import string

operators = ['+', '-', '*', '/', '%', '^', '(', ')', '=']
keywords = ['int', 'float', 'string', 'while', 'for']
symbols = [',', ';', ':']


def identify_token(t):
	t = t.strip()
	if len(t) > 0:
		if t[0] == t[-1] and t[0] == '"':
			print('String constant: ', t)
		elif t.isnumeric():
			print('Number constant: ', t)
		elif t in keywords:
			print('Keyword: ', t)
		else:
			print('Variable: ', t)

with open('input.txt', 'r') as fd:
	contents = fd.read().split('\n')
for line in contents:
	line = line.strip()
	i, j, flag, n = 0, 0, 0, len(line)
	while j < n:
		if line[j] == '"':
			if flag:
				identify_token(line[i:j + 1])
				i = j + 1
			flag = not flag
			j += 1
		elif flag:
			j += 1
		elif line[j] in operators:
			if i == j:
				print('Operator: ', line[i])
				j += 1
				i = j
			else:
				identify_token(line[i:j])
				i = j
		elif line[j] in symbols:
			if i == j:
				print('Symbol: ', line[i])
				j += 1
				i = j
			else:
				identify_token(line[i:j])
				i = j
		elif line[j] in string.whitespace:
			identify_token(line[i:j + 1])
			j += 1
			i = j
		else:
			j += 1
	identify_token(line[i:j])
