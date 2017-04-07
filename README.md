

Importance of Human Judgment in Machine Learning
Analysis of various seeding methods for K-means algorithm

Aditya Singh Verma
Department of I&CT, MIT Manipal
adityasinghverma314@gmail.com

Anshul Jain
Department of I&CT, MIT Manipal
anshul.jain.0796@gmail.com



Abstract— Comparing various seeding methods for K-means algorithm.
Keywords— unsupervised learning, K-means, human judgment, machine learning, pattern recognition

I.  Introduction 

Due to the surge in processing power and speed, machine learning and artificial intelligence algorithms are becoming ubiquitous.  Thousands of applications and organizations depend on the results from these soft-computing  algorithms.

While it has become easier to deploy machine learning solutions using tools such as R studio, TensorFlow, Caffe and so on, there exists a problem.  We may have made dozens of mistakes in creating our model and yet the algorithm would churn out solutions and we may never know that the answers were wrong! 

This is because there is a huge scope for error.  We may have used a wrong model,  for example used clustering where regression could have worked better, or perhaps an error in getting data – like using the wrong features, or an error in   pre-processing such as a failure to normalize data.   
 

II.  Objective
Our objective is to compare two different methods of seeding the K-means algorithm.  Seeding is the process of choosing the initial centroid values.  A better initial seeding means that it would take the centroids lesser time to reach optimal values, which is absolutely critical given the time complexity of K-means  is 
		   O ( n * K * t )

where  n is the total number of points in the dataset, K is the number of clusters and t is the number of iterations it took the algorithm to reach a solution. A smaller value for t increases the performance which is absolutely critical.



III. Methodology

A. Implimenting the K-means algorithm in Python

Centroids = dict()
chooseCentroids()
 for  j  in range( 0, K ):
    print(“iteration number”, j )
    classification = dict()

    for point in dataSet:
        dist = [norm(point – cntrd) for cntrd in Centroids ]
        temp = dist . index( min (dist) )
        classification[temp].append(point)

        
    compareWithPreviousCentroids()
    if Optimized():
        break

We implement the generic K-means algorithm and then write two different functions for chooseCentroids(), one to choose centroids randomly and in the other we give the user a preference to choose the initial data points



B. Randomized Apporach

for i in range( 0, K ):
    centroids[i] = np.array( [ randint(1,100), randint(1,100)] )

In this approach we choose K centroids randomly and then run the generalized K-means algorithm.






C. Asking user for input 
        image = PIL.Image.open(r'graph.png')
        image.show()
        print ("Choose ", K , " data points")
        for i in range(0, K):
            a,b = input().split(' ')
            centroids[i] = numpy.array ( [ int(a), int(b)] )  

We display a scatter plot of the data, and the user is asked to enter K points, after which the algorithm is run.
            

IV. Dataset
We set k as 3 run the algorithm on datasets of different sizes,  100, 125, 150, 175 and 200 for both randomized and user selected.  The values of the dataset were generated using a random dataset generator, with values ranging from 1 to 100. [1]



V. Conclusion

In this paper we make a case for the involvement of humans at the early stages of application of machine learning algorithms, because while it may be more efficient theoretically, human 
judgment as we showcased can tend to benefit the learning curve of the machine. 				                          
Focus on all aspects of the algorithm such as seeding with inspection from a human will help improve
efficiency and reduce the number of iterations for which the algorithm runs and perhaps eventually
improve on the algorithm to better its time complexity.


VI. Future Scope

With further development, the algorithm could have fewer iterations if a human is involved in the initial stages of  algorithm implementation. We can compare various other methods such as K-means++ and use proper statistical methods to compare the different seeding methods.

        
Acknowledgment 

We would like to thank our teacher Mr. Chethan Sharma who taught us Pattern Recognition, for his help and support.

References

[1] Data generated from https://www.mockaroo.com/
[2] All code used uploaded at git
