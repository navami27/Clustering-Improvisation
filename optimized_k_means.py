 import numpy as np
 import matplotlib.pyplot as plt
 from sklearn.datasets import load_iris
 def initialize_centroids(points, K):
 indices = np.random.choice(points.shape[0], K, replace=False)
 return points[indices]
 def closest_centroid(points, centroids):
 distances = np.linalg.norm(points[:, np.newaxis]- centroids, axis=2)
 return np.argmin(distances, axis=1)
 def compute_centroids(points, labels, K):
 return np.array([points[labels == k].mean(axis=0) for k in range(K)])
 def k_means(points, K, max_iterations=100):
 centroids = initialize_centroids(points, K)
 for _ in range(max_iterations):
 labels = closest_centroid(points, centroids)
 new_centroids = compute_centroids(points, labels, K)
 if np.all(centroids == new_centroids):
 break
 centroids = new_centroids
5
 return centroids, labels
 # Load the Iris dataset
 iris = load_iris()
 points = iris.data[:, :2] # Use only the first two features for visualization
 K =3 #Numberofclusters
 # Perform k-means clustering
 centroids, labels = k_means(points, K)
 # Plot the results
 plt.figure(figsize=(8, 6))
 scatter = plt.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis', marker='o',
 edgecolor='k', s=50)
 plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200, label='Centroids')
 plt.xlabel('Sepal length')
 plt.ylabel('Sepal width')
 plt.title('K-means Clustering of Iris
 Dataset')
 plt.legend()
 plt.colorbar(scatter, label='Cluster
 label')
 plt.grid(True)
 plt.show()
