import random
import string

# ASCII Art for "NightGEN" title (scary theme)
ascii_art = """
███╗   ███╗ ██████╗     ██████╗ ███████╗███╗   ██╗
████╗ ████║██╔════╝    ██╔════╝ ██╔════╝████╗  ██║
██╔████╔██║██║         ██║  ███╗█████╗  ██╔██╗ ██║
██║╚██╔╝██║██║         ██║   ██║██╔══╝  ██║╚██╗██║
██║ ╚═╝ ██║╚██████╗    ╚██████╔╝███████╗██║ ╚████║
╚═╝     ╚═╝ ╚═════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                  

╔╦╗┌─┐┌┬┐┌─┐  ╔╗ ┬ ┬  ╔═╗┬ ┬┌─┐┬─┐┌─┐┬ ┬
║║║├─┤ ││├┤   ╠╩╗└┬┘  ╚═╗├─┤├─┤├┬┘├─┘└┬┘
╩ ╩┴ ┴─┴┘└─┘  ╚═╝ ┴   ╚═╝┴ ┴┴ ┴┴└─┴   ┴ 
"""

def generate_code(length=25):
    """Generate a random code similar to a Minecraft-style redeem code."""
    characters = string.ascii_uppercase + string.digits  # Letters and digits
    code = ''.join(random.choice(characters) for _ in range(length))
    return code

def generate_multiple_codes(n=5, length=25):
    """Generate a list of random codes."""
    codes = [generate_code(length) for _ in range(n)]
    return codes

def save_codes_to_file(codes, filename="generated_codes.txt"):
    """Save generated codes to a text file."""
    with open(filename, "w") as f:
        for code in codes:
            f.write(code + "\n")
    print(f"\n[✔] Codes have been saved to {filename}")

def get_user_input():
    """Get valid user input for the number of codes to generate."""
    while True:
        try:
            num_codes = int(input("How many codes would you like to generate? "))
            if num_codes < 1:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    return num_codes

def display_intro():
    """Display the scary, hacker-themed intro."""
    print("\n" + ascii_art)
    print("[ WARNING ]")
    print("[ This is a RANDOM CODE GENERATOR ]")
    print("\n")

def main():
    # Display the intro ASCII art
    display_intro()

    # Get user input for the number of codes
    num_codes = get_user_input()

    # Generate the codes (25 characters long by default)
    codes = generate_multiple_codes(n=num_codes, length=25)

    # Display generated codes in spooky, code-like format
    print("\n[ CODES GENERATED: ]\n")
    for i, code in enumerate(codes, 1):
        print(f"[ {i:02d} ] {code}")

    # Ask if the user wants to save the codes to a file
    save_option = input("\nDo you want to save the codes to a file? (y/n): ").strip().lower()
    if save_option == 'y':
        save_codes_to_file(codes)

if __name__ == "__main__":
    main()
