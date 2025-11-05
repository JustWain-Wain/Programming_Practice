from requests import get

Pokemons = []
for i in range(1,21):
    current = get(f"https://pokeapi.co/api/v2/pokemon/{i}/").json()
    Pokemons.append((current["name"], current["species"]["name"], current["weight"], current["height"], current["abilities"]))

print(Pokemons)
pokemon = input("Введите название покемона: ")
for i in range(21):
    if Pokemons[i][0] == pokemon:
        print(f"Имя: {Pokemons[i][0]}",
            f"Тип: {Pokemons[i][1]}",
            f"Вес: {Pokemons[i][2]}",
            f"Рост: {Pokemons[i][3]}",
            f"Способности: {Pokemons[i][4]}", sep="\n")
        break
