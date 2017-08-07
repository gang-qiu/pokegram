from chalice import Chalice, Response
import pokemon
import json

app = Chalice(app_name='pokegram')
app.debug = True

@app.route('/favicon.ico')
def favicon():
    return Response(body="favicon", headers={"Content-Type": "text/plain"}, status_code=200)

@app.route('/')
def health():
    return Response(body="API OK", headers={"Content-Type": "text/plain"}, status_code=200)

@app.route('/api/pokemon')
def index():
    # fetches data related to 
    pokemon_collection = pokemon.fetch_all_pokemon()
    return json.dumps(pokemon_collection)

@app.route('/api/picture')
def index():
    # fetches data related to 
    pokemon_collection = pokemon.fetch_all_pokemon()
    return json.dumps(pokemon_collection)

@app.route('/pokemon')
def upload():
    # fetches data related to 
    html = open("index.html", "r").read()
    return Response(body=html, headers={"Content-Type": "text/html; charset=utf-8"}, status_code=200)

