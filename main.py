import os
import platform
import time
from cryptography.fernet import Fernet

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def generate_key():
    return Fernet.generate_key()

def encrypt_text(key, text):
    f = Fernet(key)
    start_time = time.time()
    encrypted_text = f.encrypt(text.encode())
    end_time = time.time()
    elapsed_time = end_time - start_time
    return encrypted_text, elapsed_time

def decrypt_text(key, encrypted_text):
    f = Fernet(key)
    start_time = time.time()
    decrypted_text = f.decrypt(encrypted_text).decode()
    end_time = time.time()
    elapsed_time = end_time - start_time
    return decrypted_text, elapsed_time

def splash_screen():
    clear_screen()
    print("""
--------------------------------------------------
    ███████╗██╗ ██████╗██╗  ██╗███████╗██████╗ 
    ██╔════╝██║██╔════╝██║  ██║██╔════╝██╔══██╗
    ███████╗██║██║     ███████║█████╗  ██████╔╝
    ╚════██║██║██║     ██╔══██║██╔══╝  ██╔══██╗
    ███████║██║╚██████╗██║  ██║███████╗██║  ██║
    ╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     
           version 1.1 | by @bedxnta
--------------------------------------------------
""")

def write_mode():
    clear_screen()
    print("# Write mode")
    print()
    content = input("Enter your message, and press [ENTER] key to save >\n\n")
    filename = input("\nSave as... > ")
    clear_screen()
    
    key = generate_key()
    encrypted_text, encrypt_time = encrypt_text(key, content)
    
    file_path = os.path.expanduser("~/Desktop/{}.SICHER".format(filename))
    
    with open(file_path, "wb") as file:
        file.write(encrypted_text)
    
    print("Message saved to", file_path)
    print("SICHER key > ", key.decode())
    print(f"({encrypt_time:.3f} secs.)")
    print("")
    print("THIS KEY IS EXTREMELY IMPORTANT. DO NOT LOSE IT.\n In case you lose the key, you will not be able to decrypt the file contents.")
    print("")
    input("Press [ENTER] to go back...")

def read_mode():
    clear_screen()
    print("# Read mode")
    print()    
    print("Place the .SICHER file that you want to decrypt in your `Desktop` folder.")
    filename = input("Enter file name to read > ")
    file_path = os.path.expanduser("~/Desktop/{}.SICHER".format(filename))
    key = input("Enter SICHER key > ").encode()
    
    try:
        with open(file_path, "rb") as file:
            encrypted_text = file.read()
            decrypted_text, decrypt_time = decrypt_text(key, encrypted_text)
            clear_screen()
            print("\nFile decrypted! Decrypted contents of the file:\n\n", decrypted_text)
            print(f"({decrypt_time:.3f} secs.)")
    except FileNotFoundError:
        print("The file was not found.\n")
    except Exception as e:
        print("An error occurred > ", str(e))
    
    input("\n\nPress [ENTER] to go back...")

def main():
    while True:
        splash_screen()
        print("\nOPTIONS:")
        print("1. Write Mode")
        print("2. Read Mode")
        print("3. Quit")
        
        choice = input("Select an option > ")
        
        if choice == "1":
            write_mode()
        elif choice == "2":
            read_mode()
        elif choice == "3":
            break
        else:
            print("Illegal input. Try again.")

if __name__ == "__main__":
    main()
