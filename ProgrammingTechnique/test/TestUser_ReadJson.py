from DoAnNhomCK.libs.JsonFileFactory import JsonFileFactory
from DoAnNhomCK.models.User import User
from DoAnNhomCK.test.TestUser_WriteJson import users

jff=JsonFileFactory()
filename= "../dataset/users.json"
assets=jff.read_data(filename,User)
print("Danh sách Manager:")
for u in users:
    print(u)