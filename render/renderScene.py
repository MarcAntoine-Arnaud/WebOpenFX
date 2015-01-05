import logging
from pyTuttle import tuttle

class RenderScence:
	def __init__(self):
		tuttle.core().preload(False)
		self.project = None
		self.graph = tuttle.Graph()
		self.nodes = []

	def setProject(self, project, outputFilename):
		self.project = project
		try:
			for node in project['nodes']:
				tuttleNode = self.graph.createNode(str(node['plugin']))
				self.nodes.append(tuttleNode)

			for connection in project['connections']:
				self.graph.connect( [self.nodes[connection['src']], self.nodes[connection['dst']]] )

			outputFilenameParameter = self.nodes[len(self.nodes)-1].getParam("filename")
			outputFilenameParameter.setValue( outputFilename )

		except Exception as e:
			logging.info("Error in setup of the project: " + str(e))

	def render(self):
		try:
			self.graph.compute( self.nodes[len(self.nodes)-1] )
		except Exception as e:
			logging.info("Error in render: " + str(e))