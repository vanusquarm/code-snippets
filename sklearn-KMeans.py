from sklearn.cluster import KMeans
features = [[5, 3.4, 6], [1, 9.4, 19], [2, 9.1, 1]]

# Cluster into 3 groups

kmeans = KMeans(n_clusters=3).fit(features)

# Prints which data point belongs to which cLuster group
print(kmeans.labels_)

# Prints the metric of how cLustering performed
print(kmeans.inertia_)

# output 
[0 2 1]
0.0
