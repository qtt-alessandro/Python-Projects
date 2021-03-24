import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD
from sklearn import datasets
import matplotlib.pyplot as plt
import random
import numpy as np


def classification(c, x):
    min_ = float('inf')
    for k in c.keys():
        val = np.sqrt(sum(((c[k]-x)**2)))
        if min_ >= val:
            min_ = val
            class_ = k

    return class_


def Inizialize_centroid(x, k):
    List = random.sample(list(x), k)
    return {i: List[i] for i in range(k)}


def K_Means(X, k, threshold = 100):

    Centroids = Inizialize_centroid(X, k)
    Num_class = len(Centroids.keys())

    count = 0
    Distance = float('inf')

    while count < threshold and Distance > 10**-7:

        Distance = 0

        class_ = np.apply_along_axis(lambda x: classification(Centroids, x), 1, X)

        old = Centroids.copy()

        for k in Centroids.keys():
            idx =  np.where(class_ == k)
            Centroids[k] = sum(X[idx[0], :])/X[idx[0], :].shape[0]

            Distance +=  np.sqrt(sum((Centroids[k] - old[k])**2))/Num_class

        count += 1
        print(Distance)
    return Centroids, np.apply_along_axis(lambda x: classification(Centroids, x), 1, X)
