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
    
    if text[0] == '#Name' or text[0] == '#': del text[0:2] #removes column headers from text
                   
    edge_list = [] #initialize edge list, node list
    node_list = []                       
   
    for i in range(0, len(text), 2): #loops through each line of file
        new_edge = [text[i], text[i+1]] #selects both parts of edge
        #print(new_edge)
        
        #check for duplicates
        if (new_edge not in edge_list) and ([new_edge[1], new_edge[0]] not in edge_list):
            edge_list.append(new_edge)

        #add new nodes to node list
        node_list.append(new_edge[0]) 
        node_list.append(new_edge[1])
   
    node_list = list(set(node_list)) #remove duplicate nodes
    
    return node_list, edge_list

## author: Ananke Krishnan
# edited by Mikhail Ostrovsky for speed
#edge_to_adjacency
#input: edge list
#output: adjacency list (dictionary with nodes as keys and values as neighbors)
def edge_to_adj(edge_list):

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
        else:
            adjacency_list[i[1]].append(i[0])

    return(adjacency_list)

def remove_duplicates(all_triangles):
    
    # Set so that it's easier to look up
    already_seen = {}
    for triangle in all_triangles:
        all_permutations = {}
        for perm in all_permutations:
            if perm not in already_seen:
                already_seen += {perm}
    return list(already_seen)

def get_all_triangles(node_list, adj_list):
    all_triangles = []
    for node in node_list:
        all_triangles += get_triangles_for(node, adj_list)
    return all_triangles

### get master triangle dictionary
# uses all the triangles

def get_triangle_dictionary(all_triangles, pos_nodes, neg_nodes, all_keys):
    # Initialize an empty dictionary with all possible combinations of labels
    triangles_dict = {}
    for key in all_keys:
        triangles_dict[key] = []
    print(triangles_dict)
    print('\n')
    print('len triangles_dict = '+str(len(triangles_dict)))
    print('len all keys = '+str(len(all_keys)))
    assert(len(triangles_dict) == len(all_keys))
    for triangle in all_triangles:
        print('current triangle in get_triangle_dict = '+str(triangle))
        assert(len(triangle) == 3)
        key = get_key(get_tag(triangle, pos_nodes, neg_nodes))
        triangles_dict[key] += [triangle]
    return triangles_dict
        
#make sets to make easier
def get_triangles_for(node, adj_list):
    nodes_triangles = []
    for u in adj_list[node]:
        #print('u = '+str(u))
        for v in adj_list[node]:
            #print('v = '+str(v))
            if u in adj_list[v] and (v, u) not in nodes_triangles:
                #print(u, v)
                #print('\n')
                nodes_triangles += [(node, u, v)]
                #(?) not appending correctly
            #else: print("not triangle")
    return nodes_triangles

def get_node_label(node, pos_nodes, neg_nodes):
    if node in pos_nodes:
        label = 'pos'
    elif node in neg_nodes:
        label = 'neg'
    else:
        label = 'u'
        print('unlabeled node = '+str(node))
    return label

def get_tag(triangle, pos_nodes, neg_nodes):
    assert(len(triangle) == 3)
    tag = ''    
    for node in triangle:
        label = get_node_label(node, pos_nodes, neg_nodes)
        tag+= label +str('_')
    return get_key(tag)

def get_key(tag):
    
    # If all nodes are positive
    if tag == 'pos_pos_pos_':
        return tag
    
    # If two positive, one negative
    elif tag == 'pos_pos_neg_' or tag == 'pos_neg_pos_' or tag == 'neg_pos_pos_':
        return 'pos_pos_neg_'
     
    # If one positive, two negative
    elif tag == 'pos_neg_neg_' or tag == 'neg_neg_pos_' or tag == 'neg_pos_neg_':
        return 'pos_neg_neg_'
    
    # If all negative
    elif tag == 'neg_neg_neg_':
        return tag
        
    # If two positive, one unlabeled
    elif tag == 'pos_pos_u_' or tag == 'pos_u_pos_' or tag == 'u_pos_pos_':
        return 'pos_pos_u'
        
    # If one positive, two unlabeled
    elif tag == 'pos_u_u_' or tag == 'u_pos_u_' or tag == 'u_u_pos_':
        return 'pos_u_u_'
       
            
    # If two negative, one unlabeled
    elif tag == 'neg_neg_u_' or tag == 'neg_u_neg_' or tag == 'u_neg_neg_':
        return 'neg_neg_u_'
    
    # If one negative, two unlabeled
    elif tag == 'neg_u_u_' or tag == 'u_neg_u_' or tag == 'u_u_neg_':
        return 'neg_u_u_'
    
    # If all unlabeled
    elif tag == 'u_u_u_':
        return tag
    # If one of each
    elif tag == 'neg_pos_u_' or tag == 'neg_u_pos_' or tag == 'pos_u_neg_' or tag == 'pos_neg_u_' or tag == 'u_pos_neg_' or tag == 'u_neg_pos_':
        return 'neg_pos_u_'
    else: print('exception = ' +tag)

    return tag

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

def read_labeled_nodes_example():
    posneg_file = 'example_labels.txt'
    # initializing dictionary and lists
    node_info = {}
    labeled_nodes = []
    pos_nodes = []
    neg_nodes = []

    with open(posneg_file) as fin:
        for line in fin: # for each line
            n, pos_neg = line.strip().split() # separate the two items
            if n != "#Name": # if the line is not the header (in this case, the header starts with "#Name")
                if n not in labeled_nodes: # if the node is not a duplicate
                    labeled_nodes.append(n) # add it to the full node list
                    node_info[n] = [pos_neg] # add info to full node dictionary
                    if pos_neg == "Positive": # if the node is positive, add to positive list
                        pos_nodes.append(n)
                    elif pos_neg == "Negative": # if node is negative, add to negative list
                        neg_nodes.append(n)

    return node_info, labeled_nodes, pos_nodes, neg_nodes

