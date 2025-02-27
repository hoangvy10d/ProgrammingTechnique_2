from libs.JsonFileFactory import JsonFileFactory


class DataConnector:
    def get_all_fanfic(self):
        jff = JsonFileFactory()
        filename = "../dataset/Fanfic.json"
        Fanfic=jff.read_data(filename,Fanfic)
        return Fanfic
    def get_all_user(self):
        jff = JsonFileFactory()
        filename = "../dataset/assets.json"
        assets = jff.read_data(filename, Asset)
        return assets
    def get_all_manager(self):
        jff = JsonFileFactory()
        filename = "../dataset/employee_assets.json"
        eas = jff.read_data(filename, Employee_Asset)
        return eas

    def login(self,username,password):
        employees=self.get_all_employees()
        for e in employees:
            if e.UserName==username and e.Password==password:
                return e
        return None