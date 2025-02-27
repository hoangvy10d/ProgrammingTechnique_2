from ProgrammingTechnique.libs.JsonFileFactory import JsonFileFactory


class DataConnector:
    def get_all_fanfic(self):
        jff = JsonFileFactory()
        filename = "../dataset/Fanfic.json"
        Fanfic=jff.read_data(filename,)
        return Fanfic
    def get_all_user(self):
        jff = JsonFileFactory()
        filename = "../dataset/assets.json"
        assets = jff.read_data(filename, )
        return assets
    def get_all_manager(self):
        jff = JsonFileFactory()
        filename = "../dataset/employee_assets.json"
        eas = jff.read_data(filename, )
        return eas

    def loginUSER(self,username,password):
        users=self.get_all_user()
        for u in users:
            if u.UserName==username and u.Password==password:
                return u
        return None
    def loginUSER(self,username,password):
        users=self.get_all_user()
        for u in users:
            if u.UserName==username and u.Password==password:
                return u
        return None
