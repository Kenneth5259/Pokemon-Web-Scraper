import urllib.request
import time

start_time = time.time()

for i in range (1, 806):
    file_name =  '{:03d}'.format(i) + ".png"
    url_string = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/" + file_name
    urllib.request.urlretrieve(url_string, file_name)
    print("Saved ",  file_name)

end_time = time.time()
print("Done")
print("Time Duration = ", end_time - start_time, "sec")
