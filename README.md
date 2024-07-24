# Password-Strength-Checker


**Overview:**
This Python tool checks the strength of passwords. 
It offers an easy-to-understand method of determining how secure your passwords are by calculating a password's strength depending on its length and complexity.


**Features:**
Determines the strength of a password by its length and complexity.
offers a user-friendly interface that is easy to use for entering and checking passwords.
shows a progress meter and a strength level (Weak, Medium, Strong) to help visualize the security of the password.


**Usage:**
Clone or download this repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt (if you're using a virtual environment, make sure to activate it first).
Run the script by executing python password_strength_checker.py (or the name of your Python script).
Enter a password in the input field and click the "Evaluate Password" button.
The tool will display the password strength rating and a progress bar indicating the password's security.

**How It Operates:**
The password strength checker determines a password's strength based on its length and complexity using a straightforward method. The following criteria are checked by the algorithm:

**Length:**
Passwords shorter than 10 characters are considered weak, while those between 10 and 14 characters are considered medium strength. Passwords 14 characters or longer are considered strong.
Complexity: The tool checks for a mix of uppercase and lowercase letters, numbers, and special characters.




