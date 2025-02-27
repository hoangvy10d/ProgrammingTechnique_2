from libs.JsonFileFactory import JsonFileFactory
from models.Fanfic import Fanfic


fanfic=[]

fanfic.append(Fanfic("Stranger Things", "Eleven, Mike, Dustin", '06/12/2016', 'The Mystery', 'https://netflix.com'))
fanfic.append(Fanfic("The Witcher", "Geralt, Yennefer, Ciri", '20/12/2019', 'Andrzej Sapkowski', 'https://netflix.com'))
fanfic.append(Fanfic("Attack on Titan", "Eren, Mikasa, Armin", '07/04/2013', 'Hajime Isayama', 'https://crunchyroll.com'))
fanfic.append(Fanfic("Demon Slayer", "Tanjiro, Nezuko, Zenitsu", '06/04/2019', 'Koyoharu Gotouge', 'https://funimation.com'))
fanfic.append(Fanfic("Breaking Bad", "Walter, Jesse, Saul", '20/01/2008', 'Vince Gilligan', 'https://amc.com'))

print("List of fanfics")
for f in fanfic:
    print(f)
jff=JsonFileFactory()
filename="../dataset/fanfic.json"
jff.write_data(fanfic,filename)
