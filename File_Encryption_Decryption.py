import os
from cryptography.fernet import Fernet

# Function to generate and saved an encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", 'wb') as key_file:
        key_file.write(key)
    print("Encryption key generated and saved to secret.key")
    return key

# Function to load the encryption key from a file
def load_key():
    return open("secret.key", 'rb').read()

# Function to encrypt a file
def encrypt_file(file_path, key):
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        original = file.read()
    
    encrypted = fernet.encrypt(original)

    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    
    print(f"File encrypted and saved to {encrypted_file_path}.")

# Function to decrypt a file
def decrypt_file(file_path, key):
    fernet = Fernet(key)

    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    
    try:
        decrypted = fernet.decrypt(encrypted)
    except Exception as e:
        print("Decryption failed. Possibly wrong key or corrupted file.")
        return
    
    if file_path.endswith('.enc'):
        decrypted_file_path = file_path[:-4] + ".decrypted.txt"
    else:
        decrypted_file_path = file_path + ".decrypted.txt"
    
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    
    print(f"File decrypted and saved to {decrypted_file_path}.")

# Main Function
def main():
    print("File Encryption/Decryption")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Choose an option (1/2): ")

    # check if key file exists, if not generate a new key
    if os.path.exists("secret.key"):
        key = load_key()
    else:
        key = generate_key()
    
    file_path = input("Enter the file path: ")

    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    if choice == '1':
        encrypt_file(file_path, key)
    elif choice == '2':
        decrypt_file(file_path, key)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()