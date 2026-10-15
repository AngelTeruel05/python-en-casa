pokemons = [
{
"nombre": "Bulbasaur",
"generacion": 1,

"categoria": "Semilla",
"tipos": ["Planta", "Veneno"],
"peso_kg": 6.9,
"altura_m": 0.7
},
{
"nombre": "Charizard",
"generacion": 1,
"categoria": "Llama",
"tipos": ["Fuego", "Volador"],
"peso_kg": 90.5,
"altura_m": 1.7
},
{
"nombre": "Squirtle",
"generacion": 1,
"categoria": "Tortuguita",
"tipos": ["Agua"],
"peso_kg": 9.0,
"altura_m": 0.5
},
{
"nombre": "Pikachu",
"generacion": 1,
"categoria": "Ratón",
"tipos": ["Eléctrico"],
"peso_kg": 6.0,
"altura_m": 0.4
},
{
"nombre": "Jigglypuff",
"generacion": 1,
"categoria": "Globo",
"tipos": ["Normal", "Hada"],
"peso_kg": 5.5,
"altura_m": 0.5
},
{
"nombre": "Eevee",
"generacion": 1,
"categoria": "Evolución",
"tipos": ["Normal"],
"peso_kg": 6.5,
"altura_m": 0.3
},
{
"nombre": "Lucario",
"generacion": 4,

"categoria": "Aura",
"tipos": ["Lucha", "Acero"],
"peso_kg": 54.0,
"altura_m": 1.2
},
{
"nombre": "Gardevoir",
"generacion": 3,
"categoria": "Envolvente",
"tipos": ["Psíquico", "Hada"],
"peso_kg": 48.4,
"altura_m": 1.6
},
{
"nombre": "Greninja",
"generacion": 6,
"categoria": "Ninja",
"tipos": ["Agua", "Siniestro"],
"peso_kg": 40.0,
"altura_m": 1.5
}
]

print("1. Muestra en una sóla línea el nombre y el peso del pokémon con más peso.")

mayor_peso = 0
pokemon_pesado=""
for pokemon in pokemons:
    if pokemon["peso_kg"] > mayor_peso:
        mayor_peso=pokemon["peso_kg"]
        pokemon_pesado = pokemon["nombre"]

print("El pokemon mas pesado es ",pokemon_pesado, " con un peso de ",mayor_peso)

print()
print("2. Muestra la media de altura de todos los pokémons.")
suma=0
contador=0
for pokemon in pokemons:
    suma = suma + pokemon["altura_m"]
    contador = contador +1

resultado = suma / contador

print("La altura media de los pokemons es de: ",resultado)

print()
print("3. Muestra el nombre y la altura de todos los pokémons que midan menos que la media.")

for pokemon in pokemons:
    if pokemon["altura_m"] < resultado:
        print("Nombre: ",pokemon["nombre"], " - Altura: ",pokemon["altura_m"])

print()
print("4. Muestra el nombre y los tipos de los pokémons que sean de tipo agua.")

for pokemon in pokemons:
    if "Agua" in pokemon["tipos"]:
        print(pokemon["nombre"], " - ", pokemon["tipos"])

print()
print("5. Muestra los pokémons que tengan un tipo que acabe en “a”.")
for pokemon in pokemons:
    for tipo in pokemon["tipos"]:
        if tipo.endswith("a"):
            print(pokemon["nombre"], " - ", pokemon["tipos"])
    
print()
print("6. Inserta al final de la lista un nuevo pokémon que tenga todos los campos con algún valor con sentido (puedes inventártelos, pero que sean razonables).")
new_pokemon = {
    "nombre" : "Gengar",
    "generacion" : 1,
    "categoria" : "Ninja",          
    "tipos": ["fantasma", "Siniestro"],
   "peso_kg": 20.0,               
    "altura_m": 1.5
}    

pokemons.append(new_pokemon)

print("Nuevo Pokemon añadido: ", pokemons[-1])

print()
print("7. Elimina todos los pokémons de tipo normal.")

##[:] sirve para hacer una copia de una lista completa. para eliminar
for pokemon in pokemons[:]:
    if "Normal" in pokemon["tipos"]:
        pokemons.remove(pokemon)


for pokemon in pokemons:
    print(pokemon["nombre"], " - ", pokemon["tipos"])
