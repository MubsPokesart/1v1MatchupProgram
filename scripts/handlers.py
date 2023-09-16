import random
from utils import int_selection

class ProgramHandler:
    def __init__(self, gen):
        self.gen = gen
        self.mons = []

    def get_mon_names(self):
        return [mon.name for mon in self.mons]
    
    def get_mon_ids(self):
        return [mon.id for mon in self.mons]

    def parse_mon_matchups(self, name, data, index):
        ID = 1 + random.random()
        mon = MonHandler(name, data, ID, index)
        self.mons.append(mon)
    
    def find_mon(self, name):
        for mon in self.mons:
            if mon.name == name:
                return mon

    def prompt_team_method(self):        
        print("***************************************\n")
        team_select = int_selection(range(1, 4), "Enter your choice of Teambuilding Method\n\nAvailible Options:\n1. One Pokemon Given\n2. Two Pokemon Given (FindThird)\n3. Random First Mon\n\nEnter the NUMBER listed for the option: ", "\nThe NUMBER given was not a method listed. Please enter it again if it was a mistake.")
        match (team_select):
            case 1:
                return self.team_generation(1)
            case 2:
                return self.team_generation(2)
            case 3:
                return self.random_team_generation()
            
    def menu_selection(self, selections=int, objective=str):
        program_name_list = self.get_mon_names()
        pokemon_selected = []

        for select in range(selections):
            while True:
                pokemon_choices = []
                program_choice_prompt = ""

                added_pokemon = input(f"Enter the first few letters of the Pokemon you want to {objective}: ")
                modded_pokemon = added_pokemon.lower()
                chars_pokemon = len(added_pokemon)

                for mon_name in program_name_list:
                    if ((len(pokemon_choices) <= 10) and modded_pokemon == (mon_name[:chars_pokemon]).lower()):
                        pokemon_choices.append(mon_name)

                for index, item in enumerate(pokemon_choices):
                    program_choice_prompt += f'{index + 1}. {item}\n'

                if (len(pokemon_choices)) > 0:
                    pokemon_choice = int_selection(range(1, len(pokemon_choices )+ 1), f"Here's a list of options that best fit what you put in. Choose the number of the choice in the Program that you would like to use:\n{program_choice_prompt}\nIf you want to CANCEL, use -1. If you want to exit entirely (FOR MONS BEATEN), use -2. ", "The Number you entered in is not in the range. The number you need to input is before the point(.), ex: 1. metagross_1.")
                    if pokemon_choice > -1: 
                        pokemon_selected.append(self.find_mon(pokemon_choices[pokemon_choice - 1]))
                        break
                    elif pokemon_choice == -2:
                        return self.find_mon(pokemon_choices)
                    else:
                        print("Process Reset.")
                       
                else:
                    print(f"Nothing in our index fits your search {added_pokemon}, try doing it again.\n")
           
        return pokemon_selected
    
    def generate_matchups(self, to_use, to_beat):
        teams = {}
        

        mon1 = to_use[0]

        if len(to_use) == 1:
            for mon2 in self.mons:
                for mon3 in self.mons:
                    new_team = Team([mon1, mon2, mon3])
                    if (new_team.id not in teams) and new_team.validated_team:
                        teams[new_team.id] = new_team
        else:
            mon2 = to_use[1]
            for mon3 in self.mons:
                    new_team = Team([mon1, mon2, mon3])
                    if (new_team.id not in teams) and new_team.validated_team:
                        teams[new_team.id] = new_team
    
        processed_teams = []

        for validated_team in teams.values():
            team_matchups = validated_team.combine_matchups()

            if len(to_beat) > 0:
                not_beat = False
                for mon in to_beat:
                    try:
                        if team_matchups[mon.index] != 1:
                            not_beat = True
                    except IndexError:
                        pass
                if not_beat:
                    continue

            processed_teams.append([validated_team.generate_names(), sum(team_matchups)])
        
        return processed_teams

    def prompt_mons_beaten(self):
        beaten_prompt = int_selection({0, 1}, "Is there a set of Pokemon that you want to beat in your teams?\n1 for YES, 0 for NO: ", "\nThe Number you put in was neither 0 or 1.") 
        return beaten_prompt == 1

    def team_generation(self, mons=int):
        selected_pokemon = self.menu_selection(mons, "use")
        selected_to_beat = []
        
        if self.prompt_mons_beaten():
            selected_to_beat = self.menu_selection(len(self.mons), "beat")
        
        return sorted(self.generate_matchups(selected_pokemon, selected_to_beat), key=lambda x: x[1], reverse=True)

    def random_team_generation(self):
        random_teams = []
        range_length  = len(self.mons)

        while (len(random_teams < 20)):
            random_team = Team(self.mons[random.randint(0, range_length -1)], self.mons[random.randint(0, range_length -1)]. self.mons[random.randint(0, range_length -1)])
            if random_team.validated_team:
                random_team_matchups =  random_team.combine_matchups()
                random_teams.append(random_team.generate_names(), sum(random_team_matchups()))

        return sorted(random_teams, key=lambda x: x[1], reverse=True)
            
class MonHandler:
    def __init__(self, name, data, ID, index):
        self.name = name
        self.data = self.convert_data(data)
        self.id = ID
        self.index = index

    def convert_data(self, data):
        converted_data = []
        for point in data:
            match point:
                case 'w':
                    converted_data.append(1)
                case 'm':
                    converted_data.append(0.5)
                case 'l':
                    converted_data.append(0)
        return converted_data
    

class Team:
    def __init__(self, team=list):
        self.team = team
        self.validated_team = self.is_valid_team()
        self.id = self.generate_id()

    def generate_id(self):
        return sum([mon.id for mon in self.team])
    
    def generate_names(self):
        return [mon.name for mon in self.team]
    
    def is_valid_team(self):
        return (len(set(self.team)) == len(self.team))
    
    def combine_matchups(self):
        matchups = []
        for (matchup1, matchup2, matchup3) in zip(*[mon.data for mon in self.team]):
            matchups.append(max(matchup1, matchup2, matchup3))

        return matchups