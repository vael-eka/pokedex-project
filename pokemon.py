



class Pokemon:
    def __init__(self, name:str, poke_type:list, level:int):
        self.name: str = name
        self.poke_type: list = poke_type
        self.level: int = level
        self.hp: int = level * 20

    def level_up(self):
        self.level += 1
        print(f'{self.name} level up to level {self.level}')

    def evolving(self):
        if self.level >= 16:
            print(f'{self.name} just evolved to Combusken!')
            self.name = "Combusken"
        else: pass

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
            print(f"Name: {poke.name} | Level: {poke.level}")

    def save_to_file(self, filename: str):
        # 'w' means Write mode (it creates the file or overwrites it)
        with open(filename, 'w') as file:
            for poke in self.self_entries:
                # We create a string for each pokemon
                line = f"{poke.name},{poke.level},{poke.poke_type}\n"
                file.write(line)
        print(f"Pokedex saved successfully to {filename}!")

    
    

p1 = Pokemon("Torchic", ["Fire", "Fight"], 5)

'''for level in range(11):
    p1.level_up()
    p1.evolving()
    print(f'Name: {p1.name} - Level: {p1.level}')'''

vael_pokedex = Pokedex()
vael_pokedex.add_pokemon(p1)
vael_pokedex.show_all()
print(len(vael_pokedex.self_entries))

