import networkx
import pydot  
from graph import Networkx_graph

import argparse
from .arguments import Arguments
import os
import sys



def parse_args():
    """Parse command line arguments, and return a dict.
    """
    args = argparse.ArgumentParser()

    args.add_argument('-v', '--verbose', default=0, action='count', help="be more verbose (-vv, -vvv for more verbosity)")
    args.add_argument('-s', '--shape', default='oval', help="display nodes in specified shape:'box', 'polygon', 'ellipse', 'oval', 'circle', 'egg', 'triangle', 'exagon', 'star'")
    args.add_argument('-nc', '--ncolor', default='blue', help="display nodes in specified color:'blue', 'black', 'red', '#db8625', 'green', 'gray', 'cyan', '#ed125b'")
    args.add_argument('-ec', '--ecolor', default='red', help="display edges in specified color: 'blue', 'black', 'red', '#db8625', 'green', 'gray', 'cyan', '#ed125b'")
    args.add_argument('-o', default=None, kind="FNAME:output", dest='output', metavar="file", help="write output to 'file'")
    args.add_argument('--display', kind="FNAME:exe", default=None, help="program to use to display the graph (png or svg file depending on the T parameter)", metavar="PROGRAM")
    args.add_argument('--noshow', '--no-show', action='store_true', default=False, dest='no_show', help="don't call external program to display graph")
    args.add_argument('--reverse', action='store_true', help="draw arrows to (instead of from) imported modules")
    args.add_argument('--rankdir', default='TB', type=str, choices=['TB', 'BT', 'LR', 'RL'], help="set the direction of the graph, legal values are TB (default, imported modules above importing modules), "
                                                                                         "BT (opposite direction of TB), BT (opposite direction of TB), LR (left-to-right) and RL (right-to-left)")
    _args = args.parse_args(argv)


    return vars(_args)




path = "C:\\Users\\abreham\\Desktop\\Django_projects\\asynchronous"
library_name = "asynchronous"
# path = "C:\\Users\\abreham\\Desktop\\Environment\\django_environment\\Lib\\site-packages\\django"
# library_name = "django"

print(parse_args())


# networkx_graph = Networkx_graph(path, library_name)
# dot_graph.write_png("asynchronous.png")