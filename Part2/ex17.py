import random

def SHabi():
    name = input("What is your name? ")
    
    adjectives = ["Sneaky", "Brave", "Silent", "Cunning", "Swift", "Shadowy"]
    animals = ["Otter", "Panther", "Hawk", "Fox", "Wolf", "Cobra"]

    adjective = random.choice(adjectives)
    animal = random.choice(animals)
    codename = f"{adjective} {animal}"

    lucky_number = random.randint(1, 99)

    print(f"{name}, your codename is: {codename}")
    print(f"Your lucky number is: {lucky_number}")

SHabi()
   




     



     
