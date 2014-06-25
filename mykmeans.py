import matplotlib.pyplot as pyplot
import math
import random
import numpy as np
def addVectors(vec1, vec2):
	vec = [None, None]
	n = len(vec1)
	d = 0
	for i in range(0,n):
		vec[i] = vec1[i] + vec2[i]
	return vec

def multiplybyvalue(value, vec1):
	vec = [None, None]
	n = len(vec)
	for i in range(0,n):
		vec[i] = value * vec1[i]
	return vec

def euclidianDistance (vec1 , vec2):
	N = len(vec1)
	d = 0
	for i in range(0,N):
		d += pow (vec1[i] - vec2[i], 2)
	d = math.sqrt (d)
	return d

def getRandomVectors(k, vectors):
	n = len(vectors)
	selectedVectors = []
	selectedIndices = []
	testedIndices = {}
	selected = 0
	tested = 0
	while selected < k :
		randomIndex = random.randint(0,n-1)
		if randomIndex in testedIndices:
			continue

		testedIndices[randomIndex] = 1
		tested += 1
		vector = vectors[randomIndex]
		select = True
		if vector in selectedVectors:
			select = False
		if select:
			selectedVectors.append(vector)
			selectedIndices.append(randomIndex)
			selected += 1
	return selectedVectors


def kmeans(k, vectors):
	n = len(vectors)
	assignments = []
	clustersizes = []
	repeat = True
	nb_iters = 0

	best = 0
	dist = 0
	for i in range(0,k):
		clustersizes.append(0)
	for i in range(0,n):
		assignments.append(0)
	centroids = getRandomVectors(k, vectors)
   	while(repeat):
   		for i in range(0, n):
   			mindist = np.inf
   	 		vector = vectors[i]
   	 		for j in range(0, k):
   	 			dist = euclidianDistance(centroids[j], vector)
   	 			if dist < mindist:
   	 				mindist = dist
   	 				best = j
   	 		clustersizes[best] += 1
   	 		assignments[i] = best

   	 	for i in range(0,n):
			newcentroids = []
			for i in range(0,n):
				newcentroids.append(None)
			for i in range(0,n):
				cluster = assignments[i]
				if newcentroids[cluster]==None:
					newcentroids[cluster] = vectors[i]
				else:
					newcentroids[cluster] = addVectors(newcentroids[cluster],
					vectors[i])

			for i in range(0,k):
				newcentroids[i] = multiplybyvalue (
				float(1) / float(clustersizes[i]), newcentroids[i])
			repeat = False
			for i in range(0,k):
				if centroids[i] != newcentroids[i]:
					repeat = True
					break
			centroids = newcentroids
			nb_iters += 1

			if nb_iters > 10:
				repeat = False
	for i in range(0,n):
		print vectors[i][0], "\t", vectors[i][1], "\t", assignments[i], "\t", centroids[assignments[i]][0], "\t", centroids[assignments[i]][1]


data = [
      {'company': 'Microsoft' , 'size': 9259, 'revenue': 6420},
      {'company': 'IBM' , 'size': 40000, 'revenue': 9878},
      {'company': 'Skype' , 'size': 700, 'revenue': 716},
	{'company': 'SAP' , 'size': 48000, 'revenue': 11567},
      {'company': 'Yahoo!' , 'size': 14000 , 'revenue': 6426 },
      {'company': 'eBay' , 'size': 15000, 'revenue': 8700}
	];

labels = []
vectors = []
x = []
y = []
for i in range(0, len(data)):
	labels.append(data[i]['company'])
	vectors.append([data[i]['size'] , data[i]['revenue']])
	x.append(data[i]['size'])
	y.append(data[i]['revenue'])

#print x
#pyplot.scatter(x,y)
#pyplot.savefig('test.png')
kmeans(3, vectors)
