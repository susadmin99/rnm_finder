import requests
from io import BytesIO
from PIL import Image
import json



def get_datas(page=1):
    uri = f"https://rickandmortyapi.com/api/character?page={page}"
    response = requests.get(uri)
    if response.status_code == 200:
        data = json.loads(response.text)
        results = data
        return results

def get_avatars(pageNumber):
    avatars = []
    results = get_datas(pageNumber)

    for i in results:
        avatars.append(i["image"])

    return avatars

def get_names(pageNumber):
    avatars = []
    results = get_datas(pageNumber)
    
    for i in results:
        avatars.append(i["name"])

    return avatars

def get_species(pageNumber):
    avatars = []
    results = get_datas(pageNumber)
    
    for i in results:
        avatars.append(i["species"])

    return avatars

def get_status(pageNumber):
    avatars = []
    results = get_datas(pageNumber)
    
    for i in results:
        avatars.append(i["status"])

    return avatars


    

