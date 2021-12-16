# Identifying Triangles in Drosophila (spelling) Interactome

#Abstract

There are several ways to visualize the interactions of proteins. One of them is to create a graph 
where each node is a protein and an edge between nodes symbolizes an interaction 
between those two proteins. After visualizing such a graph, there are certain shapes that emerge (spelling). Given a protein-protein interactome (PPI) of *Drosophila (spelling)*, the objective 
of this project is to identify all triangles that contain one of the proteins in non-muscle myosin (NMII). Using 
an algorythm to find these triangles, I identified all triangles that contain one 
or both of the proteins in NMII. (say that I analyzed the type) I found that the most common type of triangle in 
this sample was _________.

#Motivation

describe nmii biological problem
Many algorithms have been implemented that analyze the structure in different ways. 
The motivation behind this project was to find start to explore whether the shapes 
created by nodes and edges have any biological significance. It could also prove to be 
a way of predicting what role currently unlabeled nodes play in NMII regulation.

#Methods

1.Graphs and the computational problem

include images here

2.Approaches you used
3.Datasets/Inputss
4.Output Types (a list of predictions? A GraphSpace graph? Etc.)

#Results
In one paragraph, summarize your findings

pie chart and sample nodes

graphspace link


1916 triangles in total

include thing in screenshots

| Type | Total | Percentage |
| ---- | ----- | ---------- |
| pos/pos/pos | 5 | 0.26|
| pos/pos/neg | 39 | 2 |
| pos/neg/neg | 71 | 3.71 |
| pos/pos/u | 77 | 4.02 |
| pos/u/u | 1174 | 61.27 |
| pos/neg/u | 550 | 28.71 |


#Discussion

In one paragraph, discuss how your findings (or anticipated findings) would
fit into the bigger biological problem/question.

# References
Figures/pictures can be very useful to describe graphs, the computational problem, and the
results. URLs to GraphSpace graphs are also useful.


ask them if they want me to link the girhub into their things

cite anna correctly on viz graph


wasn't possible to have these since we needed at least 1 nmii (listed as a positive)
there were 0 triangles of type neg_neg_neg_, which made up 0.0 of the triangles
there were 0 triangles of type neg_neg_u_, which made up 0.0 of the triangles
there were 0 triangles of type neg_u_u_, which made up 0.0 of the triangles
there were 0 triangles of type u_u_u_, which made up 0.0 of the triangles








different types of triangles

pos/pos/pos
pos/pos/neg
pos/pos/u
pos/neg/pos
pos/neg/neg
pos/neg/u
pos/u/pos
pos/u/ne
pos/u/u
neg/pos/neg
neg/pos/u
neg/neg/neg
neg/neg/u
neg/u/pos
neg/u/ng
neg/u/u
u/pos/neg
u/pos/u
u/neg/neg
u/neg/u
u/u/u

make pi chart?


maybe want to do 3 different graphs

### Citations

That is ok! Make sure you link to the original fly interactome GitHub url, and you can copy the tables of the GO terms from the NMII README.md file. Those are also public (from the Gene Ontology website)


# files included

example, get fly interactome, possibly ingrids pruning