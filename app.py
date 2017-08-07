from chalice import Chalice, Response

# 
import pokemon
import json
from urllib.parse import parse_qs

app = Chalice(app_name='pokegram')
app.debug = True

@app.route('/favicon.ico')
def favicon():
    '''
    This is only to return the favicon.ico file that is required when running chalice locally
    '''
    return Response(body="favicon", headers={"Content-Type": "text/plain"}, status_code=200)

@app.route('/api/health')
def health():
    '''
    The root path return a text message of "API OK"
    '''
    return Response(body="API OK", headers={"Content-Type": "text/plain"}, status_code=200)

@app.route('/pokemon')
def index():
    '''
    Returns the `index.html` page that contains the pokemon app
    '''
    html = open("index.html", "r").read()
    return Response(body=html, headers={"Content-Type": "text/html; charset=utf-8"}, status_code=200)

@app.route('/api/pokemon')
def get_pokemon_info():
    '''
    Returns the data associated with each pokemon that's necessary for the initial rendering of index.html
    In production this data would be bootstrapped in index.html to preclude the initial JSON request to this endpoint
    '''
    pokemon_collection = pokemon.fetch_all_pokemon()
    return json.dumps(pokemon_collection)



@app.route('/api/picture', methods=['POST'], content_types=['Content-Type:multipart/form-data'])
def upload_photo():
    '''
    uploads photo from client, saves to S3, and returns the URL of the uploaded photo
    Currently not working
    '''
    parsed_photo = parse_qs(app.current_request.raw_body.decode())
    
    return json.dumps({'status': 'ok'})
