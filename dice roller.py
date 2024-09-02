import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice= []
total = 0
numDice = int(input ("how many dice to roll"))

for die in range (numDice):
    dice.append(random.randint(1,6))
#vertical paiting of dice 
#for die in range(numDice):
#    for line in dice_art.get(dice[die]):
#        print (line)
#horizontal painting of dice 
for line in range(5):
    for die in dice:
        print (dice_art.get(die)[line],end ="")
    print()

for die in dice:
    total += die 

print(f"total:{total}")



