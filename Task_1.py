import itertools
import time
#Import the itertools module for creating iterators and the time module for time-related operations.

# Vigenere Cipher Encryption
def encrypt(plaintext, key):
    ciphertext = ""
    #return value for ciphertext later
    key_length = len(key)
    #calculates the length of the key.

    for i, char in enumerate(plaintext):
        #using enumerate to keep track of the current position with i (index i).
        if char.isalpha():
            # condition: if the current character char is an alphabetic character.
            shift = ord(key[i % key_length].upper()) - ord('A')
            # calculates the shift value for the current character based on the corresponding character in the key
            base = ord('a') if char.islower() else ord('A')
            # base ASCII value based on whether the current character is lowercase or uppercase.
            encrypted_char = chr(((ord(char) - base + shift) % 26) + base)
            ciphertext += encrypted_char
            #appends the encrypted character
        else:
            ciphertext += char

    return ciphertext
    #encrypted result is returned.

# Vigenere Cipher Decryption
def decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % key_length].upper()) - ord('A')
            base = ord('a') if char.islower() else ord('A')
            decrypted_char = chr(((ord(char) - base - shift + 26) % 26) + base)
            plaintext += decrypted_char
        else:
            plaintext += char

    return plaintext

# Brute force password cracker
def brute_force_cracker(ciphertext, key_length, first_word_length, dictionary):
    start_time = time.time()
    key_space = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=key_length)
    for key in key_space:
        key = ''.join(key)
        plaintext = decrypt(ciphertext, key)
        first_word = ''.join(filter(str.isalpha, plaintext))[:first_word_length].upper()
        if first_word in dictionary:
            end_time = time.time()
            print(f"Plaintext: {plaintext}")
            print(f"Key: {key}")
            print(f"Time elapsed: {end_time - start_time:.4f} seconds\n")

# Load dictionary from dictionary file text
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return {word.strip().upper() for word in file}
        #creating hashmap for efficiency search
        
if __name__ == "__main__":
    dictionary = load_dictionary("MP1_dict.txt")

    # Example test for the encrypt and decrypt functions
    plaintext = "HI"
    key = "KEY"
    #both "HI" &&"KEY" are text holder, not fixed content
    encrypted_result = encrypt(plaintext, key)
    decrypted_result = decrypt(encrypted_result, key)
   
        
    given_messages = [
        ("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX", 2, 6),
        ("PSPDYLOAFSGFREQKKPOERNIYVSDZSUOVGXSRRIPWERDIPCFSDIQZIASEJVCGXAYBGYXFPSREKFMEXEBIYDGFKREOWGXEQSXSKXGYRRRVMEKFFIPIWJSKFDJMBGCC", 3, 7),
        ("MTZHZEOQKASVBDOWMWMKMNYIIHVWPEXJA", 4, 10),
        ("SQLIMXEEKSXMDOSBITOTYVECRDXSCRURZYPOHRG", 5, 11),
    ]

    for i, (ciphertext, key_length, first_word_length) in enumerate(given_messages):
        print(f"Message {i + 1}:")
        brute_force_cracker(ciphertext, key_length, first_word_length, dictionary)