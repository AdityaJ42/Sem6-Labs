# Hierarchical Clustering - Single Link


def check(d):
	count = 0
	for i in d:
		for j in i:
			if j != 0:
				count += 1
	return count


def form_clusters(cluster, distance):
	clusters, distances = cluster, distance
	while True:

		if check(distances) == 1:
			break
		# Finding minimum distance to group
		minimum, item1, item2 = 9999, -1, -1
		for i in range(len(clusters)):
			for j in range(len(clusters)):
				if distances[i][j] != 0 and distances[i][j] < minimum:
					minimum, item1, item2 = distances[i][j], i, j
		# Grouping points
		clusters[item1] += clusters[item2]
		del(clusters[item2])
		# Display Clusters
		print('Distance: {}  Clusters: '.format(minimum), end=' ')
		for i in clusters:
			print(i, end=' ')
		print()
		if len(clusters) == 1:
			break
		# Updating distance as per new clusters
		new_distances = [[0 for i in range(len(clusters))] for j in range(len(clusters))]
		for i in range(len(clusters)):
			t1 = clusters[i]
			for j in range(i + 1, len(clusters)):
				t2 = clusters[j]
				m = 9999

				for q in range(len(t1)):
					for w in range(len(t2)):
						e = original_distance[ord(t1[q]) - 65][ord(t2[w]) - 65]
						if e != 0 and e < m:
							m = e
				new_distances[i][j] = new_distances[j][i] = m
		distances = new_distances

n = int(input('Enter the number of points: '))
distance = []
clusters = []
for i in range(n):
	d = list(map(float, input('Enter the row {} of distance vector: '.format(str(i + 1))).split()))
	distance.append(d)
	clusters.append(chr(i + 65))

original_distance = distance
form_clusters(clusters, distance)
