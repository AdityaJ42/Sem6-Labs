def distance_vector(x, y):
	n = len(x)
	distance = []
	for i in range(n):
		d = []
		for j in range(n):
			dist = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
			d.append(round(dist, 2))
		distance.append(d)
	return distance

n = int(input('Enter the number of data points: '))
x, y = [], []

for i in range(n):
	points = list(map(float, input('Enter coordinates of point {}: '.format(i + 1)).split()))
	x.append(points[0])
	y.append(points[1])

distance = distance_vector(x, y)
print('Distance Matrix:')
for i in range(n):
	for j in range(n):
		print(distance[i][j], end='\t')
	print()
