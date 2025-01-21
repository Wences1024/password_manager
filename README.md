# Password Manager

This project is a simple password manager based on Python. It allows you to store and retrieve accounts in a JSON file to maintain an organized record of access credentials. **It is important to note that this manager is not designed to store passwords for critical accounts or highly sensitive information.**



## Features

1. **Add a new account**: Enter information such as site name, URL, password, and additional notes.
2. **Retrieve stored accounts**: Search for saved accounts by name and view their information.
3. **Smart suggestions**: If an exact match is not found, the system suggests similar accounts.


## Requirements

1. **Python 3.7 or higher**.
2. Standard libraries (no additional libraries needed).


## Installation

1. Clone this repository:
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   ```
2. Navigate to the project directory:
   ```bash
   cd password_manager
   ```
3. Run the script:
   ```bash
   python manager.py
   ```

## Usage

1. Run the script and select an option from the main menu.
2. Follow the interactive instructions to add or retrieve accounts..
3. Credentials are stored in a `gestor.json` file located in the same directory as the script..

## Advantages

- **Simplicity**: Ideal for storing basic account information.
- **Lightweight**: No external dependencies or complex setups.
- **User-friendly interface**: Text-based interactive menu.


## Disadvantages

- **Limited security**: Passwords are stored in plain text.

- **Restricted scope**: Does not support advanced features like cloud synchronization or two-factor authentication.

## Warning

This manager is designed solely to store non-critical account information, such as subscriptions or low-importance services. **If you need to store sensitive information, use a professional password manager like LastPass, Bitwarden, or 1Password.**

## Recommended Improvements

1. **Encryption**: Implement a mechanism to encrypt passwords before storing them.
2. **Validations**: Ensure URLs and passwords meet certain security standards.
3. **Cross-platform compatibility**: Improve the terminal clearing command compatibility across different operating systems.

---

Thank you for using this password manager! Feel free to contribute to the project by submitting your suggestions or improvements.