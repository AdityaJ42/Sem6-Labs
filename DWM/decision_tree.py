import numpy as np
import pandas as pd
from numpy import log2 as log

eps = np.finfo(float).eps


def find_entropy(df):
	classes = df.keys()[-1]
	entropy = 0
	values = df[classes].unique()
	for value in values:
		fraction = df[classes].value_counts()[value] / len(df[classes])
		entropy += -fraction * log(fraction)
	return entropy


def find_attribute_entropy(df, attribute):
	classes = df.keys()[-1]
	entropy2 = 0
	target_variables = df[classes].unique()
	variables = df[attribute].unique()
	for variable in variables:
		entropy = 0
		for target_variable in target_variables:
			num = len(df[attribute][df[attribute] == variable][df[classes] == target_variable])
			den = len(df[attribute][df[attribute] == variable])
			fraction = num / (den + eps)
			entropy += -fraction * log(fraction + eps)
		fraction2 = den / len(df)
		entropy2 += -fraction2 * entropy
	return abs(entropy2)


def best_attribute(df):
	attr_gain = []
	for key in df.keys()[:-1]:
		attr_gain.append(find_entropy(df) - find_attribute_entropy(df, key))
	return df.keys()[:-1][np.argmax(attr_gain)]


def get_subtable(df, node, value):
	return df[df[node] == value].reset_index(drop=True)


def build_tree(df, tree=None):
	node = best_attribute(df)
	attribute_value = np.unique(df[node])
	if tree is None:
		tree = {}
		tree[node] = {}
	for value in attribute_value:
		sub_table = get_subtable(df, node, value)
		class_value, counts = np.unique(sub_table['CLASS'], return_counts=True)

		if len(counts) == 1:
			tree[node][value] = class_value[0]
		else:
			tree[node][value] = build_tree(sub_table)
	return tree


def predict(example, tree):
	prediction = 0
	for nodes in tree.keys():
		value = example[nodes]
		tree = tree[nodes][value]

		if type(tree) is dict:
			prediction = predict(example, tree)
		else:
			prediction = tree
			break
	return prediction


df = pd.read_csv('DataSet.csv')
df = df.iloc[:, 1:]
X = input('Enter the tuple values(age, income, student, credit rating): ').split(',')
test = {'AGE': X[0], 'INCOME': X[1], 'STUDENT': X[2], 'CREDIT': X[3]}

tree = build_tree(df)
prediction = predict(test, build_tree(df))
print("Tree Structure: ", tree)
print("Prediction: ", prediction)

# Middle,Medium,No,Excellent
