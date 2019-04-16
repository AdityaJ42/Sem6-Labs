contents = ''
with open('input.txt', 'r') as fd:
	contents = fd.read().split('\n')

mdt = open('mdt.txt', 'a')
mnt = open('mnt.txt', 'a')
cala = open('cala.txt', 'a')
pala = open('pala.txt', 'a')
mntc, mdtc, palac, calac = 0, 0, 0, 0

mdt.write('Index\tDefinition\n')
mnt.write('Index\tName\tIndex\n')
pala.write('Index\tArgument\n')
cala.write('Index\tArgument\n')

while contents:
	line = contents[0]
	i = 1
	if 'macro' in line:
		temp1 = line.split()
		mnt.write('{}\t{}\t{}\n'.format(mntc, temp1[1], mdtc))
		mntc += 1
		temp2 = temp1[2].split(',')
		for j in temp2:
			pala.write('{}\t{}\n'.format(palac, j))
			palac += 1
		line = contents[i]
		while 'mend' not in line:
			i += 1
			mdt.write('{}\t{}\n'.format(mdtc, line))
			mdtc += 1
			line = contents[i]
		mdt.write('{}\t{}\n'.format(mdtc, line))
		contents = contents[i + 1:]
	else:
		temp1 = line.split()
		temp2 = temp1[1].split(',')
		for j in temp2:
			cala.write('{}\t{}\n'.format(calac, j))
			calac += 1
		contents = contents[1:]

mdt.close()
mnt.close()
pala.close()
cala.close()
