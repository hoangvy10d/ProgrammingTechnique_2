from ProgrammingTechnique.libs.JsonFileFactory import JsonFileFactory
from ProgrammingTechnique.models.User import User
from ProgrammingTechnique.test.TestUser_WriteJson import users

jff=JsonFileFactory()
filename= "../dataset/users.json"
assets=jff.read_data(filename,User)
print("Danh sách Manager:")
for u in users:
    print(u)