import networkx
import pydot  
from mapper import make_graph



class Networkx_graph:
	def __init__(self, path, library_name):
		self.png_path = "test.png"
		self.graph = make_graph(path, library_name)
		self.dot_graph = networkx.drawing.nx_pydot.to_pydot(self.graph)

	def set_graph_layout(self, **kargs):
	""" prepare output file argument for input into graphviz""" 
		shapes = ['box', 'polygon', 'ellipse', 'oval', 'circle', 'egg', 'triangle', 'exagon', 'star', ]
		colors = ['blue', 'black', 'red', '#db8625', 'green', 'gray', 'cyan', '#ed125b']
		styles = ['filled', 'rounded', 'rounded, filled', 'dashed', 'dotted, bold']

		for i, node in enumerate(self.dot_graph.get_nodes()):
		    node.set_label("n%d" % i)
		    node.set_shape(shapes[random.randrange(len(shapes))])
		    node.set_fontcolor(colors[random.randrange(len(colors))])
		    node.set_fillcolor(colors[random.randrange(len(colors))])
		    node.set_style(styles[random.randrange(len(styles))])
		    node.set_color(colors[random.randrange(len(colors))])

		for i, edge in enumerate(self.dot_graph.get_edges()):
		    edge.set_label("e%d" % i)
		    edge.set_fontcolor(colors[random.randrange(len(colors))])
		    edge.set_style(styles[random.randrange(len(styles))])
		    edge.set_color(colors[random.randrange(len(colors))])

		

	def write_png(self, png_name):
		"""send dot graph to graphviz and send output ot png file"""
		self.dot_graph.write_png(png_name)