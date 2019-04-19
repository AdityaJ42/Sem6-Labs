# Hierarchical Clustering


def check(d):
	count = 0
	for i in d:
		for j in i:
			if j != 0:
				count += 1
	return count


def single_link(c):
	new_d = [[0 for i in range(len(c))] for j in range(len(c))]
	for i in range(len(c)):
		t1 = c[i]
		for j in range(i + 1, len(c)):
			m, t2 = 99999, c[j]
			for q in range(len(t1)):
				for w in range(len(t2)):
					dist = distance_matrix[ord(t1[q]) - 65][ord(t2[w]) - 65]
					if dist < m and dist != 0:
						m = dist
			new_d[i][j] = new_d[j][i] = m
	return new_d


def complete_link(c):
	new_d = [[0 for i in range(len(c))] for j in range(len(c))]
	for i in range(len(c)):
		t1 = c[i]
		for j in range(i + 1, len(c)):
			m, t2 = 0, c[j]
			for q in range(len(t1)):
				for w in range(len(t2)):
					dist = distance_matrix[ord(t1[q]) - 65][ord(t2[w]) - 65]
					if dist > m and dist != 0:
						m = dist
			new_d[i][j] = new_d[j][i] = m
	return new_d


def average_link(c):
	new_d = [[0 for i in range(len(c))] for j in range(len(c))]
	for i in range(len(c)):
		t1 = c[i]
		for j in range(i + 1, len(c)):
			dist, counter, t2 = 0, 0, c[j]
			for q in range(len(t1)):
				for w in range(len(t2)):
					dist += distance_matrix[ord(t1[q]) - 65][ord(t2[w]) - 65]
					counter += 1
			new_d[i][j] = new_d[j][i] = dist / counter
	return new_d


def form_clusters(cluster, distance):
	clusters, distances = cluster, distance
	while True:
		if check(distances) == 1:
			break

		minimum, item1, item2 = 99999, -1, -1
		for i in range(len(clusters)):
			for j in range(len(clusters)):
				if distances[i][j] != 0 and distances[i][j] < minimum:
					minimum, item1, item2 = distances[i][j], i, j

		clusters[item1] += clusters[item2]
		del(clusters[item2])

		print('Distance: {}\tClusters:'.format(minimum), end=' ')
		for i in clusters:
			print(i, end=', ')
		print()

		if len(clusters) == 1:
			break
		if choice == 1:
			distances = single_link(clusters)
		elif choice == 2:
			distances = complete_link(clusters)
		else:
			distances = average_link(clusters)


n = int(input('Enter the number of points: '))
distance_matrix, clusters = [], []
for i in range(n):
	d = list(map(float, input('Enter row {} of the distance matrix: '.format(i + 1)).split()))
	distance_matrix.append(d)
	clusters.append(chr(i + 65))
choice = int(input('1.Single Link\n2.Complete Link\n3.Average Link\nEnter your choice: '))

form_clusters(clusters, distance_matrix)
