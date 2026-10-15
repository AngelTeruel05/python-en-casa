personajes_frieren = [
{
"nombre": "Frieren",
"raza": "Elfo",
"clase": "Mago",
"edad": 1000,
"afiliacion": ["Grupo de los Cuatro Héroes", "Grupo de Frieren"]
},
{
"nombre": "Himmel",
"raza": "Humano",
"clase": "Héroe",
"edad": 76,
"afiliacion": ["Grupo de los Cuatro Héroes"]
},
{
"nombre": "Fern",
"raza": "Humano",
"clase": "Mago",
"edad": 19,
"afiliacion": ["Grupo de Frieren", "Magos de Primera Clase"]
},

{
"nombre": "Stark",
"raza": "Humano",
"clase": "Guerrero",
"edad": 18,
"afiliacion": ["Grupo de Frieren"]
},
{
"nombre": "Heiter",
"raza": "Humano",
"clase": "Sacerdote",
"edad": 100,
"afiliacion": ["Grupo de los Cuatro Héroes"]
},
{
"nombre": "Eisen",
"raza": "Enano",
"clase": "Guerrero",
"edad": 120,
"afiliacion": ["Grupo de los Cuatro Héroes"]
},
{
"nombre": "Sein",
"raza": "Humano",
"clase": "Sacerdote",
"edad": 28,
"afiliacion": ["Grupo de Frieren"]
},
{
"nombre": "Ubel",
"raza": "Humano",
"clase": "Mago",
"edad": 19,
"afiliacion": ["Magos de Primera Clase"]
},
{
"nombre": "Aura la Guillotina",
"raza": "Demonio",
"clase": "Mago",
"edad": 500,
"afiliacion": ["Siete Sabios de la Destrucción"]
},
{
"nombre": "Denken",
"raza": "Humano",
"clase": "Mago",
"edad": 78,
"afiliacion": ["Magos de Primera Clase", "Asociación Continental de Magia"]

},
{
"nombre": "Serie",
"raza": "Elfo",
"clase": "Mago",
"edad": 2000,
"afiliacion": ["Asociación Continental de Magia"]
},
{
"nombre": "Sense",
"raza": "Humano",
"clase": "Mago",
"edad": 28,
"afiliacion": ["Magos de Primera Clase", "Asociación Continental de Magia"]
}
]

print("8. Muestra la edad media de los personajes humanos.")
contador_humanos=0
edadHumanos =0
for personaje in personajes_frieren:
    if personaje["raza"] == "Humano":
        edadHumanos = edadHumanos + personaje["edad"]
        contador_humanos = contador_humanos +1
edadMediaHumana = edadHumanos / contador_humanos
print("La edad media de los humanos es de: ",edadMediaHumana)

print()
print("9. Muestra el nombre y la raza de todos los personajes que sean magos de primera clase.")

for personaje in personajes_frieren:
    if "Magos de Primera Clase" in personaje["afiliacion"]:                                                                               
        print("Nombre:",personaje["nombre"], " - Raza:",personaje["raza"], " - Afiliacion:",personaje["afiliacion"])

         
print()
print("10. Muestra el nombre, la raza y la edad de los personajes del grupo de los cuatro héroes.")
for personaje in personajes_frieren:
    if "Grupo de los Cuatro Héroes" in personaje["afiliacion"]:
        print(personaje["nombre"], " - ", personaje["raza"], " - ", personaje["edad"])

print()
print("11. Inserta al final de la lista un nuevo personaje que tenga todos los campos con algún valor con sentido (puedes inventártelos, pero que sean razonables).")

new_personaje = {
    "nombre": "Lyria",
    "raza": "Elfo",
    "clase": "Guerrera",
    "edad": 150,
    "afiliacion": ["Grupo de los Cuatro Héroes", "Grupo de Lyria"]
}

personajes_frieren.append(new_personaje)

print()
print("12. Elimina todos los personajes cuya raza sea demonio.")

for personaje in personajes_frieren[:]:
    if personaje["raza"] == "Demonio":
        personajes_frieren.remove(personaje)

for personaje in personajes_frieren:
    print(personaje["nombre"], " - ", personaje["raza"])

print()
print("13. Añádele a todos los elfos la afiliación “Elfos Supervivientes del Examen de Python")

for personaje in personajes_frieren:
    if personaje["raza"] == "Elfo":
        personaje["afiliacion"].append("Elfos Supervivientes del Examen de Python")

print()
print("14. A todos los personajes que pertenezcan a la Asociación Continental de Magia, quítales esa afiliación.")

for personaje in personajes_frieren:
    if "Asociacion Continental de Magia" in personaje["afiliacion"]:
        personaje["afiliacion"].remove("Asociacion Continental de Magia")


print()
print("15. Modifica la raza de todos los humanos que tengan 100 o más años a “Zombie”.")

for personaje in personajes_frieren:
    if personaje["raza"] == "Humano" and personaje["edad"] >= 100:
        personaje["raza"] = "Zombie"

for personaje in personajes_frieren:
    print(personaje["nombre"], " - ", personaje["raza"], " - ", personaje["edad"])