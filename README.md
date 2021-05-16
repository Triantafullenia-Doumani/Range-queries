# Range-queries

Implement a range query evaluation function in R-Tree. The range
of the question is determined by a rectangle W and the aim is to find the MBRs
intersecting W. The function takes as its argument the nodeid of the root of R-
tree, the rectangle-question W in the format [x-low, x-high, y-low, y-high] and will calculate the
query results using the R-tree.

The Rqueries.txt file contains examples of 'queries'.

python3 Range_queries.py Rtree.txt Rqueries.txt
