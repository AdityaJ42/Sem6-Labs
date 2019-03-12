def distance(point, centroid):
	dist = 0
	for k in range(len(point)):
		dist += (point[k] - centroid[k]) ** 2
	return dist ** 0.5

n = int(input('Enter the number of data points: '))
data = []
for i in range(n):
	points = list(map(float, input('Enter point {}: '.format(i + 1)).split()))
	data.append(points)
k = int(input('Enter the number of clusters: '))
centroids = [data[i] for i in range(k)]
while True:
	clusters = [[] for i in range(k)]
	for point in data:
		d = []
		for j in centroids:
			d.append(distance(point, j))
		i = d.index(min(d))
		clusters[i].append(point)
	new_centroids = []
	for cluster in clusters:
		sum1, sum2 = 0, 0
		for point in cluster:
			sum1 += point[0]
			sum2 += point[1]
		new_centroids.append([round(sum1 / len(cluster), 2), round(sum2 / len(cluster), 2)])
	if new_centroids == centroids:
		break
	else:
		centroids = new_centroids

for i in range(k):
	print('Cluster {}: '.format(i + 1), end='')
	for points in clusters[i]:
		print(points, end=', ')
	print()
