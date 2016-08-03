import sqlite3
import time


rarePokemonIds = [16]
encounteredPokemonIds = []

conn = sqlite3.connect('pogom.db')
cursor = conn.cursor()

count = 0
while True:
    print("Round: " + str(count))

    selectNewPokemons = """
        SELECT encounter_id, pokemon_id, latitude, longitude, disappear_time
        FROM pokemon
        WHERE pokemon_id IN ({seq}) AND
              disappear_time > datetime('now')
        """.format(seq=','.join(['?']*len(rarePokemonIds)))


    cursor = conn.execute(selectNewPokemons, rarePokemonIds)

    countNewPokemons = 0
    for row in cursor:
        pokemonId = row[0]

        if pokemonId not in encounteredPokemonIds:
            countNewPokemons += 1
            encounteredPokemonIds.append(pokemonId)
            #print(row)

    print(str(countNewPokemons) + " new pokemons.")
    print(encounteredPokemonIds[:5])
    count += 1
    time.sleep(5)


conn.close()