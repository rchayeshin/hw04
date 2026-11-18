# ------------------------------------------------------
#        Name: (Riley Chaye-Shin)
#       Peers: (add any collaborators)
#  References: (lecture slides, python tutor)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """Reads text from user repeatedly until dog/Dog is used"""
    while True:
        # Read user text
        user_text = input("Enter text: ")
        
        # Check for secret word
        if secret_word in user_text:
            print("You used the secret word!")
            break
        # If not, check if dog or Dog is anywhere in text
        elif "dog" in user_text or "Dog" in user_text:
            print('You used the word "dog" or the word "Dog"!')
            break
        # If neither condition met, ask user to try again
        else:
            print("Try again")



# Task 2
def check_greater():
    """Reads two ints from the user and prints which one is greater, if equal, it repeats"""
    while True:
        # Read two nums from user and make them ints
        first = int(input("Enter the first integer: "))
        second = int(input("Enter the second integer: "))
        
        # Compare the  ints
        if first > second:
            print("First is Greater")
            break
        # If not, check if second is greater
        elif second > first:
            print("Second is Greater")
            break
        # If neither condition met (equal), ask user to try again
        else:
            print("Try again")



# Task 3
def get_special_numbers():
    """Checks ints in range 1 through 40 and prints the ones that are odd, multiples of 3, and not multiples of 5"""
    for num in range(1, 41):
        # Discard if even
        if num % 2 == 0:
            continue
        # Discard if not a multiple of 3
        elif num % 3 != 0:
            continue
        # Discard if a multiple of 5
        elif num % 5 == 0:
            continue
        # If no conditions met, print number
        else:
            print(num)   


# Task 4.a
def my_for_loop():
    """Asks user for a word and prints whether each character is a vowel or consonant."""
    
    word = input("Enter a word (2 to 5 letters, no spaces): ")

    # Check if length is 2 through 5 and for spaces
    if len(word) < 2 or len(word) > 5 or " " in word:
        print("bad word")
        return
    
    # Check every character in the string
    vowels = "aeiouAEIOU"
    for let in word:
        if let in vowels:
            print(f"letter {let} is a vowel")
        else:
            print(f"letter {let} is a consonant")

# Task 4.b
def my_while_loop():
    """Asks user to pick a, b, or c and repeats, returns, or exits depending on what was picked"""
    while True:
        choice = input("Pick an option (a, b, or c): ")
        
        if choice == "a":
            continue
        elif choice == "b":
            print("Goodbye")
            return
        elif choice == "c":
            sys.exit()
        else:
            print("try again")   

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
