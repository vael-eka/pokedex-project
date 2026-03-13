
from decorators import *
import json, os

class Pokedex:
    def __init__(self):
        self.self_entries: list = []


    #Loads n Pokemon from a json file
    def load_from_json(self, filename="pokedex.json"):
        #Check the radar first!
        if os.path.exists(filename):
            with open(filename, "r") as f:
                raw_data = json.load(f)
                self.self_entries = []
            for item in raw_data:
                new_poke = Pokemon(item['name'], item['type'], item['stats'])
                self.add_pokemon(new_poke)
            #print(f"Restored {len(raw_data)} Pokemon from the archives.")
        else:
            print("Warning: Archive file not found. Creating a new DataBase")

    #Saves the new Pokemon entries made here in the code to our json file
    def save_to_json(self, filename="pokedex.json"):
        data_to_save = []
        for poke in self.self_entries:
            poke_dict = {
                "name":poke.name,
                "type":poke.poke_type,
                "stats":poke.poke_stats
            }
            data_to_save.append(poke_dict)

        with open(filename, "w") as f:
            json.dump(data_to_save, f, indent=4)
        print("Archives successfully saved to the Jedi Temple!")


    def add_pokemon(self, pokemon_obj: Pokemon):
        if not isinstance(pokemon_obj, Pokemon):
            raise TypeError("You can only add Pokemon objects to the Pokedex!")
        
        self.self_entries.append(pokemon_obj)
        self.save_to_json()

    #Show all Pokemon in our Dex
    def get_formatted_entries(self):
        return (f"Name: {poke.name} - Type: {poke.poke_type} - Power: {poke.stats_sum}" for poke in self.self_entries)
    
            
    def get_by_type(self, type_name: str):
        return (poke.name for poke in self.self_entries if poke.poke_type.lower() == type_name.lower())

    #Get the most powerfull Pokes
    def get_elite_team(self, tresshold = 500):
        return (poke for poke in self.self_entries if poke.stats_sum >= tresshold)

    '''def get_elite(self, tresshold = 500):
            for pokemon in self.self_entries:
                if pokemon.stats_sum >= tresshold:
                    yield pokemon.name'''

    def get_pokemon_type(self, name:str):
        match = next((poke.poke_type for poke in self.self_entries if poke.name.lower() == name.lower()), None)

        if match:
            return f"The type of {name} is {match}."
        else:
            return "Pokemon not found in the archives."
        
    def remove_pokemon(self, name:str):
        self.self_entries = [poke for poke in self.self_entries if poke.name.lower() != name.lower()]
        self.save_to_json()


    

class Pokemon:
    def __init__(self, name:str, poke_type:str, poke_stats:dict):
        self.name: str = name
        self.poke_type: str = poke_type
        self.poke_stats: dict = poke_stats

    @property
    def stats_sum(self):
        combat_values = [val for key, val in self.poke_stats.items() if key != "Level"]
        return sum(combat_values)

    def level_up(self):
        self.poke_stats["Level"] += 1
        print(f'{self.name} level up to level {self.poke_stats["Level"]}')

    @shout
    def get_battle_cry(self):
        return f"{self.name} I choose you!"

    #I have to change this to make it worth it for all Pokemon
    '''def evolving(self):
        if self.poke_level >= 16:
            print(f'{self.name} just evolved to Combusken!')
            self.name = "Combusken"
        else: pass'''  

p1 = Pokemon("Bulbasur", "Grass",
             {"Level":5, "HP":45, "Attack":49, "Defense":49, "Sp.Atk":65, "Sp.Def":65, "Speed":45})

p2 = Pokemon("Charizard", "Fire", 
             {"Level": 60, "HP":160, "Attack":100, "Defense":120, "Sp.Atk":170, "Sp.Def":140, "Speed":200})

p3 = Pokemon("Darmanitan", "Fire",
             {"Level": 30, "HP":120, "Attack":130, "Defense":70, "Sp.Atk":33, "Sp.Def":78, "Speed":97})

