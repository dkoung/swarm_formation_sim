# This simulation tests the probabilistic convergence algorithm (a collective decision
# making algorithm) on randomly generated 2D honeycomb network. The algorithm is extracted
# from previous loop reshape simulations, for further testing if it can be generally used
# on 2D random network topologies.

import math, sys, os, getopt
import matplotlib.pyplot as plt
from network_generator_2D_swarm import *

net_size = 0  # size of the honeycomb network
net_folder = 'honeycomb-networks'  # folder for all network files
net_filename = '30-1'  # defautl filename of the network file, if no input
net_filepath = os.path.join(os.getcwd(), net_folder, net_filename)  # corresponding filepath

# read command line options
try:
    opts, args = getopt.getopt(sys.argv[1:], 'f:')
    # The colon after 'f' means '-f' requires an argument, it will raise an error if no
    # argument followed by '-f'. But if '-f' is not even in the arguments, this won't raise
    # an error. So it's necessary to define the default network filename
except getopt.GetoptError as err:
    print str(err)
    sys.exit()
for opt,arg in opts:
    if opt == '-f':
        net_filename = arg
        # check if this file exists
        net_filepath = os.path.join(os.getcwd(), net_folder, net_filename)
        if not os.path.isfile(net_filepath):
            print "{} does not exist".format(net_filename)
            sys.exit()
        # parse the network size
        net_size = int(net_filename.split('-')[0])  # the number before first dash

# read the network from file
nodes = []
f = open(net_filepath, 'r')
new_line = f.readline()
while len(new_line) != 0:  # not the end of the file yet
    pos_str = new_line[0:-1].split(' ')  # get rid of '\n' at end
    pos = [int(pos_str[0]), int(pos_str[1])]  # convert to integers
    nodes.append(pos)
    new_line = f.readline()

# generate the connection variable, 0 for not connected, 1 for connected
connections = [[0 for j in range(size)] for i in range(size)]  # populated with zeros
for i in range(size):
    for j in range(i+1, size):
        # find if nodes[i] and nodes[j] are neighbors
        diff_x = nodes_t[i][0] - nodes_t[j][0]
        diff_y = nodes_t[i][1] - nodes_t[j][1]
        if abs(diff_x) + abs(diff_y) == 1 or diff_x * diff_y == -1:
            # condition 1: one of the axis value difference is 1, the other is 0
            # condition 2: one of the axis value difference is 1, the other is -1
            connections[i][j] = 1
            connections[j][i] = 1

# plot the network as dots and lines


