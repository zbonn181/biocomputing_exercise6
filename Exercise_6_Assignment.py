#Problem 1
def mimic_head(filename, nlines):
        from itertools import islice
        with open(filename) as myfile:
                for line in islice(myfile, nlines):
                        print(line)
print("Problem 1:")
mimic_head('wages.csv',2)

#Problem 2
#Part 1
import pandas as pd
iris = pd.read_csv("iris.csv")
iris2 = iris.iloc[[-2,-1], [-2,-1]]
print("Problem 2:")
print("Part 1:")
print(iris2)

#Part 2
#I opted to have my code return a data frame stating there are 50 values for each measurement for each species,
#so you know that the number of observations (where each row is an observation) is 50 since each measurement
#returns a value of 50, meaning that there are 50 rows of observations per species.  I thought this made it
#easier to interpret and understand what is actually being printed than using .size() instead of .count()
print("\nPart 2:")
print(iris.groupby("Species").count())

#Part 3
print("\nPart 3: ")
print(iris[iris["Sepal.Width"] > 3.5])

#Part 4
setosa = iris[iris["Species"] == "setosa"]
setosa.to_csv("setosa.csv")

#Part 5
virginica = iris[iris["Species"] == "virginica"]
print("\nPart 5: ")
print("Mean virginica petal length is:", virginica["Petal.Length"].mean())
print("Minimum virginica petal length is:", virginica["Petal.Length"].min())
print("Maximum virginica petal length is:", virginica["Petal.Length"].max())
