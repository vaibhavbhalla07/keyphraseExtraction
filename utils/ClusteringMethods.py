from sklearn import cluster
from utils import CreateDictionaries as cdict
import numpy as np


def hierarchial_cluster(X,no_clusters):
    ward = cluster.AgglomerativeClustering(n_clusters=no_clusters, linkage='ward').fit(X)
    label = ward.labels_
    return label


def spectral_cluster(X,no_clusters):
    spectralCluster = cluster.SpectralClustering(n_clusters = no_clusters, affinity = 'precomputed').fit(X)
    spectral_label = spectralCluster.labels_
    return spectral_label


def affinity_propagation(X):
    af = cluster.AffinityPropagation(preference=-50,affinity = 'precomputed')
    af.fit_predict(X)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_
    return labels,cluster_centers_indices


def createClusters(matrix_sim,unique_words,num_clusters=15,clusteringType="affinity"):
    labels=[]
    if clusteringType=="spectral":
        labels = spectral_cluster(matrix_sim, num_clusters)
    if clusteringType=="hierarchial":
        labels = hierarchial_cluster(matrix_sim, num_clusters)
    if clusteringType=="affinity":
        labels,cluster_centers = affinity_propagation(matrix_sim)
        dict_clusters = cdict.getClustersDictionary(labels, unique_words, matrix_sim)
        return labels,cluster_centers, dict_clusters
    dict_clusters = cdict.getClustersDictionary(labels, unique_words, matrix_sim)
    return labels, dict_clusters

