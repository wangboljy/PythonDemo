import os, sys

rootPath = os.path.abspath("..")
sys.path.append(rootPath)

from pets import *

pet = Hound("killer")
pet.makesound()

pet = Shepherd("luna")
pet.makesound()

'''
#will error due to __all__
pet = Pet("DT", "dog")
pet.makesound()

'''
