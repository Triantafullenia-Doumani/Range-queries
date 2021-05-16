#TRIANTAFYLLENIA DOUMANI
# for example, you can run the program with: python3 Range_queries.py Rtree.txt Rqueries.txt

import sys

def main(argv):

    global Rtree_file
    global Rqueries
    global question
    global objects
    global output

    Rtree = open(argv[1], "r")
    Rqueries = open(argv[2], "r")
    output = open("RtreeSearch.txt","w")
    Rtree_file = []
    Rtree_line = Rtree.readline()
    question = 0
    objects = 0

    # read the Rtree.txt and store its value into a list
    while(Rtree_line):
        Rtree_line_update = Rtree_line.replace("[" , "").replace("]" , "").replace("\n" , "").split(",")
        Rtree_file.append(Rtree_line_update)
        Rtree_line = Rtree.readline()

    root_id = len(Rtree_file) - 1
    search(root_id)
    Rtree.close()
    Rqueries.close()
# read the Rqueries file and for each Window search into the Rtree for the objects(leafs) that intersect with it
def search(root_id):

    global id_list
    global objects

    w = Rqueries.readline().split()
    question = 0
    objects = 0

    while(w):

        id_list = []

        x_low_WIN = float(w[0])
        y_low_WIN = float(w[1])
        x_hight_WIN = float(w[2])
        y_hight_WIN = float(w[3])

        WIN = [x_low_WIN,x_hight_WIN,y_low_WIN,y_hight_WIN]

        find_object(WIN, int(root_id) )
        print_result(question , objects , id_list)
        w = Rqueries.readline().split()
        question += 1
        objects = 0

# find the objects that intersect with Window
def find_object(WIN, node_id ):

    global objects
    parent_node = Rtree_file[node_id]
    isleaf = parent_node[0]
    parent_id = parent_node[1]

    for i in range(2,len(parent_node) - 2 , 5):
        child_id = parent_node[i]
        x_low =  float(parent_node[i+1])
        y_low =  float(parent_node[i+2])
        x_hight =  float(parent_node[i+3])
        y_hight =  float(parent_node[i+4])
        MBR  = [x_low,y_low,x_hight,y_hight]

        if intersects(WIN ,MBR):
            if isleaf == '0' :
                id_list.append(int(child_id))
                objects+= 1
            else:
                find_object(WIN, int(child_id) )

# check if WIN has intersect with MBR
def intersects(WIN ,MBR):

        x_axis  = 0
        y_axis = 0

        if WIN[2] > MBR[3]:
        	y_axis = 1

        if  MBR[2] > WIN[3]:
            y_axis = 1

        if WIN[0] > MBR[1]:
        	x_axis = 1

        if  MBR[0] > WIN[1]:
            x_axis = 1

        if x_axis or y_axis:
            return False
        else:
            return True

def print_result(question , objects , id_list):

    output.write((str(question) + " ("+str(objects)+") : " + str(id_list).replace("[", "").replace("]","")+"\n") )

if __name__ == "__main__":
	main(sys.argv)
