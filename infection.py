from total_infection import total_infection
from limited_infection import limited_infection
from exact_infection import exact_infection
from graph import Graph
from user import User

import argparse
import networkx as nx
import matplotlib.pyplot as plt
import sys
import ntpath

__title__ = 'Infections'
__version__ = '1.0'
__author__ = 'Eric Li'

def createGraph(file):
    """
    Creates a graph from a given input csv file. Returns the graph object if
    valid file. Errors out if invalid.
    """

    graph = Graph()

    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(',')

            # Ensures input file is only three entries per line
            if len(line) != 3:
                print "Input file corrupted!"
                sys.exit(1)

            graph.addEdge(str(line[0]),str(line[1]), str(line[2]))

    return graph

def visualize(list, infected):
        """
        Uses networkx and matplotlib to visualize the infected graph. Blue
        indicates user hasn't been infected, green means that it has.
        """
        g = nx.read_weighted_edgelist(list, delimiter=',')
        plt.figure(figsize=(10,10))

        rawInfected = set()

        for user in infected:
            rawInfected.add(user.id)

        pos=nx.spring_layout(g)
        nx.draw(g, pos, node_color = 'b',node_size= 25, with_labels = True)
        nx.draw_networkx_nodes(g, pos, nodelist = rawInfected, node_size = 50, node_color = 'g')


        # saves specific filenames
        path = ntpath.basename(list)
        fn = path.split('.')

        output = "{}/{}_infected.png".format(ntpath.dirname(list),fn[0])
        plt.savefig(output)
        plt.show()

if __name__ == '__main__':
    """
    Runner for infections. Accepts two arguments: a data file and an optional
    --vis VIS argument that performs visualization of the final graph. Users
    can select the initial point of infection as well as perform several
    threshold filters. The program produces a png file with format
    infected_output.png and also outputs a list of all infected.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("data", help="csv file containing edges plus weights")
    parser.add_argument("-v","--vis", action="store_true", help="visualizes the infection and produces an image of final infection")
    args = parser.parse_args()


    graph = createGraph(args.data)
    users = graph.getUsers()

    if len(users) == 0:
        print "Input file is empty!"
        sys.exit(1)

    # Picker
    types = ["total", "limited", "exact"]

    infectionType = raw_input("Select type of infection (total, limited, exact): ")
    while infectionType not in types:
        infectionType = raw_input("Invalid selection. Select from (total, limited, exact): ")

    if infectionType == "total":
        print "\n=== Total Infection ==="
        print "Users: ", users
        initialUser = raw_input("Initial user to infect: ")
        while initialUser not in users:
            print "Invalid User. Please one of the following users: ", users
            initialUser = raw_input("Initial user to infect: ")

        infected = total_infection(graph, initialUser)

    elif infectionType == "limited":
        print "\n=== Limited Infection ==="
        print "Users: ", users
        initialUser = raw_input("Initial user to infect: ")
        while initialUser not in users:
            print "Invalid User. Please one of the following users: ", users
            initialUser = raw_input("Initial user to infect: ")

        numInfect = raw_input("Number of users to infect: ")
        threshold = raw_input("Base threshold: ")
        infected = limited_infection(graph, initialUser, int(numInfect), int(threshold))
    else:
        print "\n=== Exact Infection ==="
        print "Users: ", users
        initialUser = raw_input("Initial user to infect: ")
        while initialUser not in users:
            print "Invalid User. Please one of the following users: ", users
            initialUser = raw_input("Initial user to infect: ")

        numInfect = raw_input("Number of users to infect: ")
        threshold = raw_input("Base threshold: ")
        infected = exact_infection(graph, initialUser, int(numInfect), int(threshold))

    # Post stuff
    if infected:

        print "\n=== Infected =="
        for user in infected:
            print str(user)

        print "Total Infected: " + str(len(infected))

        if args.vis:
            visualize(args.data, infected)

    else:
        print "\nNo valid infections"
