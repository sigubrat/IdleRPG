import random
import math
options = {"age": 8, "rename": 4, "take_money": 4, "give_money": 4, "random_crate": 2}
result = {"age": 0, "rename": 0, "take_money": 0, "give_money": 0, "random_crate": 0}
MAX = 23
possibilities = []
crate_possibilities = {"common": 0, "uncommon": 0, "rare": 0, "magic": 0, "legendary": 0}
N = 100000

def populate_possibilities(result, times):
    for _ in range(times):
        possibilities.append(result)

def calculate_rolls_until_death():
    return math.ceil(math.log10(1/23)/math.log(22/23))

def display_event(e):
    print(f"Your kid will probably {e} {math.floor(result[e]/N)} times")

def display_kid_events():
    for event, count in result.items():
        display_event(event)

def display_crate_probabilities():
    for _ in range(N):
        for _ in range(math.ceil(result["random_crate"]/N)):
            rand = math.floor(random.random()*761)
            if rand <= 1: crate_possibilities["legendary"]+=1
            elif rand <= 10: crate_possibilities["magic"]+=1
            elif rand <= 50: crate_possibilities["rare"]+=1
            elif rand <= 200: crate_possibilities["uncommon"]+=1
            else: crate_possibilities["common"]+=1
    
    for rarity, count in crate_possibilities.items():
        if count > 0: print(f"Your kid found {math.floor(count/N)} {rarity} crates!")

if __name__ == "__main__":
    # Populate all possibilities
    for option, times in options.items():
        populate_possibilities(option, times)
    
    ROLLS = calculate_rolls_until_death()

    print("Rolls until there's a 95% your kid is dead: ", ROLLS)
    print(f"Running {N:,} simulations with {ROLLS} rolls and presenting averages!")
    for _ in range(N): 
        for i in range(ROLLS):
            event = random.choice(possibilities)
            result[event] += 1
    
    display_kid_events()
    display_crate_probabilities()
    # Calculate how many rolls until dead