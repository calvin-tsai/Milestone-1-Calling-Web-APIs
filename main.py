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