import random
import time

def print_slow(text):
    """Print text slowly for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

# Game variables
health = 100
ammo = 10
grenades = 3
rooms = ["Armory", "Med Bay", "Alien Nest", "Control Room", "Hallway"]
alien_health = 50
score = 0

def explore_room():
    """Explore a random room."""
    global health, ammo, grenades, score
    room = random.choice(rooms)
    print_slow(f"\nYou enter the {room}...\n")
    
    if room == "Armory":
        ammo_found = random.randint(2, 6)
        grenades_found = random.randint(0, 1)
        print_slow(f"You find {ammo_found} ammo and {grenades_found} grenades.")
        ammo += ammo_found
        grenades += grenades_found

    elif room == "Med Bay":
        health_boost = random.randint(10, 30)
        print_slow(f"You find a med kit and restore {health_boost} health.")
        health = min(100, health + health_boost)

    elif room == "Alien Nest":
        print_slow("You stumble into an alien nest!")
        alien_encounter()

    elif room == "Control Room":
        print_slow("You find some intel to increase your score!")
        score += 10

    elif room == "Hallway":
        print_slow("The hallway is eerily quiet...")

def alien_encounter():
    """Handle an alien encounter."""
    global health, ammo, grenades, alien_health, score
    print_slow("\nAn alien attacks!")
    alien_health = 50
    
    while alien_health > 0 and health > 0:
        print_slow(f"Alien health: {alien_health}, Your health: {health}, Ammo: {ammo}, Grenades: {grenades}")
        action = input("\nChoose your action - [F]ire, [G]renade, [R]un: ").strip().upper()
        
        if action == "F":
            if ammo > 0:
                damage = random.randint(10, 25)
                print_slow(f"You fire your weapon and deal {damage} damage!")
                alien_health -= damage
                ammo -= 1
            else:
                print_slow("You're out of ammo!")
        
        elif action == "G":
            if grenades > 0:
                damage = random.randint(20, 40)
                print_slow(f"You throw a grenade and deal {damage} damage!")
                alien_health -= damage
                grenades -= 1
            else:
                print_slow("You're out of grenades!")
        
        elif action == "R":
            print_slow("You run away to safety!")
            return
        
        else:
            print_slow("Invalid action. The alien attacks!")
        
        if alien_health > 0:
            damage = random.randint(5, 20)
            print_slow(f"The alien retaliates and deals {damage} damage!")
            health -= damage

    if alien_health <= 0:
        print_slow("You defeated the alien!")
        score += 20
    elif health <= 0:
        print_slow("The alien overpowered you...")

def main():
    """Main game loop."""
    global health
    print_slow("Welcome to Xeno Crisis: Text Adventure!")
    print_slow("You are a soldier trapped in an alien-infested facility. Survive and find a way out!")
    
    while health > 0:
        print_slow(f"\nYour current status - Health: {health}, Ammo: {ammo}, Grenades: {grenades}, Score: {score}")
        choice = input("\nDo you want to [E]xplore a room or [Q]uit? ").strip().upper()
        
        if choice == "E":
            explore_room()
        elif choice == "Q":
            print_slow("You chose to retreat. Game over!")
            break
        else:
            print_slow("Invalid choice. Try again.")
    
    if health <= 0:
        print_slow("You succumbed to your injuries. Game over!")
    
    print_slow(f"Final Score: {score}")

if __name__ == "__main__":
    main()
