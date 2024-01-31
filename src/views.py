from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import requests, json
from markupsafe import Markup

views = Blueprint(__name__, "views")

def get_datas_by_page(page=1):
    uri = f"https://rickandmortyapi.com/api/character?page={page}"
    response = requests.get(uri)
    if response.status_code == 200:
        data = json.loads(response.text)
        results = data
        return results

def get_datas_by_uri(uri):
    response = requests.get(uri)
    if response.status_code == 200:
        data = json.loads(response.text)
        results = data
        return results

@views.route("/")
def home():
    page = request.args.get('page', default=1, type=int)
    datas = get_datas_by_page(page)
    status = []

    for data in datas['results']:
        if str(data['status']).lower() == "alive":
            data['status'] += "/is-success"
        elif str(data['status']).lower() == "unknown":
            data['status'] += "/is-warning"
        elif str(data['status']).lower() == "dead":
            data['status'] += "/is-danger"

    return render_template("index.html", datas=datas, page=page)

@views.route("/profile/")
def profile():
    id = request.args.get('id', type=int)
    uri = request.args.get('uri', type=str)
    episodes = []
    episodesCount = 0

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
        

    for episode in character['episode']:
        episodes.append(Markup(f'<li class="hidden"> <p>Episode: {episode.split("/")[-1]}</p> </li>'))

    episodesCount = len(episodes)

    return render_template("profile.html", character=character, uri=uri, episodes=episodes, episodesCount=episodesCount)
