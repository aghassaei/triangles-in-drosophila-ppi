"""
Utility file for all community functions.
Add your name to the functions you write.
Note: there is no main function, but you can import modules here.
"""
from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph
import time
import csv

## author: Ananke Krishnan
# edited by Mikhail Ostrovsky for speed
#edge_to_adjacency
#input: edge list
#output: adjacency list (dictionary with nodes as keys and values as neighbors)
def edge_to_adjacency(edge_list):

    adjacency_list = {}
    
    for i in edge_list: #loops through every edge (list of 2 nodes)
        #for node 1 of the edge
        if i[0] not in adjacency_list: #if it is not already present in the adj list add it
            adjacency_list[i[0]] = []
            adjacency_list[i[0]].append(i[1])
        else: #add to both each node to both nodes in list because there is a new connection
            adjacency_list[i[0]].append(i[1])
        #for node 2 of the edge
        if i[1] not in adjacency_list:  #if it is not already present in the adj list add it
            adjacency_list[i[1]] = []
            adjacency_list[i[1]].append(i[0])
        else:  #otherwise
            adjacency_list[i[1]].append(i[0])

    return(adjacency_list)


# author: ingrid zoll
# input: none. it automatically gets the labeled nodes file when it is run
# outputs: has 4 different outputs
## node_info: dictionary, with format {node: [id, pos_neg, annotation], etc}
## labeled_nodes: list of all nodes in the labeled-nodes file
## pos_nodes and neg_nodes: lists of positive and negative labeled nodes, respectively.
# code to run: node_info, labeled_nodes, pos_nodes, neg_nodes = utils.read_labeled_nodes()
# NOTE: MUST BE RUN IN YOUR OWN DIRECTORY.
def read_labeled_nodes():
    posneg_file = '../../inputs/labeled-nodes.txt'
    # initializing dictionary and lists
    node_info = {}
    labeled_nodes = []
    pos_nodes = []
    neg_nodes = []

    with open(posneg_file) as fin:
        for line in fin: # for each line
            n, ID, pos_neg, annotation = line.strip().split() # separate the four items
            if n != "#Name": # if the line is not the header (in this case, the header starts with "#Name")
                if n not in labeled_nodes: # if the node is not a duplicate
                    labeled_nodes.append(n) # add it to the full node list
                    node_info[n] = [ID, pos_neg, annotation] # add info to full node dictionary
                    if pos_neg == "Positive": # if the node is positive, add to positive list
                        pos_nodes.append(n)
                    elif pos_neg == "Negative": # if node is negative, add to negative list
                        neg_nodes.append(n)

    return node_info, labeled_nodes, pos_nodes, neg_nodes


# author: ingrid zoll
# input: none. it automatically gets the file when it is run
# outputs: has 3 outputs
## prev_nodes: dictionary, with format {node: [id, status, years], etc}
## nodes: list of all nodes in the file
## status_type: dictionary, with keys = status, values = list of nodes with that status.
# status: 0 = Never was a hit
# 1 = Had one hit in class
# 2 = Had two hits (in class or in summer)
# 3 = Had one hit but not a second hit
# NOTE: MUST BE RUN IN YOUR OWN DIRECTORY.
def read_prev_predictions():
    pred_file = '../../inputs/previous-preds.txt'
    # initializing dictionary and lists
    prev_nodes = {}
    nodes = []

    with open(pred_file) as fin:
        for line in fin: # for each line
            n, ID, status, years = line.strip().split() # separate the four items
            if n != "#Name": # if the line is not the header (in this case, the header starts with "#Name")
                if n not in nodes: # if the node is not a duplicate
                    nodes.append(n) # add it to the full node list
                    prev_nodes[n] = [ID, status, years] # add info to full node dictionary

    status_type = {}
    stat_list = ["0", "1", "2", "3"]

    for j in stat_list: # for each status type
        list_type = []
        for i in prev_nodes:
            status = prev_nodes[i][1]
            if status == j:
                list_type.append(i) # add all nodes with that status to a list
        status_type[j] = list_type # add list to dictionary

    return prev_nodes, nodes, status_type


## author: Aliya
## NOTE: Running read_ppi on the entire interactome took me 1 hour
################
## INPUTS: file name as a string 
## To test: use '../../inputs/test-fly-interactome.txt'
## To run: use '../../inputs/flybase-interactome.txt'
## must call this from within your own directory
## RETURNS:
## edge_list: a list of edges (as lists)
## node_list: a list of nodes (as strings)
## edge_dictionary: a dictionary with edges (keys) and edge weights as lists (values)
## If you want more information about the edges in edge_dictionary, just change 
## the row index in line 98 to get the rest of the collumns.
################

