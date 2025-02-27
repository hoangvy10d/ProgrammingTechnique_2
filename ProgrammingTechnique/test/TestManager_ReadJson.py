from ProgrammingTechnique.libs.JsonFileFactory import JsonFileFactory
from ProgrammingTechnique.models.Manager import Manager
from ProgrammingTechnique.test.TestManager_WriteJson import managers

jff=JsonFileFactory()
filename= "../dataset/managers.json"
assets=jff.read_data(filename,Manager)
print("Danh sách Manager:")
for m in managers:
    print(m)