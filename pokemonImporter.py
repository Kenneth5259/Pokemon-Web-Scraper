import csv
import json
import requests

apiUrl = "http://localhost:8080/pokemon"

class Pokemon:
    def __init__(self):
        self.pokedexNumber = None
        self.name = None
        self.type1 = None
        self.type2 = None
        self.hp = None
        self.att = None
        self.defense = None
        self.spA = None
        self.spD = None
        self.spe = None
        self.previousEvolution = None
        self.nextEvolutions = None

    def __init__(self, pokedexNumber, name, type1, type2, hp, att, defense, spA, spD, spe):
        self.pokedexNumber = pokedexNumber
        self.name = name
        self.type1 = type1
        if type2 == "nan":
            self.type2 = None
        else:
            self.type2 = type2
        self.hp = hp
        self.att = att
        self.defense = defense
        self.spA = spA
        self.spD = spD
        self.spe = spe
        self.previousEvolution = None
        self.nextEvolutions = None
        self.imageName = str(pokedexNumber).zfill(3) + ".png"

def generatePokemonFromFile():
    print("Opening File...")
    with open('pokemon.csv', newline='') as csvfile:
        # Read first row to remove header
        csvfile.readline()
        # Create a pokemon for each row
        csvreader = csv.reader(csvfile, delimiter=',')
        x = 1
        for row in csvreader:
            tempPokemon = Pokemon(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            pkmnString = json.dumps(tempPokemon.__dict__)
            r = requests.post(apiUrl, data=pkmnString, headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
            #print(pkmnString)

def main():
    print("Starting Import")
    generatePokemonFromFile()

if __name__ == "__main__":
    main()