p4 = Pokemon("Gengar", "Ghost", 
             {"Level": 45, "HP": 130, "Attack": 65, "Defense": 60, "Sp.Atk": 130, "Sp.Def": 75, "Speed": 110})

p5 = Pokemon("Lucario", "Fighting", 
             {"Level": 36, "HP": 140, "Attack": 110, "Defense": 70, "Sp.Atk": 115, "Sp.Def": 70, "Speed": 90})

p6 = Pokemon("Gyarados", "Water", 
             {"Level": 52, "HP": 195, "Attack": 125, "Defense": 79, "Sp.Atk": 60, "Sp.Def": 100, "Speed": 81})

p7 = Pokemon("Gardevoir", "Psychic", 
             {"Level": 40, "HP": 138, "Attack": 65, "Defense": 65, "Sp.Atk": 125, "Sp.Def": 115, "Speed": 80})

p8 = Pokemon("Reshiram", "Fire", 
             {"Level": 55, "HP": 208, "Attack": 130, "Defense": 95, "Sp.Atk": 80, "Sp.Def": 85, "Speed": 102})

p9 = Pokemon("Umbreon", "Dark", 
             {"Level": 32, "HP": 195, "Attack": 65, "Defense": 110, "Sp.Atk": 60, "Sp.Def": 130, "Speed": 65})

p10 = Pokemon("Metagross", "Steel", 
             {"Level": 50, "HP": 180, "Attack": 135, "Defense": 130, "Sp.Atk": 95, "Sp.Def": 90, "Speed": 70})

p11 = Pokemon("Mawile", "Fairy", 
             {"Level": 87, "HP": 180, "Attack": 200, "Defense": 130, "Sp.Atk": 95, "Sp.Def": 90, "Speed": 70})




'''for level in range(11):
    p1.level_up()
    p1.evolving()
    print(f'Name: {p1.name} - Level: {p1.level}')'''

vael_pokedex = Pokedex()

vael_pokedex.load_from_json()

#vael_pokedex.add_pokemon(p11)
#vael_pokedex.save_to_json()
'''vael_pokedex.add_pokemon(p1)
vael_pokedex.add_pokemon(p2)
vael_pokedex.add_pokemon(p3)
vael_pokedex.add_pokemon(p4)
vael_pokedex.add_pokemon(p5)
vael_pokedex.add_pokemon(p6)
vael_pokedex.add_pokemon(p7)
vael_pokedex.add_pokemon(p8)
vael_pokedex.add_pokemon(p9)
vael_pokedex.add_pokemon(p10)'''
#vael_pokedex.save_to_json()


vael_pokedex.remove_pokemon("Darmanitan")

for poke in vael_pokedex.get_formatted_entries():
    print(poke)


#vael_pokedex.load_from_file("poke_update.txt")

#vael_pokedex.show_all()
#p1.level_up()
#vael_pokedex.show_all()
#vael_pokedex.save_to_file("Vael_Pokedex.txt")
#print(f"Pokedex length: {len(vael_pokedex.self_entries)}")
#print(p1.get_battle_cry())
#for item in vael_pokedex.get_by_type("ghost"):
#   print(item)

#for item in vael_pokedex.get_elite():
#    print(f"{item} it's a beast!")

#glass_cannons = (p for p in vael_pokedex.self_entries if p.poke_stats["Attack"] > 100 and p.poke_stats["Defense"] < 80)

#for cannon in glass_cannons:
#    print(f"Danger: {cannon.name} has {cannon.poke_stats["Attack"]} but only {cannon.poke_stats["Defense"]} Defense!")

#max_val = max(p.poke_stats["Attack"] for p in vael_pokedex.self_entries)

#boss_pokes = (p.name for p in vael_pokedex.self_entries if p.poke_stats["Attack"] == max_val)

#for name in boss_pokes:
#    print(f"{name} is the most physical attacker with {max_val} Attack!")

#print(vael_pokedex.get_pokemon_type("Gengar"))

'''entries = vael_pokedex.get_formatted_entries()
found_any = False

for poke in entries:
    print(poke)
    found_any = True

if not found_any:
    print("No Pokemon found in the database")'''


