from cloudev.entityLoader import EntityLoader

__version__ = "0.1"


EntityLoader.load("aws", globals())
#EntityLoader.load("azure", globals())
#EntityLoader.load("k8s", globals())

#print(globals())