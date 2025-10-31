"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Kabijah Hill
Date: 2024-10-01

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    gold = 100  # Starting gold
    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    - Sentinel: High strength, low magic, high health
    - Arcanist: Low strength, very high magic, low health  
    - Ranger: Balanced stats, decent health
    - Cleric: High magic and health, average strength
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)

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
        # default or unknown class
        strength = 5 + level * 1
        magic = 5 + level * 1
        health = 100 + level * 3

    return (strength, magic, health)

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
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
        return True
    except Exception as e:
        print(f"Error saving character: {e}")
        return False

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Create your three characters
    ariah = create_character("Ariah", "Arcanist")
    memphis = create_character("Memphis", "Ranger")
    locus = create_character("Locus", "Sentinel")

    # Display all characters
    print("Main Character:")
    display_character(ariah)
    print("\nSide Character 1:")
    display_character(memphis)
    print("\nSide Character 2:")
    display_character(locus)

    save_character(ariah, "ariah.txt")
    save_character(memphis, "memphis.txt")
    save_character(locus, "locus.txt")
    
# Example usage:
# char = create_character("TestHero", "Warrior")
# display_character(char)
# save_character(char, "my_character.txt")
# loaded = load_character("my_character.txt")
