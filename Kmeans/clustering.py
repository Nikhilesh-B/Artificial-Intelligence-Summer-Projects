#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:55:17 2020

@author: Nick
"""



n_colors = 64

from sklearn import cluster 

import numpy as np 
from scipy import ndimage 
from sklearn import cluster 

import matplotlib.pyplot as plt 
import matplotlib.pyplot as img


img = img.imread('trees.png')

plt.figure(figsize=(15,8))
plt.imshow(img)

x,y,z = img.shape 
img_2d = img.reshape(x*y,z)


def kmeans(k):
    kmeans_cluster = cluster.KMeans(n_clusters=k)
    kmeans_cluster.fit(img_2d)
    cluster_centers = kmeans_cluster.cluster_centers_ 
    cluster_labels = kmeans_cluster.labels_
    plt.figure(figsize=(15,8))
    plt.imshow(cluster_centers[cluster_labels].reshape(x,y,z))


def main():
    kmeans(3)
    kmeans(15)
    kmeans(64)
    
main()








