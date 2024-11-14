import random

def name_Generator(desired_alphabet):
    # List of possible names to choose from
    names = [
        "Alice", "Amelia", "Alexander", "Anthony", "Barbara", "Benjamin", "Caroline", "Charles",
        "Diana", "Daniel", "Edward", "Eleanor", "Fiona", "Frederick", "George", "Grace",
        "Hannah", "Henry", "Isabella", "Isaac", "Jack", "Julia", "Kevin", "Katherine",
        "Laura", "Liam", "Megan", "Matthew", "Nina", "Nathan", "Olivia", "Oscar",
        "Penelope", "Paul", "Quincy", "Quinn", "Rachel", "Robert", "Sophia", "Samuel",
        "Thomas", "Theodore", "Uma", "Ulysses", "Violet", "Victor", "William", "Wendy",
        "Xander", "Xena", "Yara", "Yosef", "Zara", "Zachary"
    ]
    
    # Filter names that start with the desired alphabet
    filtered_names = [name for name in names if name.startswith(desired_alphabet.capitalize())]
    
    # If no names are found with the given alphabet, handle the case
    if not filtered_names:
        return f"No names found starting with '{desired_alphabet}'"

    # Randomly select a name from the filtered list
    generated_name = random.choice(filtered_names)
    return generated_name

# Example usage
user_input = input("Enter the first letter of the name you want: ")
result = name_Generator(user_input)
print(f"Generated Name: {result}")