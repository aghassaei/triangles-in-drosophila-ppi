# Identifying Triangles in Drosophila (spelling) Interactome

#Abstract

There are several ways to visualize the interactions of proteins. One of them is to create a graph 
where each node is a protein and an edge between nodes symbolizes an interaction 
between those two proteins. After visualizing such a graph, there are certain shapes that emerge (spelling). Given a protein-protein interactome (PPI) of *Drosophila (spelling)*, the objective 
of this project is to identify all triangles that contain one of the proteins in non-muscle myosin (NMII). Using 
an algorythm to find these triangles, I identified all triangles that contain one 
or both of the proteins in NMII. I found that 

In a few sentences, describe the purpose of the project, the approach, and
the results. This should summarize the whole project.
Motivation In a few sentences, describe the biological problem, and why a computa-
tional approach may be useful.
Methods Include a concise description of
1.Graphs and the computational problem
2.Approaches you used
3.Datasets/Inputss
4.Output Types (a list of predictions? A GraphSpace graph? Etc.)
Results In one paragraph, summarize your findings
Discussion In one paragraph, discuss how your findings (or anticipated findings) would
fit into the bigger biological problem/question.
References List of references you used.
Figures/pictures can be very useful to describe graphs, the computational problem, and the
results. URLs to GraphSpace graphs are also useful.


ask them if they want me to link the girhub into their things

cite anna correctly on viz graph

# plan

make toy graph to answer question: how do i want to figure out what/how many triangles 
a given node is a part of

change percentages later

put in ascending order

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