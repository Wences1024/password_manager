import os
import json
from difflib import SequenceMatcher

menu_message = "Please enter your option: \n1.- Add new account \n2.- Search\n3.- Exit"


class CustomError(Exception):
    def __init__(self, message, *args):
        super().__init__(message)

def clear_terminal(message="") -> None:
    if len(message) < 1:
        os.system("cls | clear")
    else:
        os.system("cls | clear")
        print(message)

def menu() -> int:
    print("----Main Menu----")
    print(menu_message)
    while True:
        try:
            choice = int(input("Option: "))
        except ValueError:
            print("Please enter a valid number, not nonsense.")
        else:
            if choice > 0 and choice < 4:
                clear_terminal()
                break 
    return choice 

def add_new_account() -> int:

    while True:
        clear_terminal()
        name = input("Site name: ").strip()
        account_name = input("Account name: ").strip()
        url = input("Site URL: ").strip()
        password = input("Password: ").strip()
        notes = input("Notes: ").strip()
        clear_terminal()
        print(f"Please confirm the details: \n\nName: {name}\nAccount name: {account_name}\nURL: {url}\nPassword: {password}\nNotes: {notes}")
        
        confirm = input("y/n?: ").lower().strip()
        while confirm != 'y' and confirm !='n':
            confirm = input("y/n?: ").lower().strip()
            
        if confirm == 'y':
            clear_terminal()
            break
        else:
            continue

    new_account = {
        "name": name,
        "account_name": account_name,
        "url": url,
        "password": password,
        "notes": notes
    }
    
    # Path to the JSON file
    json_file = "manager.json"
    try:
        # Check if the JSON file exists
        if os.path.exists(json_file):
            with open(json_file, "r") as file:
                try:
                    json_object = json.load(file)
                except json.JSONDecodeError:
                    # If the file is empty or there is a decoding error
                    json_object = {}
        else:
            json_object = {}
        
        # Check if the account already exists
        if name.lower() in json_object:
            raise CustomError("The account already exists \n")
        
        # Add the account
        json_object[name.lower()] = new_account
        
        # Save the updated data to the file
        with open(json_file, "w") as file:
            sorted(json_object)
            json.dump(json_object, file, indent=4)
            
            
    except CustomError as e:
        print(e)
        return 4
    except (OSError, IOError) as e:
        print("Error handling the JSON file: ", e)
        return 4
    else:
        clear_terminal("Data saved\n")
        return 4

def get_similar_words(user_word, json_object) -> list:
    word_list = [word.lower() for word in json_object]
    
    similar_words = [
        word for word in word_list
        if SequenceMatcher(None, user_word, word).ratio() >= 0.7
    ]
    
    return similar_words

def return_to_menu() -> str:
    while True:
        response = input("y -> Main menu, n -> Stay in the current menu: ").strip().lower()
        if response == 'y' or response == 'n':
            break
    return response
        
def search() -> int:
    match_found = False
    file_path = "manager.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                json_object = json.load(file)
            except json.JSONDecodeError:
                raise CustomError("Error opening JSON file, or it is empty.")
    
    while True:   
        search_term = input("Please enter the account name to search: ").strip().lower()
        for account in json_object:
            if account == search_term:
                match_found = True
                clear_terminal()
                print(f"\nName: {json_object[account]['name']}")
                print(f"Account name: {json_object[account]['account_name']}")
                print(f"Password: {json_object[account]['password']}")
                print(f"URL: {json_object[account]['url']}")
                print(f"Notes: {json_object[account]['notes']}\n")
        
        if match_found:
            return_to_menu_option = return_to_menu()
            clear_terminal()
            if return_to_menu_option == 'y':
                break
            elif return_to_menu_option == 'n':
                return 2
            else:
                continue
        else:
            clear_terminal()
            suggestions = get_similar_words(search_term, json_object)
            if len(suggestions) < 1:
                print(f"No matches found for '{search_term}'")
            else:
                print(f"No exact matches found for '{search_term}'")
                print("Did you mean:")
                for suggestion in suggestions:
                    print(suggestion)
                
                return_to_menu_option = return_to_menu()
                clear_terminal()                
                if return_to_menu_option == 'y':
                    break
                elif return_to_menu_option == 'n':
                    return 2
                else:
                    continue                 

    return 4
        
if __name__ == "__main__":
    clear_terminal()
    print("Password manager initialized\n")
    choice = menu()    
    while True:
        match choice:
            case 1:
                choice = add_new_account()
            case 2:
                choice = search()
            case 3:
                clear_terminal()
                print("Password manager closed. Bye")
                break
            case 4:
                choice = menu()
