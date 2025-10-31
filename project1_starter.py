"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Kabijah Hill
Date: 2024-10-01

AI Usage: AI helped with file I/O error handling logic in save_character function
"""
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    if character_class == "Sentinel":
        strength = 10 + level * 3
        magic = 3 + level * 1
        health = 100 + level * 5
    elif character_class == "Arcanist":
        strength = 4 + level * 1
        magic = 12 + level * 4
        health = 80 + level * 3
    elif character_class == "Ranger":
        strength = 7 + level * 2
        magic = 6 + level * 2
        health = 90 + level * 4
    elif character_class == "Cleric":
        strength = 6 + level * 1
        magic = 10 + level * 3
        health = 110 + level * 5
    else:
        # default stats
        strength = 5 + level * 1
        magic = 5 + level * 1
        health = 100 + level * 3
    return (strength, magic, health)

    
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    gold = 100
    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }



def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns True if successful, False if error occurs
    """
    try:
        with open(filename, "w") as file:
            file.write(f"Character Name: {character['name']}\n")
            file.write(f"Class: {character['class']}\n")
            file.write(f"Level: {character['level']}\n")
            file.write(f"Strength: {character['strength']}\n")
            file.write(f"Magic: {character['magic']}\n")
            file.write(f"Health: {character['health']}\n")
            file.write(f"Gold: {character['gold']}\n")
        print(f"{filename} saved successfully!")
        return True
    except Exception as e:
        print(f" Error saving character: {e}")
        return False

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        char = {}
        for line in lines:
            key, value = line.strip().split(": ")
            if key in ["Level", "Strength", "Magic", "Health", "Gold"]:
                value = int(value)
            char[key.replace("Character Name", "name").lower()] = value
        return char
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

def display_character(character):
    """
    Prints formatted character sheet
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}\n")

def level_up(character):
    """
    Increases character level and recalculates stats
    """
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

# =====================
# Main Program
# =====================
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!\n")

    # Create characters
    ariah = create_character("Ariah", "Arcanist")
    memphis = create_character("Memphis", "Ranger")
    locus = create_character("Locus", "Sentinel")

    # Display characters
    print("Main Character:")
    display_character(ariah)
    print("Side Character 1:")
    display_character(memphis)
    print("Side Character 2:")
    display_character(locus)

    # Save characters
    save_character(ariah, "ariah.txt")
    save_character(memphis, "memphis.txt")
    save_character(locus, "locus.txt")
