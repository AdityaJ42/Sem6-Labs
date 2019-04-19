# Naive Bayes Algorithm
import pandas as pd


def pci(data):
	class_count = [0, 0]
	for i in range(len(data)):
		if data.iloc[i, -1] == 'Yes':
			class_count[0] += 1
		else:
			class_count[1] += 1
	return class_count[0], class_count[1]


def pcix(data, x, c1, c2):
	p1, p2 = 1, 1
	count_yes = [0 for i in range(len(data.columns) - 1)]
	count_no = [0 for i in range(len(data.columns) - 1)]

	for i in range(len(data)):
		for j in range(len(data.columns) - 1):
			if data.iloc[i, j] == x[j]:
				if data.iloc[i, -1] == 'Yes':
					count_yes[j] += 1
				else:
					count_no[j] += 1

	for i in range(len(count_yes)):
		p1 = p1 * count_yes[i] / c1
		p2 = p2 * count_no[i] / c2
	return p1, p2

data = pd.read_csv('NB.csv')
data = data.iloc[:, 1:]
X = input('Enter tuple to classify: ')
X = X.split(',')
c1, c2 = pci(data)
p1, p2 = pcix(data, X, c1, c2)

if (p1 * c1 / len(data)) > (p2 * c2 / len(data)):
	print('Buys')
else:
	print('No Buy')

"""
Enter tuple to classify: Youth,Medium,Yes,Fair
Buys
"""
