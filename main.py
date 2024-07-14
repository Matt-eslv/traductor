meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Una cara de risa",
            "CREEPY": "Algo aterrador que da miedo",
            "BOOMER": "Persona que se aferra mucho al pasado",
            "PA": "para",
            "TROLIAR": "Hacer una broma",
            }

for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("todavía no agregamos esa palabra en nuestro diccionario")
