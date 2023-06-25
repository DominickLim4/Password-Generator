import random

class Password:
    def __init__(self, name, birthday) -> None:
        self.__name = name
        self.__birthday = birthday

    @property
    def name(self):
        return self.__name
    
    @property
    def birthday(self):
        return self.__birthday

    def nextLetter(self):
        # List to store the next letters
        nextLetters = []
        for letter in range(len(self.name)):
            # Get the ASCII value of the current letter
            ascii_value = ord(self.name[letter])
            # Increment the ASCII value by 1 to get the next letter
            next_ascii_value = ascii_value + 1
            # Convert the ASCII value back to a character
            next_letter = chr(next_ascii_value)
            # Append the next letter to the list
            nextLetters.append(next_letter)
        # Join the next letters into a single string
        separator = ''
        nextString = separator.join(nextLetters)
        return nextString

def generateSpecialWord():
    # List of special characters
    specialWord = ['!', '@', '#', '$', '%', '&', '*']
    # Generate a random index to choose a special character from the list
    randomIndex = specialWord[random.randint(0, 6)]
    return randomIndex

if __name__ == '__main__':
    # Create a Password instance with a name and birthday
    user = Password("Matheus", 11)
    # Print a randomly generated special character, next letter of the name, and the birthday
    print(generateSpecialWord() + user.nextLetter() + str(user.birthday))
