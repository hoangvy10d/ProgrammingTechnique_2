from DoAnNhomCK.libs.JsonFileFactory import JsonFileFactory
from DoAnNhomCK.models.Manager import Manager
from DoAnNhomCK.test.TestManager_WriteJson import managers

jff=JsonFileFactory()
filename="../dataset/managers.json"
assets=jff.read_data(filename,Manager)
print("Danh sách caác quản lí:")
for m in managers:
    print(m)