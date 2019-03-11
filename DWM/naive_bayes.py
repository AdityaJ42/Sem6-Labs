# Naive Bayes Algorithm
import pandas as pd


def pci(data):
	classes = [0, 0]
	for i in range(1, len(data)):
		if data.iloc[i, -1] == "Yes":
			classes[0] += 1
		else:
			classes[1] += 1
	return classes[0], classes[1]


def pcix(data, x, pos, neg):
	count_yes = [0 for i in range(len(data.columns) - 1)]
	count_no = [0 for i in range(len(data.columns) - 1)]
	p1 = 1
	p2 = 1

	for i in range(len(data)):
		if data.iloc[i, 0] == x[0]:
			if data.iloc[i, -1] == "Yes":
				count_yes[0] += 1
			else:
				count_no[0] += 1
		if data.iloc[i, 1] == x[1]:
			if data.iloc[i, -1] == "Yes":
				count_yes[1] += 1
			else:
				count_no[1] += 1
		if data.iloc[i, 2] == x[2]:
			if data.iloc[i, -1] == "Yes":
				count_yes[2] += 1
			else:
				count_no[2] += 1
		if data.iloc[i, 3] == x[3]:
			if data.iloc[i, -1] == "Yes":
				count_yes[3] += 1
			else:
				count_no[3] += 1

	for i in range(len(count_no)):
		p1 = p1 * count_yes[i] / pos
		p2 = p2 * count_no[i] / neg
	return p1, p2

dataset = pd.read_csv('DataSet.csv')
dataset = dataset.iloc[:, 1:]
X = input('Enter the tuple values(age, income, student, credit rating): ')
X = X.split(',')

c1, c2 = pci(dataset)
p1, p2 = pcix(dataset, X, c1, c2)
print('Prediction by Naive Bayes Classifier:', end=' ')
if (p1 * c1 / len(dataset)) > (p2 * c2 / len(dataset)):
	print('The person will buy the computer')
else:
	print('The person will not buy the computer')
