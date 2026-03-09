



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

    #I have to change this to make it worth it for all Pokemon
    '''def evolving(self):
        if self.poke_level >= 16:
            print(f'{self.name} just evolved to Combusken!')
            self.name = "Combusken"
        else: pass'''


class Pokedex:
    def __init__(self):
        self.self_entries: list = []

    def add_pokemon(self, pokemon_obj: Pokemon):
        if not isinstance(pokemon_obj, Pokemon):
            raise TypeError("You can only add Pokemon objects to the Pokedex!")
        
        self.self_entries.append(pokemon_obj)
        print(f"{pokemon_obj.name} has been added to the Pokedex!")

    def show_all(self):
        for poke in self.self_entries:
            print(f"Name: {poke.name} | Type: {poke.poke_type} | Stats: {poke.poke_stats}")

    def save_to_file(self, filename: str):
        # 'w' means Write mode (it creates the file or overwrites it)
        with open(filename, 'w') as file:
            for poke in self.self_entries:
                # We create a string for each pokemon
                line = f"{poke.name}, {poke.poke_type}, {poke.poke_stats}\n\n"
                file.write(line)
        print(f"Pokedex saved successfully to {filename}!")

    def get_by_type(self, type_name: str) -> list:
        return [poke.name for poke in self.self_entries 
                if poke.poke_type.lower().strip() == type_name.lower().strip()]

''' def load_from_file(self, filename: str):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    # Clean the line
                    clean_line = line.strip()

                    if not clean_line:
                        continue
                    data = clean_line.split(',')
                    # Check if we have all 3 pieces of data (Name, Level, Type)
                    if len(data) < 3:
                        print(f"Skipping messy line: {clean_line}")
                        continue # Moves to the next line instead of crashing

                    new_poke = Pokemon(data[0], data[1], data[])
                    self.add_pokemon(new_poke)
                print("Data loaded back into the Dex!")
        except FileNotFoundError:
            print("No save file found. Starting fresh!")'''
    

p1 = Pokemon("Bulbasur", "Grass",
             {"Level":5, "HP":45, "Attack":49, "Defense":49, "Sp.Atk":65, "Sp.Def":65, "Speed":45})

p2 = Pokemon("Charizard", "Fire", 
             {"Level": 60, "HP":160, "Attack":100, "Defense":120, "Sp.Atk":170, "Sp.Def":140, "Speed":200})

p3 = Pokemon("Darmanitan", "Fire",
             {"Level": 30, "HP":120, "Attack":130, "Defense":70, "Sp.Atk":33, "Sp.Def":78, "Speed":97})


'''for level in range(11):
    p1.level_up()
    p1.evolving()
    print(f'Name: {p1.name} - Level: {p1.level}')'''

vael_pokedex = Pokedex()
vael_pokedex.add_pokemon(p1)
vael_pokedex.add_pokemon(p2)
vael_pokedex.add_pokemon(p3)

#vael_pokedex.load_from_file("poke_update.txt")

#vael_pokedex.show_all()
#p1.level_up()
#vael_pokedex.show_all()
#vael_pokedex.save_to_file("Vael_Pokedex.txt")
#print(f"Pokedex length: {len(vael_pokedex.self_entries)}")
#print(vael_pokedex.get_by_type("Grass"))
print(p1.stats_sum)

