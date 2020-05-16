# The aim of this exercise was to group customers into groups based on their age and spending habit.

# The dataset was not available for the students to download, but it contains data of the spending habits of customers of different ages.
# Each data point has two values, age of the customer and the money spent.


# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
import numpy as np
from sklearn.mixture import GaussianMixture
from scipy.stats import multivariate_normal # Multivariate normal random variable

# Read in data from the csv file and store it in the data matrix X. The dataset contains m = 400 data points.

df = pd.read_csv("/coursedata/R5_Clustering/data.csv")
X = np.array(df)

n, m = X.shape

# Define the number of clusters
k = 3

means = np.zeros((k, m))  # Array for storing the cluster means
covariances = np.zeros((k, m, m))  # Array for storing the covariance matrices
cluster_labels = np.zeros(n)  # Array for storing the cluster labels of each data point

np.random.seed(1)    # Set random seed for reproducability

### STUDENT TASK ###
gmm = GaussianMixture(n_components = k, covariance_type = 'full', random_state = 1)
gmm.fit(X)


y_pred = gmm.predict(X)

cluster_labels = y_pred

means = gmm.means_
covariances = gmm.covariances_

### STUDENT TASK ###


plot_GMM(X, means, covariances, k, cluster_labels)
print("The means are:\n", means, "\n")
print("The covariance matrices are:\n", covariances)
