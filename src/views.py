from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import requests, json
from markupsafe import Markup

views = Blueprint(__name__, "views")

#Get the API but only the requested page of it
def get_datas_by_page(page=1):
    uri = f"https://rickandmortyapi.com/api/character?page={page}"
    response = requests.get(uri)
    if response.status_code == 200:
        data = json.loads(response.text)
        results = data
        return results

#Get the data from API with a dedicated url
def get_datas_by_uri(uri):
    response = requests.get(uri)
    if response.status_code == 200:
        data = json.loads(response.text)
        results = data
        return results

#Creates the rendering of the main/home page
@views.route("/")
def home():
    page = request.args.get('page', default=1, type=int)
    datas = get_datas_by_page(page) #Get the api and store it in datas

    #Check the status of the characters and add the corresponding css class to the status to use it on the page
    #For instance - if status == alive then in the html the alive text will be green
    for data in datas['results']:
        if str(data['status']).lower() == "alive":
            data['status'] += "/is-success"
        elif str(data['status']).lower() == "unknown":
            data['status'] += "/is-warning"
        elif str(data['status']).lower() == "dead":
            data['status'] += "/is-danger"

    return render_template("index.html", datas=datas, page=page) #Renders the index.html with 2 parameters: datas and page


#Creates the rendering of the profile page
@views.route("/profile/")
def profile():
    id = request.args.get('id', type=int) #When the profile page is called to be rendered then it collects the id parameter
    uri = request.args.get('uri', type=str) #
    episodes = []
    episodesCount = 0

    #Check the current page number to have a maximum 42 pages because thats the max the api has
    if uri is None:
        uri = "https://rickandmortyapi.com/api/character?page=42"
    else:    
        page = int(uri[-1])
        page -= 1
        uri = uri[:-1] + str(page)

    datas = get_datas_by_uri(uri)
    character = dict()

    for item in datas['results']:
        if int(item['id']) == id:
            character = item

    #Checks the character's status (alive, dead, unknown) for the appropriate styling
    for i in character:
        if character['status'].lower() == "alive":
            character['status'] += "/is-success"
        
    #Adds the episodes the selected character is in to an episodes list which is then rendered at the page with the also added markup (html)
    for episode in character['episode']:
        episodes.append(Markup(f'<li class="hidden"> <p>Episode: {episode.split("/")[-1]}</p> </li>'))

    episodesCount = len(episodes)

    return render_template("profile.html", character=character, uri=uri, episodes=episodes, episodesCount=episodesCount)
