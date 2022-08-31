
PyImports
-----
Python import dependency visualizer to aid in understanding module architecture 



Requirements
-----

* GraphViz(stand alone application that needs to be downloaded separately)
* networkx
* pydot



Usage
-----

```
python pyImports.py [-h] [-v] [-o file] [--display PROGRAM]
                    [--noshow] [--reverse] [--rankdir {TB,BT,LR,RL}]
                    library_path library_name





positional arguments:
  library_path                 system path for where the inteded library is located
  library_name                 name of library
  
  

optional arguments:
  -h, --help                             show this help message and exit
  -s, --shape                            display nodes in specified shape:'box', 'polygon', 'ellipse', 'oval', 'circle', 'egg', 'triangle', 'exagon', 'star'")
  -st, --style                           display edges in specified style:'filled', 'rounded', 'dashed', 'dotted', 'bold'
  -nc, --ncolor                          display nodes in specified color:'blue', 'black', 'red', '#db8625', 'green', 'gray', 'cyan', '#ed125b'
  -ec, --ecolor                          display edges in specified color: 'blue', 'black', 'red', '#db8625', 'green', 'gray', 'cyan', '#ed125b'
  -o                                     write output to 'file'
  --display                              program to use to display the graph
  --noshow, --no-show                    don't call external program to display graph
  --reverse'                             draw arrows to (instead of from) imported modules
  --rankdir                              set the direction of the graph, choices= TB (default, imported modules above importing modules), BT (opposite direction of TB)                                          LR (left-to-right) and RL (right-to-left)")
  
```

TODO
-----

* make package more self contained by implementing a limited graphics library to replace graphviz

* check and include import dependencies written in other languages



