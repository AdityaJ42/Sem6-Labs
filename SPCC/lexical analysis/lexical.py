contents = []
keywords = ['int', 'void', 'char', 'printf']
delimiters = ['#', ' ', ',', ';']

fd = open('program.txt', 'r')
f1 = open('keywords.txt', 'w')
f2 = open('operators.txt', 'w')
f3 = open('identifier.txt', 'w')
f4 = open('literal.txt', 'w')
f5 = open('seperators.txt', 'w')

for n, line in enumerate(fd):
	data = line.strip().split('\n')
	if data != ['']:
		contents.append(''.join(data))
fd.close()

print('Input Program:')
for item in contents:
	print(item)

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
