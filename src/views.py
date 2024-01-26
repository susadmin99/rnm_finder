from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import requests, json

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

    return render_template("index.html", datas=datas, page=page)

@views.route("/profile/")
def profile():
    name = request.args.get('name', type=str)
    uri = request.args.get('uri', type=str)
    if uri is None:
        uri = "https://rickandmortyapi.com/api/character?page=42"
    else:    
        page = int(uri[-1])
        page -= 1
        uri = uri[:-1] + str(page)
    datas = get_datas_by_uri(uri)
    character = dict()
    for item in datas['results']:
        if item['name'] == name:
            character = item

    return render_template("profile.html", character=character)
