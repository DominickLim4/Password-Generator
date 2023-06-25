# Password Generator

This is a simple Python program that generates a password by combining a randomly chosen special character, the next letter of a name, and a birthday. The program showcases the usage of classes, properties, and random number generation in Python.

## Usage

1. Make sure you have Python installed on your system.
2. Clone the repository or download the `randomPassword.py` file.
3. Open a terminal or command prompt and navigate to the directory where the `randomPassword.py` file is located.
4. Run the following command to execute the program:

   ```bash
   python randomPassword.py
   
## Code Explanation
The code consists of the following components:

- Password class: Represents a password object and contains properties for name and birthday.
- nextLetter method: Iterates over the name characters, converts them to ASCII values, increments each value by 1 to get the next letter, and returns the resulting string.
- generateSpecialWord function: Returns a randomly chosen special character from a list of predefined special characters.
- Main code: Creates an instance of the Password class with a name and birthday, generates a special character, retrieves the next letter, and concatenates everything into a password string. The password is then printed to the console.
Feel free to modify the code to suit your needs!
