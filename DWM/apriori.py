def find_rules(s, data, t, sup):
	count = 0
	global min_conf
	for k in range(len(data)):
		found = True
		for j in s:
			if data[k][ord(j) - 65] != 1:
				found = False
				break
		if found:
			count += 1
	if (sup / count) * 100 > min_conf:
		print('{} => {}'.format(s, t.replace(s, '')))

fd = open('Apriori.csv')
data = []
for n, line in enumerate(fd):
	if n != 0:
		contents = line.split(',')
		data.append([int(i.rstrip()) for i in contents[1:]])

min_support = int(input('Enter the minimum support: '))
min_conf = int(input('Enter the minimum confidence: '))
items = [chr(i + 65) for i in range(len(data[0]))]
final_large = []
final_support = 0

iteration = 1
while True:
	iteration += 1
	support = [0 for i in range(len(items))]
	large = []
	for i in range(len(items)):
		count = 0
		for k in range(len(data)):
			found = True
			for j in items[i]:
				if data[k][ord(j) - 65] != 1:
					found = False
					break
			if found:
				count += 1
		support[i] = count

	print('\nCandidate Set:\nItem\tSupport')
	for i in range(len(support)):
		print('{}\t{}'.format(items[i], support[i]))
		if support[i] >= min_support:
			large.append(items[i])
	print('Large Item Set: ')
	for i in range(len(large)):
		print(large[i])
	if len(large) == 1:
		final_large = large
		final_support = support[items.index(large[0])]
		break

	items = []
	for i in range(len(large)):
		temp1 = large[i]
		for j in range(i + 1, len(large)):
			temp2 = large[j]
			temp3 = list(temp1 + temp2)
			temp = []
			for i in range(len(temp3)):
				if temp3[i] not in temp3[i + 1:]:
					temp.append(temp3[i])
			temp.sort()
			temp = ''.join(temp)
			if len(temp) == iteration:
				if temp not in items:
					items.append(temp)

t, sup = final_large[0], final_support
print('\nAssociation Rules')
find_rules(t[0], data, t, sup)
find_rules(t[1], data, t, sup)
if len(t) == 3:
	find_rules(t[2], data, t, sup)
	find_rules(t[0] + t[1], data, t, sup)
	find_rules(t[1] + t[2], data, t, sup)
	find_rules(t[0] + t[2], data, t, sup)
