from ProgrammingTechnique.libs.JsonFileFactory import JsonFileFactory
from ProgrammingTechnique.models.Fanfic import Fanfic

jff=JsonFileFactory()
filename="../dataset/fanfic.json"
fanfic=jff.read_data(filename,Fanfic)
print("List of Fanfics:")
for f in fanfic:
    print(f)