def read_ppi(filename):
    file = open(filename, 'r')      #open file, store contents in variable text, close file  
    text = file.read() 
    file.close()
    text = text.strip()             #format to remove white space, line breaks, headers
    text = text.split('\n')         
    text.pop(0)                     
    edge_list = []                  #initialize edge list, node list, and edge_dictionary
    node_list = []                 
    edge_dictionary = {}            
    for i in range(len(text)): 
        #print(i)
        row = text[i].split('\t')
        new_edge = row[:2]          #isolate the next edge
        
        #check to make sure edge and reverse aren't in edge_pairs before adding it
        edge_is_new = (new_edge not in edge_list)
        reverse_is_new = ([new_edge[1], new_edge[0]] not in edge_list)
        if edge_is_new and reverse_is_new: #if True, add edge to list and dictionary
            edge_list += [new_edge] #add new edge
            edge_dictionary[tuple(new_edge)] = [row[2]] 
        
        #add new nodes to node list
        node_list += [new_edge[0]] 
        node_list += [new_edge[1]]
   
    node_list = list(set(node_list)) #remove duplicate nodes
    return edge_list, node_list, edge_dictionary

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

def read_ppi_edited(filename):
    file = open(filename, 'r')      #open file, store contents in variable text, close file
    text = file.read()
    file.close()
    text = text.split()
    
    del text[0:8] #removes column headers from text
                   
    edge_list = [] #initialize edge list, node list, and edge_dictionary
    node_list = []                 
    edge_dictionary = {}            
   
    for i in range(0, len(text), 8): #loops through each line of file
        new_edge = [text[i], text[i+1]] #selects both parts of edge
        
        #check for duplicates
        if (tuple(new_edge) not in edge_dictionary.keys()) and (tuple([new_edge[1], new_edge[0]]) not in edge_dictionary.keys()):
            edge_list.append(new_edge)
            edge_dictionary[tuple(new_edge)] = float(text[i+2])
        
        #add new nodes to node list
        node_list.append(new_edge[0]) 
        node_list.append(new_edge[1])
   
    node_list = list(set(node_list)) #remove duplicate nodes
    
    return node_list, edge_list, edge_dictionary

## author: Jon deVries
##  nodlist: is a list of the nodes you predict to be positive. It 
## would be ideal if they were in the format symbol1_symbol2
##
## ranked: is a string. Either 'ranked' or 'unranked' 
##
## firstname: is your first name
##
## num: is the number corresponding to the input list of nodes. It should be
## a value from '1' to '4'
##
## identifier: if you are producing multiple list of candidate nodes, please
## distinguish them with some string in the 'identifier' slot. Otherwise, please 
## simply input an empty string, eg. ""

def list_to_csv(nodlist, ranked, firstname, num, identifier):
    with open(str(ranked + '_' + firstname + '_' + str(num) + '_' + identifier + '.csv'),'w') as outfile:
        writer = csv.writer(outfile)
        for row in nodlist:
            writer.writerow([row])

    return

## author: Anna Ritz
## Posts the graph G to GraphSpace and shares it with the group.
## Prompts the user for graph name, email, and password.
## param G: GSGraph object
## param post_group: share with the group (default True).
##  (note: you can prevent sharing by specifying post_group=False)

def post_to_graphspace(G,post_group=True):
    ## connect to the GraphSpace client.
    group='BIO331F21'
    graph_name = input('Enter Graph Name:')
    G.set_name(graph_name)
    email = input('Enter Email:')
    password = input('Enter Password:')
    gs = GraphSpace(email,password)
    print('GraphSpace successfully connected.')

    try: ## If graph does not yet exist...
        graph = gs.post_graph(G)
        if post_group:
            gs.share_graph(graph=graph,group_name=group)
    except: ## Otherwise, graph exists.
        print('Graph exists! Removing and re-posting (takes a few secs)...')
        graph = gs.get_graph(graph_name=graph_name)
        gs.delete_graph(graph=graph)
        time.sleep(1) # pause for 1 second
        graph = gs.post_graph(G)
        if post_group:
            gs.share_graph(graph=graph,group_name=group)
    print('Done!')
    return


## Returns the hexadecimal color code when given three channels
## for red, green, and blue between 0 and 1.  Copied from Anna's Lab 3 utils.
## Author: Anna Ritz
def rgb_to_hex(red,green,blue): # pass in three values between 0 and 1
  maxHexValue= 255  ## max two-digit hex value (0-indexed)
  r = int(red*maxHexValue)    ## rescale red
  g = int(green*maxHexValue)  ## rescale green
  b = int(blue*maxHexValue)   ## rescale blue
  RR = format(r,'02x') ## two-digit hex representation
  GG = format(g,'02x') ## two-digit hex representation
  BB = format(b,'02x') ## two-digit hex representation
  return '#'+RR+GG+BB
