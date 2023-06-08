import requests
import random
def trace(*args):
  pass

pokemonlist = ["bulbasaur", "charmander", "squirtle", "caterpie", "butterfree", "weedle", "pidgey", "rattata", "spearow", "ekans", "pikachu", "sandshrew", "nidoran", "vulpix", "jigglypuff"]

print("Welcome to the Pokemon API!\n")

name = ""
while(name != "q"):
  name = input("Type a pokemon name or type r for a random pokemon to learn about (q = quit): ")
  if(name == "r"):
    name = random.choice(pokemonlist)
    print(f"Your pokemon is {name}.")

  URL = f"https://pokeapi.co/api/v2/pokemon/{name}"
  trace ("Calling", URL)
  response = requests.get(URL)
  response.raise_for_status()  

  data = response.json() 
  print(f"pokemon id: {data['id']}\nbase experience: {data['id']}\nability: {data['abilities'][0]['ability']['name']}\nheld item: {data['held_items'][0]['item']['name']}\n")