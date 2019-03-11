# KMeans Clustering - 2 cluster structure
n = int(input('Enter dimensions: '))
if n == 1:
	x = list(map(float, input('Enter the data points: ').split()))
	y = [0 for i in range(len(x))]
elif n == 2:
	x = list(map(float, input('Enter the data points for x: ').split()))
	y = list(map(float, input('Enter the data points for y: ').split()))

m1 = [x[0], y[0]]
m2 = [x[1], y[1]]
c1, c2 = [], []
count = 1

while True:
	new_m1 = [0, 0]
	new_m2 = [0, 0]

	old_c1 = c1
	old_c2 = c2
	c1, c2 = [], []

	print('Iteration: ', count)
	print('Means: {}, {}'.format(m1, m2))
	print('CLusters: {}, {}'.format(old_c1, old_c2))

	for i in range(len(x)):
		d1 = ((x[i] - m1[0]) ** 2 + (y[i] - m1[1]) ** 2) ** 0.5
		d2 = ((x[i] - m2[0]) ** 2 + (y[i] - m2[1]) ** 2) ** 0.5

		if d1 < d2:
			c1.append((x[i], y[i]))
			new_m1[0] += x[i]
			new_m1[1] += y[i]
		else:
			c2.append((x[i], y[i]))
			new_m2[0] += x[i]
			new_m2[1] += y[i]

	if new_m1 != [0, 0]:
			m1 = [new_m1[0] / len(c1), new_m1[1] / len(c1)]
	if new_m2 != [0, 0]:
		m2 = [new_m2[0] / len(c2), new_m2[1] / len(c2)]

	if c1 == old_c1 or c2 == old_c2:
		break

	count += 1

print('\nFinal Clusters: ', c1, c2)
