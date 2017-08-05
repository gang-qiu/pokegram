


ICON_URL = 'https://pldh.net/media/pokemon/shuffle/' # url for pokemon icons. Ends with 3-digit 0-padded id of pokemon
                                                     # complete url: 'https://pldh.net/media/pokemon/shuffle/021.png'

def fetch_all_pokemon():
    # reads in pokemon list from pokemon151.txt
    # returns collection containing pokemon id and associated icon_url

    pokemon_collection = []
    pokemon_id = 0
    file = open('pokemon151.txt', 'r')
    for pokemon in file:
        pokemon_id += 1
        pokemon_collection.append({
            "name": pokemon.strip(),    # strip trailing newline character
            "id": pokemon_id,
            "icon_url": ICON_URL + three_digit_number(pokemon_id) + '.png'
        })

    return pokemon_collection

def three_digit_number(num):
    #  returns a number as a 0-padded 3 digit string
    #  eg "2" => "002"
    #  this is needed for the icon url for each pokemon

    num_str = str(num)
    padded_zeroes = '0' * (3-len(num_str));
    return padded_zeroes + num_str