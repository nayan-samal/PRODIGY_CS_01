def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

if choice == 'e':
    print("Encrypted Message:", encrypt(message, shift))
elif choice == 'd':
    print("Decrypted Message:", decrypt(message, shift))
else:
    print("Invalid choice!")