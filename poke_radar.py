import sqlite3
import time
from datetime import datetime

rarePokemonIds = [16]
encounteredPokemonIds = []
#twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

pokemonList = [
	'Bulbizarre'
	'Herbizarre',
	'Florizarre',
	'Salamèche',
	'Reptincel',
	'Dracaufeu',
	'Carapuce',
	'Carabaffe',
	'Tortank',
	'Chenipan',
	'Chrysacier',
	'Papilusion',
	'Aspicot',
	'Coconfort',
	'Dardargnan',
	'Roucool',
	'Roucoups',
	'Roucarnage',
	'Rattata',
	'Rattatac',
	'Piafabec',
	'Rapasdepic',
	'Abo',
	'Arbok',
	'Pikachu',
	'Raichu',
	'Sabelette',
	'Sablaireau',
	'Nidoran♀',
	'Nidorina',
	'Nidoqueen',
	'Nidoran♂',
	'Nidorino',
	'Nidoking',
	'Mélofée',
	'Mélodelfe',
	'Goupix',
	'Feunard',
	'Rondoudou',
	'Grodoudou',
	'Nosferapti',
	'Nosferalto',
	'Mystherbe',
	'Ortide',
	'Rafflesia',
	'Paras',
	'Parasect',
	'Mimitoss',
	'Aéromite',
	'Taupiqueur',
	'Triopikeur',
	'Miaouss',
	'Persian',
	'Psykokwak',
	'Akwakwak',
	'Férosinge',
	'Colossinge',
	'Caninos',
	'Arcanin',
	'Ptitard',
	'Têtarte',
	'Tartard',
	'Abra',
	'Kadabra',
	'Alakazam',
	'Machoc',
	'Machopeur',
	'Mackogneur',
	'Chétiflor',
	'Boustiflor',
	'Empiflor',
	'Tentacool',
	'Tentacruel',
	'Racaillou',
	'Gravalanch',
	'Grolem',
	'Ponyta',
	'Galopa',
	'Ramoloss',
	'Flagadoss',
	'Magnéti',
	'Magnéton',
	'Canarticho',
	'Doduo',
	'Dodrio',
	'Otaria',
	'Lamantine',
	'Tadmorv',
	'Grotadmorv',
	'Kokiyas',
	'Crustabri',
	'Fantominus',
	'Spectrum',
	'Ectoplasma',
	'Onix',
	'Soporifik',
	'Hypnomade',
	'Krabby',
	'Krabboss',
	'Voltorbe',
	'Électrode',
	'Nœunœuf',
	'Noadkoko',
	'Osselait',
	'Ossatueur',
	'Kicklee',
	'Tygnon',
	'Excelangue',
	'Smogo',
	'Smogogo',
	'Rhinocorne',
	'Rhinoféros',
	'Leveinard',
	'Saquedeneu',
	'Kangourex',
	'Hypotrempe',
	'Hypocéan',
	'Poissirène',
	'Poissoroy',
	'Stari',
	'Staross',
	'M.Mime',
	'Insécateur',
	'Lippoutou',
	'Élektek',
	'Magmar',
	'Scarabrute',
	'Tauros',
	'Magicarpe',
	'Léviator',
	'Lokhlass',
	'Métamorph',
	'Évoli',
	'Aquali',
	'Voltali',
	'Pyroli',
	'Porygon',
	'Amonita',
	'Amonistar',
	'Kabuto',
	'Kabutops',
	'Ptéra',
	'Ronflex',
	'Artikodin',
	'Électhor',
	'Sulfura',
	'Minidraco',
	'Draco',
	'Dracolosse',
	'Mewtwo',
	'Mew'
]

conn = sqlite3.connect('pogom.db', detect_types = sqlite3.PARSE_COLNAMES)
cursor = conn.cursor()

count = 0
while True:
    print("Round: " + str(count))

    selectNewPokemons = """
        SELECT encounter_id, pokemon_id, latitude, longitude, disappear_time as "[timestamp]"
        FROM pokemon
        WHERE pokemon_id IN ({seq}) AND
              disappear_time > datetime('now')
        """.format(seq=','.join(['?']*len(rarePokemonIds)))


    cursor = conn.execute(selectNewPokemons, rarePokemonIds)

    countNewPokemons = 0
    for row in cursor:
        encounterId = row[0]
        pokemonId = row[1]
        pokemonName = pokemonList[pokemonId]
        lat = '%.10f'%(row[2])
        lng = '%.10f'%(row[3])
        disTime = row[4]
        expirationTime = disTime.strftime('%Hh%Mm%Ss')
        remainingTime = disTime - datetime.now()
        remainingMinutes, remainingSeconds = divmod(remainingTime.days * 86400 + remainingTime.seconds, 60)

        if encounterId not in encounteredPokemonIds:
            countNewPokemons += 1
            encounteredPokemonIds.append(encounterId)

            tweetContent = "{0} apparu en {1},{2}. Disparaît à {3} (dans {4}m{5}s).".format(pokemonName, lat, lng, expirationTime, remainingMinutes, remainingSeconds)
            print(tweetContent)
            #twitter.update_status(status=tweetContent)

    print(str(countNewPokemons) + " new pokemons.")
    count += 1
    time.sleep(5)


conn.close()

