import matplotlib.pyplot as plt
from matplotlib import style
import random
import numpy as np

class K_means:

    def __init__ (self, k = 2, tol = 0.001, max_iter = 300000 ):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter


    def fit( self, data):

        self.centroids = {}

        ######## important ###############
        ####### the initial k centroids are chosen as the inital k points of
        ####### the data set, we can use other algorithms for the initialization too
    
        for i in range(self.k):
            self.centroids[i] = data[i]; 



        for i in range(self.max_iter):

            ##each iteration we are gonna clear out the classifications
            print(i)
            ##the key in this dict is the centroid/cluster id, the value is a list of points
            self.classifications = {}

            #set the centroid ids
            for i in range(self.k):
                ## k is the number of clusters/centroids that we have
                ## each centroid has its own key marked as 0,1,2... and a list of  points
                ## as values
                self.classifications[i] = []

            
            ## distance from datapoints to centroids
            for featureset in data:
                distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids ]
                ##distances gives a distance from a point featureset to all the centroids marked 0,1,2..

                ##classification gets the centroid id with the minimum distance
                classification = distances.index( min(distances) )

                ##append to the key-value pair of that centroid the particular featureset
                self.classifications[classification].append(featureset)


            
            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis = 0)
                
            optimized = True

            for c in self.centroids:
                original_centroid  = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum ( (current_centroid - original_centroid)/original_centroid * 100.0 ) > self.tol:
                    optimized = False

            if optimized:
                break
        




          

    def predict(self, data):
                distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids ]
                ##distances gives a distance from a point featureset to all the centroids marked 0,1,2..

                ##classification gets the centroid id with the minimum distance
                classification = distances.index( min(distances) )
                return classification




style.use('ggplot')
#IMPORT DATA from csv
X = np.genfromtxt('my_file.csv', delimiter=',')



#set colors
colors = 10 * [ "g", "r", "c", "b", "k"]
clf = K_means(k=3)
clf.fit(X)

for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1], marker ="o", color = "k", s = 100, linewidths = 5 )

for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter( featureset[0], featureset[1], marker = "x", color = color, s = 50, linewidths = 5)

#unk = np.array ( [ [1,2],[1,2.5], [1,3], [4,5] ] )
#for u in unk:
#    classification = clf.predict(u)
#    plt.scatter ( u[0], u[1], marker = "*", color = colors[classification] )
    
plt.show()




        



