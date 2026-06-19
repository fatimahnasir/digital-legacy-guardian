import numpy as np
from sklearn.cluster import KMeans

sample_scores = np.array([
    [95],
    [90],
    [85],
    [50],
    [45],
    [30],
    [20],
    [10]
])

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

kmeans.fit(sample_scores)

def get_priority(category):

    if category == "Financial":
        return "Critical"

    elif category == "Legal":
        return "Important"

    else:
        return "Normal"