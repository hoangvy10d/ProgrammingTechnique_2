from libs.JsonFileFactory import JsonFileFactory
from models.Film import Film

jff=JsonFileFactory()
filename="../dataset/viet_review.json"
review_films=jff.read_data(filename,Film)
print("list of reviews from json:")
for p in review_films:
    print(p)