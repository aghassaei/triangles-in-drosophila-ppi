## All utilities
# utilities for the thing

## author: Ananke
## NOTE: Edited from Aliya's read_ppi function above!
################
## INPUTS: file name as a string 
## To test: use '../../inputs/test-fly-interactome.txt'
## To run: use '../../inputs/flybase-interactome.txt'
## must call this from within your own directory
## RETURNS:
## edge_list: a list of edges (as lists)
## node_list: a list of nodes (as strings)
## edge_dictionary: a dictionary with edges (keys) and edge weights as lists (values)

## Edited to try and decrease runtime
# It seems to be working on the flybase_interactome file and I was able to verify its accuracy using the test file

################

def read_in(filename):
    file = open(filename, 'r')      #open file, store contents in variable text, close file
    text = file.read()
    file.close()
    text = text.split()
    
    del text[0:8] #removes column headers from text
                   
    edge_list = [] #initialize edge list, node list
    node_list = []                       
   
    for i in range(0, len(text), 8): #loops through each line of file
        new_edge = [text[i], text[i+1]] #selects both parts of edge
        
        #check for duplicates
        if (new_edge not in edge_list) and ([new_edge[1], new_edge[0]] not in edge_list):
            edge_list.append(new_edge)
        
        #add new nodes to node list
        node_list.append(new_edge[0]) 
        node_list.append(new_edge[1])
   
    node_list = list(set(node_list)) #remove duplicate nodes
    
    return node_list, edge_list
