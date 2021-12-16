# Identifying Triangles in Drosophila (spelling) Interactome

**Note for Anna:** This repository is complete but still private at the time that I am 
turning this in because I'd like to add more to it before making it public. When I 
make it public I will let you know!

#Abstract

There are several ways to visualize the interactions of proteins. One of them is to create a graph 
where each node is a protein and an edge between nodes symbolizes an interaction 
between those two proteins. After visualizing such a graph, there are certain shapes that emerge (spelling). Given a protein-protein interactome (PPI) of *Drosophila (spelling)*, the objective 
of this project is to identify all triangles that contain one of the proteins in non-muscle myosin (NMII). Using 
an algorythm to find these triangles, I identified all triangles that contain one 
or both of the proteins in NMII. The most frequent triangles that contained NMII 
were those with one positive and two unlabeled nodes, followed by triangles with one 
positive, one negative, and one unlabeled node.

#Motivation

One of the aims in compiling the *Drosophila* interactome is to better understand how 
NMII is regulated. Because there are so many proteins and protein-protein interactions, 
it is not feasible to experimentally validate the role of each invididual protein. 
By representing the data as a graph G with proteins as nodes V and intereactions as edges 
E, it becomes possible to use algorithms to predict which proteins would be most benificial to 
put time and resources into testing. This project aims to see whether the geometrical shapes in G 
have any biological relevance, which could inform the way that we make predictions for regulators 
in the future. 

#Methods

Using the dataset ______ by _____, go terms?????, we construct a graph *G* with a set of nodes *V* (proteins) and a set of edges *E*, 
the task is to find every triangle (set of three nodes) such that each node in the 
set is connected by an edge to both of the remaining nodes. For this project, we are 
only interested in the triangles that contain one or both of the proteins in NMII. 
The data used includes labels for some nodes that indicate its role in NMII regulation, 
if known. Proteins that are confirmed regulators of NMII are labeled `pos` while 
proteins that do not regulate NMII are labeled `neg`. If the protein is unlabeled, the corresponding node 
will be labeled as `u`. 

To find all such triangles, the program reads the file `flybase-interactome.txt` 
and generates *V*, *E*. An adjacency list is created from *E* and then the labeles of the proteins 
are read in from `labeled-nodes.txt`. `get_triangles_for()` is run on both nodes in NMII, 
which find every set of neighbors (*u*, *v*) in the neighbors of the node and checks to 
see if the edge `[*u*, *v*]` exists. If it does, then (*node*, *u*, *v*) is a triangle. 
Below is a toy graph where all the triangles have bolded edges:

![](images/example_graph.png)

*This graph may also be viewed ![here](http://graphspace.org/graphs/33194?user_layout=14638) on GraphSpace*

For the actual *Drosophila* interactome, there were 1916 triangles in total that had 
one or both of NMII protreins in their set, so only 25 triangles were vizualied:

![](images/sample_triangles.png)

*This graph may also be viewed ![here](http://graphspace.org/graphs/33193?auto_layout=cola#) on GraphSpace*

In addition to the GraphSpace graphs, the program also prints the percentages of triangles found for 
each possible combination of node labels. Below is a list of all possible combinations* and how they are 
represented in the program:

| Type | Significance | Representation in code |
| ---- | ----- | ---------- |
| pos/pos/pos | All positive labels | `pos_pos_pos_`|
| pos/pos/neg | Two positive labels, one negative label | `pos_pos_neg_` |
| pos/neg/neg | One positive label, two negative labels | `pos_neg_neg_` |
| pos/pos/u | Two positive labels, one  unlabeled node| `pos_pos_u_` |
| pos/u/u | One positive label, two unlabeled nodes | `pos_u_u_` |
| pos/neg/u | One positive label, one negative label, and one unlabeled node | `pos_neg_u_` |

**Note that combinations without any positives are not included because both NMII proteins are 
labeled `pos`, therefore all triangle sets much have at least one `pos` node because the program 
only finds triangles with NMII.*


To run the code, you must use a version of Python that supports the ![GraphSpace Python Client](http://manual.graphspace.org/projects/graphspace-python/en/latest/) 
From there, type `main.py` to run the program on the *Drosophila* interactome or 
`example.py` to generate the example graph. The program will prompt you to put in an 
email address and password associated with your GraphSpace account. After generating 
the graph, it will print the percentages of each type of triange found to the screen.

#Results

The program produced 1916 triangles in total that contained NMII. Below are is a 
breakdown of the frequency of each type of triangle:

| Type | Total | Percentage |
| ---- | ----- | ---------- |
| pos/pos/pos | 5 | 0.26|
| pos/pos/neg | 39 | 2 |
| pos/neg/neg | 71 | 3.71 |
| pos/pos/u | 77 | 4.02 |
| pos/u/u | 1174 | 61.27 |
| pos/neg/u | 550 | 28.71 |

![](images/results.png)

Of the 1916 triangles, the most commonly occuring type were those with one positive node 
and two unlabeled nodes. The next most commonly ocurring type were those with one positive, one negative, 
and one unknown label. This means that it was more likely for a NMII protein to 
participate in triangles with one negative and one unlabeled node, or two unlabeled nodes.

#Discussion

In one paragraph, discuss how your findings (or anticipated findings) would
fit into the bigger biological problem/question.

# References

ask them if they want me to link the girhub into their things

cite anna correctly on viz graph

That is ok! Make sure you link to the original fly interactome 
GitHub url, and you can copy the tables of the GO terms from the NMII README.md file. 
Those are also public (from the Gene Ontology website)
