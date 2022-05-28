import urllib.request
import time
import os

def retrieve_pokemon_image(file, url):
    cwd = os.getcwd()
    fullfilename = os.path.join(cwd,'images', file)
    print(fullfilename)
    try:
        urllib.request.urlretrieve(url, fullfilename)
        print("Saved ",  file)
    except:
        print("The attempted pokemon does not exist in Pokemon Assets")

def main():
    start_time = time.time()
    # Latest Number Available in Pokemon Online
    for i in range (1, 906):

        file_name =  '{:03d}'.format(i) + ".png"
        url_string = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/" + file_name
        retrieve_pokemon_image(file_name, url_string)

        # Number of variations like mega/gigantamax/hisuian
        for x in range(2,6):
            file_name =  '{:03d}'.format(i) + "_f" + str(x) + ".png"
            url_string = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/" + file_name
            retrieve_pokemon_image(file_name, url_string)

    end_time = time.time()
    print("Done")
    print("Time Duration = ", end_time - start_time, "sec")        

if __name__ == "__main__":
    main()