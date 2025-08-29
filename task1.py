#Problem statement:
"""
1. Pikachu, I CHOOSE YOU!!
You are preparing your pokemon squad for a battle. Each pokemon in your pokedex has one or
more types. You have to form a team of all possible squads with k pokemons and their
combined types.
Based on those formations you have to choose the strongest team. Strongest team is the one
which as most number of types
"""

Pokedex = {
"Pikachu": ("Electric",), # ADDED a comma, so it's a tuple, not a string
"Charizard": ("Fire", "Flying"),
"Lapras": ("Water", "Ice"),
"Machamp": ("Fighting",),
"Mewtwo": ("Psychic", "Fighting"),
"Hoopa": ("Psychic", "Ghost", "Dark"),
"Lugia": ("Psychic", "Flying", "Water"),
"Squirtle": ("Water",),
"Gengar": ("Ghost", "Poison"),
"Onix": ("Rock", "Ground")
}

# So my logic is if we can sort pokedex based on number of types then it will give us the best possible
# combination as we can maximize the number of types
# We can do this recursively and find out every possible combination of possible and push that into a set


"""
So we can either choose the pokemon or we can not choose the pokemon
Then we append the types to a set and try to maximize the size of the set
"""

# These will store answers and hence are global variables
max_len=0
best_team=[]
best_type=set()


k=int(input("Enter the number of pokemon you need: "))
if(k>len(Pokedex)):
    print("Not enough pokemons")
    exit()


def make_teams(pokemon, k, index, typeSet, team):
    global max_len, best_team, best_type
    if(len(team)==k):
        if(len(typeSet)>max_len):
            max_len=len(typeSet)
            best_team=team[:] # or we could have used list(team)
            # we cannot use best_team = team because it will create a shallow copy and not a deep copy
            best_type=typeSet.copy()
        return
    
    if(index==len(pokemon)):
        return
    
    # We chose the pokemon
    team.append(pokemon[index])
    new_types=typeSet.union(Pokedex[pokemon[index]]) 
    make_teams(pokemon, k, index+1,new_types, team)

    #Then we remove the pokemon and move onto the next one
    team.pop()
    make_teams(pokemon, k, index+1, typeSet,team)


make_teams(list(Pokedex.keys()),k,0,set(),[])
print(f"My team is {best_team}")
print(f"All the types in my team are {best_type}")
